<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-CJQWKW82 -->

# ANT-2026-CJQWKW82 · postgres/postgres

## denial-of-service high

[CVE-2026-6479](https://nvd.nist.gov/vuln/detail/CVE-2026-6479)
[GHSA-hwfh-mh4f-m67f](https://github.com/advisories/GHSA-hwfh-mh4f-m67f)

Maintainer high

Claude Opus 4.6

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-CJQWKW82: Pre-auth unbounded recursion in ProcessStartupPacket: alternating SSL/GSS negotiation requests cause infinite recursion when both are rejected. ssl\_done/gss\_done flags oscillate (true,false)->(false,true) endlessly. No check\_stack\_depth. Pre-authentication.

Unauthenticated attacker alternates SSL and GSS request packets. After ~40K-80K exchanges the backend crashes from stack overflow (SIGSEGV). On localhost takes seconds. AuthenticationTimeout (60s) is only time bound.

**Project:** postgres/postgres
**Commit:** `5241616289cc64e0`
**Location:** `src/backend/tcop/backend_startup.c:637`

When SSL is rejected, line 637 recurses with ProcessStartupPacket(port, true, SSLok == 'S') → (true,false); when GSS is rejected, line 693 recurses with ProcessStartupPacket(port, GSSok == 'G', true) → (false,true). The guards at lines 574 (!ssl\_done) and 639 (!gss\_done) therefore never both stay true, so alternating requests re-enter forever. No check\_stack\_depth(), counter, or iteration cap exists in the path, so the recursion terminates only via stack exhaustion (SIGSEGV).

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-CJQWKW82.

---

**Reference:** ANT-2026-CJQWKW82

Triage and disclosure were performed by Calif.

UPSTREAM FIX

The change that resolved this finding.

```
diff --git a/src/backend/tcop/backend_startup.c b/src/backend/tcop/backend_startup.c
index 5abf276c89848..a810e41a9040e 100644
--- a/src/backend/tcop/backend_startup.c
+++ b/src/backend/tcop/backend_startup.c
@@ -496,6 +496,7 @@ ProcessStartupPacket(Port *port, bool ssl_done, bool gss_done)
 	ProtocolVersion proto;
 	MemoryContext oldcontext;

+retry:
 	pq_startmsgread();

 	/*
@@ -616,6 +617,7 @@ ProcessStartupPacket(Port *port, bool ssl_done, bool gss_done)
 #endif

 		pfree(buf);
+		buf = NULL;

 		/*
 		 * At this point we should have no data already buffered.  If we do,
@@ -634,7 +636,16 @@ ProcessStartupPacket(Port *port, bool ssl_done, bool gss_done)
 		 * another SSL negotiation request, and a GSS request should only
 		 * follow if SSL was rejected (client may negotiate in either order)
 		 */
-		return ProcessStartupPacket(port, true, SSLok == 'S');
+		ssl_done = true;
+		if (SSLok == 'S')
+		{
+			/*
+			 * We are done with SSL and negotiated correctly, so consider the
+			 * same for GSS.
+			 */
+			gss_done = true;
+		}
+		goto retry;
 	else if (proto == NEGOTIATE_GSS_CODE && !gss_done)
@@ -672,6 +683,7 @@ ProcessStartupPacket(Port *port, bool ssl_done, bool gss_done)
 #endif

 		pfree(buf);
+		buf = NULL;

 		/*
 		 * At this point we should have no data already buffered.  If we do,
@@ -690,7 +702,16 @@ ProcessStartupPacket(Port *port, bool ssl_done, bool gss_done)
 		 * another GSS negotiation request, and an SSL request should only
 		 * follow if GSS was rejected (client may negotiate in either order)
 		 */
-		return ProcessStartupPacket(port, GSSok == 'G', true);
+		gss_done = true;
+		if (GSSok == 'G')
+		{
+			/*
+			 * We are done with GSS and negotiated correctly, so consider the
+			 * same for SSL.
+			 */
+			ssl_done = true;
+		}
+		goto retry;

 	/* Could add additional special packet types here */
diff --git a/src/test/postmaster/meson.build b/src/test/postmaster/meson.build
index d2709867da71c..fa30883b601bd 100644
--- a/src/test/postmaster/meson.build
+++ b/src/test/postmaster/meson.build
@@ -9,6 +9,7 @@ tests += {
       't/001_basic.pl',
       't/002_connection_limits.pl',
       't/003_start_stop.pl',
+      't/004_negotiate.pl',
   },
diff --git a/src/test/postmaster/t/004_negotiate.pl b/src/test/postmaster/t/004_negotiate.pl
new file mode 100644
index 0000000000000..949aa2ba19ac0
--- /dev/null
+++ b/src/test/postmaster/t/004_negotiate.pl
@@ -0,0 +1,83 @@
+# Copyright (c) 2026, PostgreSQL Global Development Group
+
+# Test the negotiation of combined SSL and GSS requests.  This test
+# relies on both SSL and GSS requests to be rejected first, followed
+# by more requests.
+
+use strict;
+use warnings FATAL => 'all';
+use PostgreSQL::Test::Cluster;
+use PostgreSQL::Test::Utils;
+use Test::More;
+use Time::HiRes qw(usleep);
+
+my $node = PostgreSQL::Test::Cluster->new('main');
+$node->init;
+$node->append_conf('postgresql.conf', "log_min_messages = debug2");
+$node->append_conf('postgresql.conf',
+	"log_connections = 'receipt,authentication,authorization'");
+$node->append_conf('postgresql.conf', 'trace_connection_negotiation=on');
+$node->start;
+
+if (!$node->raw_connect_works())
+{
+	plan skip_all => "this test requires working raw_connect()";
+}
+
+my $sock = $node->raw_connect();
+
+# SSLRequest: packet length followed by NEGOTIATE_SSL_CODE.
+my $ssl_request = pack("Nnn", 8, 1234, 5679);
+
+# GSSENCRequest: packet length followed by NEGOTIATE_GSS_CODE.
+my $gss_request = pack("Nnn", 8, 1234, 5680);
+
+# Send SSLRequest, reject or bypass.
+$sock->send($ssl_request);
+my $reply = "";
+$sock->recv($reply, 1);
+if ($reply ne 'N')
+{
+	$sock->close();
+	plan skip_all =>
+	  "server accepted SSL; test requires SSL to be rejected";
+}
+
+# Send GSSENCRequest, reject or bypass test.
+$sock->send($gss_request);
+$reply = "";
+$sock->recv($reply, 1);
+if ($reply ne 'N')
+{
+	$sock->close();
+	plan skip_all =>
+	  "server accepted GSS; test requires GSS to be rejected";
+}
+
+my $log_offset = -s $node->logfile;
+
+# Send a second SSLRequest, now that we know that both SSL and GSS have
+# been rejected for this connection.  We are done with both requests, so
+# extra requests will be rejected and fail with an invalid protocol
+# version, and the connection should be closed by the server.
+$sock->send($ssl_request);
+
+# Try to read a response, there should be nothing, and certainly not an
+# extra 'N' message indicating a rejection.
+$reply = "";
+my $bytes = $sock->recv($reply, 1024);
+isnt($reply, 'N',
+	"server does not re-enter SSL negotiation after SSL+GSS were both tried");
+
+$sock->close();
+$node->wait_for_log(qr/FATAL: .* unsupported frontend protocol 1234.5679/,
+					$log_offset);
+
+# Check extra connection with a simple query.
+my $result = $node->safe_psql('postgres', 'select 1;');
+is($result, '1', 'server able to accept connection');
+ok($node->is_alive(), "server still running after negotiation attempt");
+
+$node->stop;
+
+done_testing();
```

<https://github.com/postgres/postgres/commit/b63f25bddfebc67b1e78f86341a6aecb0e9fe576>

1. 2026-04-01
2. 2026-05-08
3. 2026-05-09
4. 2026-05-14
5. 2026-07-21

6ccb97193bc23f5185d8846690778b6b553b97c7a27eff1ae8a5e80c0f404193c5d139372722332faa52572e486f6d0512238b53e885233b5bf7d1c8d3589f5a

Committed 2026-05-08 00:09 PT

Revealed 2026-07-21 11:01 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-CJQWKW82%22%2C%22bug_class%22%3A%22Denial-of-service%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%225241616289cc64e0%22%2C%22created_at%22%3A%222026-04-02T05%3A09%3A32%2B00%3A00%22%2C%22description%22%3A%22Unauthenticated%20attacker%20alternates%20SSL%20and%20GSS%20request%20packets.%20After%20~40K-80K%20exchanges%20the%20backend%20crashes%20from%20stack%20overflow%20%28SIGSEGV%29.%20On%20localhost%20takes%20seconds.%20AuthenticationTimeout%20%2860s%29%20is%20only%20time%20bound.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22src/backend/tcop/backend_startup.c%3A637%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22postgres/postgres%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22When%20SSL%20is%20rejected%2C%20line%20637%20recurses%20with%20ProcessStartupPacket%28port%2C%20true%2C%20SSLok%20%3D%3D%20%27S%27%29%20%E2%86%92%20%28true%2Cfalse%29%3B%20when%20GSS%20is%20rejected%2C%20line%20693%20recurses%20with%20ProcessStartupPacket%28port%2C%20GSSok%20%3D%3D%20%27G%27%2C%20true%29%20%E2%86%92%20%28false%2Ctrue%29.%20The%20guards%20at%20lines%20574%20%28%21ssl_done%29%20and%20639%20%28%21gss_done%29%20therefore%20never%20both%20stay%20true%2C%20so%20alternating%20requests%20re-enter%20forever.%20No%20check_stack_depth%28%29%2C%20counter%2C%20or%20iteration%20cap%20exists%20in%20the%20path%2C%20so%20the%20recursion%20terminates%20only%20via%20stack%20exhaustion%20%28SIGSEGV%29.%22%2C%22title%22%3A%22Pre-auth%20unbounded%20recursion%20in%20ProcessStartupPacket%3A%20alternating%20SSL/GSS%20negotiation%20requests%20cause%20infinite%20recursion%20when%20both%20are%20rejected.%20ssl_done/gss_done%20flags%20oscillate%20%28true%2Cfalse%29-%3E%28false%2Ctrue%29%20endlessly.%20No%20check_stack_depth.%20Pre-authentication.%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-CJQWKW82",
  "bug_class": "Denial-of-service",
  "commit_sha": "5241616289cc64e0",
  "created_at": "2026-04-02T05:09:32+00:00",
  "description": "Unauthenticated attacker alternates SSL and GSS request packets. After ~40K-80K exchanges the backend crashes from stack overflow (SIGSEGV). On localhost takes seconds. AuthenticationTimeout (60s) is only time bound.",
  "location": "src/backend/tcop/backend_startup.c:637",
  "project": "postgres/postgres",
  "technical_details": "When SSL is rejected, line 637 recurses with ProcessStartupPacket(port, true, SSLok == 'S') → (true,false); when GSS is rejected, line 693 recurses with ProcessStartupPacket(port, GSSok == 'G', true) → (false,true). The guards at lines 574 (!ssl_done) and 639 (!gss_done) therefore never both stay true, so alternating requests re-enter forever. No check_stack_depth(), counter, or iteration cap exists in the path, so the recursion terminates only via stack exhaustion (SIGSEGV).",
  "title": "Pre-auth unbounded recursion in ProcessStartupPacket: alternating SSL/GSS negotiation requests cause infinite recursion when both are rejected. ssl_done/gss_done flags oscillate (true,false)->(false,true) endlessly. No check_stack_depth. Pre-authentication.",
```
