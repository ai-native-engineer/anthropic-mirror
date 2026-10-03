<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-JS5D1Z2X -->

# ANT-2026-JS5D1Z2X · wolfssl/wolfssl

## buffer-overflow medium

[CVE-2026-5295](https://nvd.nist.gov/vuln/detail/CVE-2026-5295)
[CVE-2026-6678](https://nvd.nist.gov/vuln/detail/CVE-2026-6678)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-JS5D1Z2X: Stack buffer overflow in PKCS#7 OtherRecipientInfo OID copy

In wc\_PKCS7\_DecryptOri(), the 32-byte stack array `oriOID[MAX_OID_SZ]` is populated with `XMEMCPY(oriOID, pkiMsg + *idx, oriOIDSz)`. `oriOIDSz` is obtained from GetASNObjectId(), which bounds it only against the remaining message length, not MAX\_OID\_SZ. An attacker supplying an EnvelopedData whose [4] OtherRecipientInfo contains an OBJECT IDENTIFIER with encoded length >32 overflows the stack with controlled bytes. The path is reachable from the public wc\_PKCS7\_DecodeEnvelopedData()/wc\_PKCS7\_DecodeAuthEnvelopedData() APIs when the application has registered an ORI callback. A secondary word32 underflow of `oriValueSz` at line 11515 compounds the issue.

**Project:** wolfssl/wolfssl
**Location:** `wolfcrypt/src/pkcs7.c:11507`

GetASNObjectId → GetASNHeader → GetLength\_ex only checks `idx + length > maxIdx` (remaining input), and the ASN\_OBJECT\_ID path enforces only a 3-byte minimum — there is no cap at MAX\_OID\_SZ (32). The decoded length is then used directly as the XMEMCPY size into a 32-byte stack local, so any OID TLV with length >32 writes attacker-controlled bytes past the buffer and over saved registers/return address.

1. Craft a CMS EnvelopedData (or AuthEnvelopedData) message containing a RecipientInfo with CHOICE tag [4] (OtherRecipientInfo).
2. Encode the oriType OBJECT IDENTIFIER with a DER length greater than 32 (e.g., 200 bytes of attacker-chosen content).
3. Deliver the message to the victim application, which calls wc\_PKCS7\_DecodeEnvelopedData().
4. Parsing reaches wc\_PKCS7\_DecryptOri(); GetASNObjectId() returns oriOIDSz=200.
5. XMEMCPY writes 200 attacker-controlled bytes into the 32-byte stack array, overwriting saved registers / return address.

## Suggested Fix

Bound `oriOIDSz` against `MAX_OID_SZ` (the destination buffer size) before the XMEMCPY, rejecting or truncating any OID whose encoded length exceeds it; also validate that `(*idx - tmpIdx) <= seqSz` before computing `oriValueSz` to prevent the word32 underflow.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-JS5D1Z2X.

---

**Reference:** ANT-2026-JS5D1Z2X

Triage and disclosure were performed by Calif.

1. 2026-04-02
2. 2026-05-28
3. 2026-05-28
4. 2026-05-28
5. 2026-05-28

6fb8b908f6dd4779d30612aab9dd3e34fc1d4f82a937a110480b5c8ee9bc3e3ffbf38a24be20d73810e6c0fd05385ed4cff98c7fd74d654488dd017e5308a2c9

Committed 2026-05-28 15:10 UTC

Revealed 2026-05-28 18:00 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-JS5D1Z2X%22%2C%22bug_class%22%3A%22Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T14%3A11%3A51%2B00%3A00%22%2C%22description%22%3A%22In%20wc_PKCS7_DecryptOri%28%29%2C%20the%2032-byte%20stack%20array%20%60oriOID%5BMAX_OID_SZ%5D%60%20is%20populated%20with%20%60XMEMCPY%28oriOID%2C%20pkiMsg%20%2B%20%2Aidx%2C%20oriOIDSz%29%60.%20%60oriOIDSz%60%20is%20obtained%20from%20GetASNObjectId%28%29%2C%20which%20bounds%20it%20only%20against%20the%20remaining%20message%20length%2C%20not%20MAX_OID_SZ.%20An%20attacker%20supplying%20an%20EnvelopedData%20whose%20%5B4%5D%20OtherRecipientInfo%20contains%20an%20OBJECT%20IDENTIFIER%20with%20encoded%20length%20%3E32%20overflows%20the%20stack%20with%20controlled%20bytes.%20The%20path%20is%20reachable%20from%20the%20public%20wc_PKCS7_DecodeEnvelopedData%28%29/wc_PKCS7_DecodeAuthEnvelopedData%28%29%20APIs%20when%20the%20application%20has%20registered%20an%20ORI%20callback.%20A%20secondary%20word32%20underflow%20of%20%60oriValueSz%60%20at%20line%2011515%20compounds%20the%20issue.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22wolfcrypt/src/pkcs7.c%3A11507%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL/wolfssl%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20CMS%20EnvelopedData%20%28or%20AuthEnvelopedData%29%20message%20containing%20a%20RecipientInfo%20with%20CHOICE%20tag%20%5B4%5D%20%28OtherRecipientInfo%29.%22%2C%222.%20Encode%20the%20oriType%20OBJECT%20IDENTIFIER%20with%20a%20DER%20length%20greater%20than%2032%20%28e.g.%2C%20200%20bytes%20of%20attacker-chosen%20content%29.%22%2C%223.%20Deliver%20the%20message%20to%20the%20victim%20application%2C%20which%20calls%20wc_PKCS7_DecodeEnvelopedData%28%29.%22%2C%224.%20Parsing%20reaches%20wc_PKCS7_DecryptOri%28%29%3B%20GetASNObjectId%28%29%20returns%20oriOIDSz%3D200.%22%2C%225.%20XMEMCPY%20writes%20200%20attacker-controlled%20bytes%20into%20the%2032-byte%20stack%20array%2C%20overwriting%20saved%20registers%20/%20return%20address.%22%5D%2C%22technical_details%22%3A%22GetASNObjectId%20%E2%86%92%20GetASNHeader%20%E2%86%92%20GetLength_ex%20only%20checks%20%60idx%20%2B%20length%20%3E%20maxIdx%60%20%28remaining%20input%29%2C%20and%20the%20ASN_OBJECT_ID%20path%20enforces%20only%20a%203-byte%20minimum%20%E2%80%94%20there%20is%20no%20cap%20at%20MAX_OID_SZ%20%2832%29.%20The%20decoded%20length%20is%20then%20used%20directly%20as%20the%20XMEMCPY%20size%20into%20a%2032-byte%20stack%20local%2C%20so%20any%20OID%20TLV%20with%20length%20%3E32%20writes%20attacker-controlled%20bytes%20past%20the%20buffer%20and%20over%20saved%20registers/return%20address.%22%2C%22title%22%3A%22Stack%20buffer%20overflow%20in%20PKCS%237%20OtherRecipientInfo%20OID%20copy%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-JS5D1Z2X",
  "bug_class": "Buffer Overflow",
  "created_at": "2026-04-16T14:11:51+00:00",
  "description": "In wc_PKCS7_DecryptOri(), the 32-byte stack array `oriOID[MAX_OID_SZ]` is populated with `XMEMCPY(oriOID, pkiMsg + *idx, oriOIDSz)`. `oriOIDSz` is obtained from GetASNObjectId(), which bounds it only against the remaining message length, not MAX_OID_SZ. An attacker supplying an EnvelopedData whose [4] OtherRecipientInfo contains an OBJECT IDENTIFIER with encoded length >32 overflows the stack with controlled bytes. The path is reachable from the public wc_PKCS7_DecodeEnvelopedData()/wc_PKCS7_DecodeAuthEnvelopedData() APIs when the application has registered an ORI callback. A secondary word32 underflow of `oriValueSz` at line 11515 compounds the issue.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "wolfcrypt/src/pkcs7.c:11507",
  "project": "wolfSSL/wolfssl",
    "1. Craft a CMS EnvelopedData (or AuthEnvelopedData) message containing a RecipientInfo with CHOICE tag [4] (OtherRecipientInfo).",
    "2. Encode the oriType OBJECT IDENTIFIER with a DER length greater than 32 (e.g., 200 bytes of attacker-chosen content).",
    "3. Deliver the message to the victim application, which calls wc_PKCS7_DecodeEnvelopedData().",
    "4. Parsing reaches wc_PKCS7_DecryptOri(); GetASNObjectId() returns oriOIDSz=200.",
    "5. XMEMCPY writes 200 attacker-controlled bytes into the 32-byte stack array, overwriting saved registers / return address."
  "technical_details": "GetASNObjectId → GetASNHeader → GetLength_ex only checks `idx + length > maxIdx` (remaining input), and the ASN_OBJECT_ID path enforces only a 3-byte minimum — there is no cap at MAX_OID_SZ (32). The decoded length is then used directly as the XMEMCPY size into a 32-byte stack local, so any OID TLV with length >32 writes attacker-controlled bytes past the buffer and over saved registers/return address.",
  "title": "Stack buffer overflow in PKCS#7 OtherRecipientInfo OID copy",
```
