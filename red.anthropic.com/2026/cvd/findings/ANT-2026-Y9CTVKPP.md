<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-Y9CTVKPP -->

# ANT-2026-Y9CTVKPP · jetty/jetty.project

## denial-of-service high

[GHSA-85fq-fc5f-7j7g](https://github.com/jetty/jetty.project/security/advisories/GHSA-85fq-fc5f-7j7g)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-Y9CTVKPP: WebSocket reserved opcode bypasses frame size limits

In Jetty's WebSocket core Parser, checkFrameSize() only enforces maxFrameSize for control or data opcodes, and the else-branch check is disabled when autoFragment is true (the default). Reserved opcodes 0x03-0x07 and 0x0B-0x0F therefore skip both the size check and the auto-fragment clamps in parsePayload(), and execution reaches bufferPool.acquire(payloadLength) at Parser.java:346 with an attacker-controlled 63-bit length truncated to int (up to Integer.MAX\_VALUE). ArrayByteBufferPool falls through to a raw ByteBuffer.allocate of ~2 GiB, and the illegal opcode is only rejected afterward in newFrame()/FrameSequence. A single ~15-byte frame header sent after a WebSocket upgrade thus forces a ~2 GiB heap allocation per connection, allowing an unauthenticated remote attacker to drive the JVM to OutOfMemoryError and take down every hosted application.

**Project:** jetty/jetty.project
**Location:** `jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java:346`

OpCode.isControlFrame() and OpCode.isDataFrame() both return false for reserved opcodes, so Parser.checkFrameSize() (lines 265-275) falls into an else branch whose throw is gated by !configuration.isAutoFragment() — with DEFAULT\_AUTO\_FRAGMENT=true no limit is applied. parsePayload()'s fragment clamps at lines 333/341 require isDataFrame==true and are also skipped, so aggregate = bufferPool.acquire(payloadLength, false) at line 346 runs with attacker-controlled payloadLength before the only opcode validation (OpCode.isKnown() in newFrame(), line 282) executes.

1. Complete a WebSocket handshake against the target Jetty endpoint.
2. Send a frame with FIN=1, opcode=0x03 (reserved), MASK=1, payload-len=127, 8-byte extended length = 0x000000007FFFFFF0, a 4-byte masking key, and at least 1 payload byte.
3. Parser.parsePayload() calls bufferPool.acquire(~2 GiB) before validating the opcode.
4. Repeat over a handful of concurrent connections to exhaust the JVM heap and trigger OutOfMemoryError.

## Suggested Fix

Reject frames with reserved/unknown opcodes before any payload-length-dependent processing, and enforce the configured maximum frame size unconditionally for all opcode categories.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-Y9CTVKPP.

---

**Reference:** ANT-2026-Y9CTVKPP

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

Jetty's WebSocket frame parser rejects an oversized frame and validates the frame opcode at two different points, and for a reserved opcode the ordering lets an attacker force a multi-gigabyte allocation before the opcode is ever checked. When `Parser.parse()` has read a frame header it calls `checkFrameSize(opcode, payloadLength)`, but the non-control branch of that method only enforces `maxFrameSize` when auto-fragmentation is disabled, and auto-fragmentation is on by default. It then calls `parsePayload()`, whose auto-fragment clamps apply only to data frames (`CONTINUATION`/`TEXT`/`BINARY`). A reserved opcode such as `0x03` is neither a control frame nor a data frame, so it slips past both guards and reaches `aggregate = bufferPool.acquire(payloadLength, false)`, allocating the full attacker-declared payload length up to `Integer.MAX_VALUE` in one go. The opcode is only validated later, inside `newFrame()` via `OpCode.isKnown()`, which is reached after the allocation has already been requested. A single WebSocket frame header of about fifteen bytes therefore forces a roughly 2 GiB heap allocation and causes OutOfMemoryError.

## Root cause

`Parser.parse()` reads the frame header, decodes the declared `payloadLength` (the 8-byte extended length is masked down to a non-negative `int`, so it can be as large as `Integer.MAX_VALUE`), and calls the size checking logic.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java#L221

`checkFrameSize` method rejects oversized control frames, but for everything else the only throw is gated on auto-fragmentation being off.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java#L260-L276

Auto-fragmentation is on by default.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/WebSocketConstants.java#L58

`Configuration.isAutoFragment()` returns that default when the value is unset.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/Configuration.java#L111-L114

So with the shipped defaults the `!isAutoFragment()` condition is false and the `maxFrameSize` rejection is skipped for every non-control frame, including reserved opcodes.

The design intent is that the size limit is enforced later, by clamping through auto-fragmentation in `parsePayload()`. But that clamping is conditined on the frame being a data frame.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java#L328-L348

`OpCode.isDataFrame()` returns true only for `CONTINUATION`, `TEXT` and `BINARY`, the other opcode is considered reserved and not a data frae.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/OpCode.java#L83-L94

For a reserved opcode such as `0x03`, `isDataFrame` is false, so both auto-fragment paths (the size clamp at line 333 and the insufficient-data clamp at line 341) are skipped, and execution falls straight through to the `bufferPool.acquire(payloadLength, false)` call at line 346 shown above, which requests a buffer of the full declared length.

The opcode is only validated afterwards, inside `newFrame()`.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java#L278-L291

`OpCode.isKnown()` would throw `ProtocolException` for the reserved opcode `0x03` by returning false.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/OpCode.java#L102-L116

That check comes too late: the roughly 2 GiB `acquire` at earlier line has already run. The reserved opcode is the exact input that evades both the `maxFrameSize` rejection and the auto-fragment clamp, so it is the one case that reaches an unbounded allocation. A legitimate `BINARY` frame with the same declared length is safe precisely because `isDataFrame` is true and it is clamped to `maxFrameSize`

The parser runs on the connection read path with the live session configuration. `WebSocketConnection` constructs its `Parser` from the core session.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/WebSocketConnection.java#L153

It drives the parser from `onFillable()`.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/WebSocketConnection.java#L363

That path reaches the `parser.parse(...)` call on the network buffer, all before the frame is delivered to any application handler.

https://github.com/jetty/jetty.project/blob/852c52def077bd7878807b2534c36cb618f7b03a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/WebSocketConnection.java#L497

## Proof of Concept

The reproducer drives the real upstream `Parser` with a default `Configuration` (`autoFragment=true`, `maxFrameSize=64KiB`) and feeds it two single frames: a negative control with data opcode `0x02` (BINARY) and the attack frame with reserved opcode `0x03`, both declaring a payload length of `0x7FFFFFF0` (about 2 GiB). It runs under `-Xmx256m` so that the unbounded allocation deterministically fails with `OutOfMemoryError`, while the clamped control survives, and it unwinds the thrown exception to print the Jetty allocation stack. This is a component-level harness against the shipped parser; the network path that reaches it (`onFillable` to `parse`) is established by source above rather than exercised over a socket.

[Harness.java](https://github.com/user-attachments/files/29643513/Harness.java)

```
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

ARG TARGET_COMMIT=95efeb2bf041bc6b7a5da91b281499592417371b

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates git openjdk-17-jdk-headless maven \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/jetty/jetty.project /src/repo
WORKDIR /src/repo
RUN git checkout ${TARGET_COMMIT}

# Build jetty-websocket-core-common
RUN mvn -q -B -P'!config' -pl jetty-core/jetty-websocket/jetty-websocket-core-common -am install \
        -DskipTests -Dmaven.test.skip=true \
        -Dcheckstyle.skip=true -Dspotbugs.skip=true -Denforcer.skip=true \
        -Dmaven.javadoc.skip=true -Dlicense.skip=true -Dsource.skip=true \
        -Dmaven.source.skip=true -Djapicmp.skip=true

# Assemble the runtime classpath of the module into /tmp/cp.txt.
RUN mvn -q -B -pl jetty-core/jetty-websocket/jetty-websocket-core-common \
        dependency:build-classpath -Dmdep.outputFile=/tmp/cp.txt -Denforcer.skip=true

# Compile the reproducer harness against the freshly built module + its deps.
ENV MODCLASSES=/src/repo/jetty-core/jetty-websocket/jetty-websocket-core-common/target/classes
COPY Harness.java /tmp/Harness.java
RUN javac -cp "${MODCLASSES}:$(cat /tmp/cp.txt)" -d /tmp /tmp/Harness.java

# Small heap so the unbounded ~2 GiB allocation deterministically OOMs (proving the
# allocation is unbounded), while the negative control (clamped to 64KiB) survives.
CMD ["/bin/sh","-c","java -Xmx256m -cp \"/tmp:${MODCLASSES}:$(cat /tmp/cp.txt)\" Harness 2>&1; echo EXIT=$?"]
```

```
docker build -t poc . && docker run --rm poc
```

### Result

```
Heap max: 256 MiB

--- NEGATIVE CONTROL: data opcode 0x02 (BINARY) ---
[control] opcode=0x02 declared payloadLength=2147483632 (2047 MiB)
[control] sending 15-byte frame header, then parse()...
[control] parse() returned without large allocation (clamped/auto-fragmented)

--- ATTACK: reserved opcode 0x03 ---
[attack] opcode=0x03 declared payloadLength=2147483632 (2047 MiB)
[attack] sending 15-byte frame header, then parse()...
[attack] *** OutOfMemoryError *** triggered by a 15-byte frame header: Java heap space
[attack] VULNERABILITY CONFIRMED: bufferPool.acquire(2147483632) ran before opcode validation. Allocation site:
    at org.eclipse.jetty.util.BufferUtil.allocate(BufferUtil.java:127)
    at org.eclipse.jetty.util.BufferUtil.allocate(BufferUtil.java:158)
    at org.eclipse.jetty.io.ArrayByteBufferPool.acquire(ArrayByteBufferPool.java:241)
    at org.eclipse.jetty.websocket.core.internal.Parser.parsePayload(Parser.java:346)
    at org.eclipse.jetty.websocket.core.internal.Parser.parse(Parser.java:222)
```

The reserved-opcode frame reaches `bufferPool.acquire(2147483632)` at `Parser.parsePayload` and throws `OutOfMemoryError` under the small heap, while the identical data-opcode frame is clamped by auto-fragmentation and returns without a large allocation. In a live server the same roughly 2 GiB allocation is held per connection while the parser awaits the remainder of the frame, so a small number of concurrent frames exhausts the heap and denies service across the whole JVM.

## Mitigation

Validate the opcode before allocating for the payload: call `OpCode.isKnown()` at the start of `checkFrameSize()` or before `parsePayload()` acquires a buffer, so an unknown opcode is refused early while only the header has been read.

## Attribution

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged manually with manual report writing by Ada Logics in collaboration with Anthropic Research.

```
diff --git a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java b/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java
index 7626f40a596..184a53b26ee 100644
--- a/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java
+++ b/jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java
@@ -107,6 +107,7 @@ public Frame.Parsed parse(ByteBuffer buffer) throws WebSocketException
                         // peek at byte
                         firstByte = buffer.get();
                         state = State.PAYLOAD_LEN;
+                        checkFirstByte(firstByte);
                         break;

@@ -257,6 +258,19 @@ else if (payloadLength == 0)
         return null;

+    protected void checkFirstByte(byte firstByte)
+    {
+        // Validate OpCode
+        byte opcode = OpCode.getOpCode(firstByte);
+        if (!OpCode.isKnown(opcode))
+            throw new ProtocolException("Unknown opcode: " + opcode);
+
+        // Validate Control Frame
+        boolean fin = ((firstByte & 0x80) != 0);
+        if (OpCode.isControlFrame(opcode) && !fin)
+            throw new ProtocolException("Fragmented Control Frame [" + OpCode.name(opcode) + "]");
+    }
+
     protected void checkFrameSize(byte opcode, int payloadLength) throws MessageTooLargeException, ProtocolException
         if (payloadLength < 0)
@@ -267,26 +281,20 @@ protected void checkFrameSize(byte opcode, int payloadLength) throws MessageTooL
             if (payloadLength > Frame.MAX_CONTROL_PAYLOAD)
                 throw new ProtocolException("Invalid control frame payload length, [" + payloadLength + "] cannot exceed [" + Frame.MAX_CONTROL_PAYLOAD + "]");
-        else
+        else if (OpCode.isDataFrame(opcode))
             long maxFrameSize = configuration.getMaxFrameSize();
             if (!configuration.isAutoFragment() && maxFrameSize > 0 && payloadLength > maxFrameSize)
                 throw new MessageTooLargeException("Cannot handle payload lengths larger than " + maxFrameSize);
+        else
+        {
+            throw new ProtocolException("Unknown opcode: " + opcode);
+        }

     protected Frame.Parsed newFrame(byte firstByte, byte[] mask, ByteBuffer payload, Runnable releaser)
-        // Validate OpCode
-        byte opcode = OpCode.getOpCode(firstByte);
-        if (!OpCode.isKnown(opcode))
-            throw new ProtocolException("Unknown opcode: " + opcode);
-
-        // Validate Control Frame
-        boolean fin = ((firstByte & 0x80) != 0);
-        if (OpCode.isControlFrame(opcode) && !fin)
-            throw new ProtocolException("Fragmented Control Frame [" + OpCode.name(opcode) + "]");
-
         return new Frame.Parsed(firstByte, mask, payload, releaser);

diff --git a/jetty-core/jetty-websocket/jetty-websocket-core-server/src/main/java/org/eclipse/jetty/websocket/core/server/internal/RFC6455Handshaker.java b/jetty-core/jetty-websocket/jetty-websocket-core-server/src/main/java/org/eclipse/jetty/websocket/core/server/internal/RFC6455Handshaker.java
index a9a2c19c0a4..1742c10ba81 100644
--- a/jetty-core/jetty-websocket/jetty-websocket-core-server/src/main/java/org/eclipse/jetty/websocket/core/server/internal/RFC6455Handshaker.java
+++ b/jetty-core/jetty-websocket/jetty-websocket-core-server/src/main/java/org/eclipse/jetty/websocket/core/server/internal/RFC6455Handshaker.java
@@ -77,10 +77,11 @@ protected boolean validateNegotiation(WebSocketNegotiation negotiation)
     @Override
     protected WebSocketConnection createWebSocketConnection(Request baseRequest, WebSocketCoreSession coreSession)
+        WebSocketComponents components = coreSession.getWebSocketComponents();
         ConnectionMetaData connectionMetaData = baseRequest.getConnectionMetaData();
         Connector connector = connectionMetaData.getConnector();
         EndPoint endPoint = connectionMetaData.getConnection().getEndPoint();
-        return newWebSocketConnection(endPoint, connector.getExecutor(), connector.getScheduler(), connector.getByteBufferPool(), coreSession);
+        return newWebSocketConnection(endPoint, components.getExecutor(), connector.getScheduler(), components.getByteBufferPool(), coreSession);

     @Override
```

<https://github.com/jetty/jetty.project/commit/b5bdc24629cac46ed51c12de11afd7a068cb3b48>

1. 2026-04-02
2. 2026-07-22
3. 2026-07-22
4. 2026-08-04
5. 2026-09-28

02d2070d13dafd3b1d7788dc77f0547d32da15bb8053ba64bb1f63a13403631f7b91237816ab5daa27b3b62ddab2fe85b44cfa74b17cc7805f0816d724029a71

Committed 2026-07-22 07:33 UTC

Revealed 2026-09-28 22:29 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-Y9CTVKPP%22%2C%22bug_class%22%3A%22Denial%20of%20Service%20/%20Resource%20Exhaustion%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T02%3A39%3A24%2B00%3A00%22%2C%22description%22%3A%22In%20Jetty%27s%20WebSocket%20core%20Parser%2C%20checkFrameSize%28%29%20only%20enforces%20maxFrameSize%20for%20control%20or%20data%20opcodes%2C%20and%20the%20else-branch%20check%20is%20disabled%20when%20autoFragment%20is%20true%20%28the%20default%29.%20Reserved%20opcodes%200x03-0x07%20and%200x0B-0x0F%20therefore%20skip%20both%20the%20size%20check%20and%20the%20auto-fragment%20clamps%20in%20parsePayload%28%29%2C%20and%20execution%20reaches%20bufferPool.acquire%28payloadLength%29%20at%20Parser.java%3A346%20with%20an%20attacker-controlled%2063-bit%20length%20truncated%20to%20int%20%28up%20to%20Integer.MAX_VALUE%29.%20ArrayByteBufferPool%20falls%20through%20to%20a%20raw%20ByteBuffer.allocate%20of%20~2%20GiB%2C%20and%20the%20illegal%20opcode%20is%20only%20rejected%20afterward%20in%20newFrame%28%29/FrameSequence.%20A%20single%20~15-byte%20frame%20header%20sent%20after%20a%20WebSocket%20upgrade%20thus%20forces%20a%20~2%20GiB%20heap%20allocation%20per%20connection%2C%20allowing%20an%20unauthenticated%20remote%20attacker%20to%20drive%20the%20JVM%20to%20OutOfMemoryError%20and%20take%20down%20every%20hosted%20application.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java%3A346%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22jetty/jetty.project%22%2C%22reproduction%22%3A%5B%221.%20Complete%20a%20WebSocket%20handshake%20against%20the%20target%20Jetty%20endpoint.%22%2C%222.%20Send%20a%20frame%20with%20FIN%3D1%2C%20opcode%3D0x03%20%28reserved%29%2C%20MASK%3D1%2C%20payload-len%3D127%2C%208-byte%20extended%20length%20%3D%200x000000007FFFFFF0%2C%20a%204-byte%20masking%20key%2C%20and%20at%20least%201%20payload%20byte.%22%2C%223.%20Parser.parsePayload%28%29%20calls%20bufferPool.acquire%28~2%20GiB%29%20before%20validating%20the%20opcode.%22%2C%224.%20Repeat%20over%20a%20handful%20of%20concurrent%20connections%20to%20exhaust%20the%20JVM%20heap%20and%20trigger%20OutOfMemoryError.%22%5D%2C%22technical_details%22%3A%22OpCode.isControlFrame%28%29%20and%20OpCode.isDataFrame%28%29%20both%20return%20false%20for%20reserved%20opcodes%2C%20so%20Parser.checkFrameSize%28%29%20%28lines%20265-275%29%20falls%20into%20an%20else%20branch%20whose%20throw%20is%20gated%20by%20%21configuration.isAutoFragment%28%29%20%E2%80%94%20with%20DEFAULT_AUTO_FRAGMENT%3Dtrue%20no%20limit%20is%20applied.%20parsePayload%28%29%27s%20fragment%20clamps%20at%20lines%20333/341%20require%20isDataFrame%3D%3Dtrue%20and%20are%20also%20skipped%2C%20so%20aggregate%20%3D%20bufferPool.acquire%28payloadLength%2C%20false%29%20at%20line%20346%20runs%20with%20attacker-controlled%20payloadLength%20before%20the%20only%20opcode%20validation%20%28OpCode.isKnown%28%29%20in%20newFrame%28%29%2C%20line%20282%29%20executes.%22%2C%22title%22%3A%22WebSocket%20reserved%20opcode%20bypasses%20frame%20size%20limits%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-Y9CTVKPP",
  "bug_class": "Denial of Service / Resource Exhaustion",
  "created_at": "2026-04-16T02:39:24+00:00",
  "description": "In Jetty's WebSocket core Parser, checkFrameSize() only enforces maxFrameSize for control or data opcodes, and the else-branch check is disabled when autoFragment is true (the default). Reserved opcodes 0x03-0x07 and 0x0B-0x0F therefore skip both the size check and the auto-fragment clamps in parsePayload(), and execution reaches bufferPool.acquire(payloadLength) at Parser.java:346 with an attacker-controlled 63-bit length truncated to int (up to Integer.MAX_VALUE). ArrayByteBufferPool falls through to a raw ByteBuffer.allocate of ~2 GiB, and the illegal opcode is only rejected afterward in newFrame()/FrameSequence. A single ~15-byte frame header sent after a WebSocket upgrade thus forces a ~2 GiB heap allocation per connection, allowing an unauthenticated remote attacker to drive the JVM to OutOfMemoryError and take down every hosted application.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "jetty-core/jetty-websocket/jetty-websocket-core-common/src/main/java/org/eclipse/jetty/websocket/core/internal/Parser.java:346",
  "project": "jetty/jetty.project",
    "1. Complete a WebSocket handshake against the target Jetty endpoint.",
    "2. Send a frame with FIN=1, opcode=0x03 (reserved), MASK=1, payload-len=127, 8-byte extended length = 0x000000007FFFFFF0, a 4-byte masking key, and at least 1 payload byte.",
    "3. Parser.parsePayload() calls bufferPool.acquire(~2 GiB) before validating the opcode.",
    "4. Repeat over a handful of concurrent connections to exhaust the JVM heap and trigger OutOfMemoryError."
  "technical_details": "OpCode.isControlFrame() and OpCode.isDataFrame() both return false for reserved opcodes, so Parser.checkFrameSize() (lines 265-275) falls into an else branch whose throw is gated by !configuration.isAutoFragment() — with DEFAULT_AUTO_FRAGMENT=true no limit is applied. parsePayload()'s fragment clamps at lines 333/341 require isDataFrame==true and are also skipped, so aggregate = bufferPool.acquire(payloadLength, false) at line 346 runs with attacker-controlled payloadLength before the only opcode validation (OpCode.isKnown() in newFrame(), line 282) executes.",
  "title": "WebSocket reserved opcode bypasses frame size limits",
```
