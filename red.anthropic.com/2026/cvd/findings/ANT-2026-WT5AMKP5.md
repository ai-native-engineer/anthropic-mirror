<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-WT5AMKP5 -->

# ANT-2026-WT5AMKP5 · wireshark/wireshark

## stack-buffer-overflow medium

[CVE-2026-15166](https://nvd.nist.gov/vuln/detail/CVE-2026-15166)
[GHSA-h9wc-3j4p-q5g3](https://github.com/advisories/GHSA-h9wc-3j4p-q5g3)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-WT5AMKP5: 802.11 EAPOL key-data decryption stack buffer overflow

In Wireshark's 802.11 decryption code, Dot11DecryptDecryptKeyData() declares a 1024-byte stack array decrypted\_data[] and, on the RC4 key-wrap path, calls memcpy(decrypted\_data, data, key\_bytes\_len). key\_bytes\_len is bounded only by eapol\_parsed->len - 95, where eapol\_parsed->len is the raw attacker-controlled 16-bit EAPOL length field. The existing DOT11DECRYPT\_EAPOL\_MAX\_LEN checks at dot11decrypt.c:861 and :1618-1620 are on different code paths and do not protect the try\_decrypt\_keydata → Dot11DecryptDecryptKeyData path. An attacker who injects a spoofed EAPOL-Key message 3 with a ~2000–4000 byte Key Data Length (or supplies a malicious pcap) causes ~900+ attacker-influenced bytes to overwrite the stack frame of try\_decrypt\_keydata, yielding a crash on canary-protected builds and potential RCE otherwise.

**Project:** wireshark/wireshark
**Location:** `epan/crypt/dot11decrypt.c:485`

The root cause is a missing bounds check: key\_bytes\_len is derived from the packet's EAPOL Key Data Length / EAPOL length fields and is never compared against sizeof(decrypted\_data) (1024) before the memcpy at dot11decrypt.c:477. The RC4 branch (dot11decrypt.c:458-478) has no integrity check and always returns, so once a valid SA exists the overflowing memcpy is reached unconditionally; the AES-unwrap path uses the same undersized output buffer.

1. Ensure Wireshark has observed/established an SA for the target BSSID/STA (e.g., deauth the client to force a fresh 4-way handshake).
2. Craft an EAPOL-Key message 3 with key\_version=1 (RC4) and a Key Data Length / EAPOL length of ~2000–4000 bytes, padding the body accordingly.
3. Transmit the frame (or embed it in a pcap opened by the analyst).
4. packet-ieee80211.c:43016 calls try\_decrypt\_keydata → Dot11DecryptDecryptKeyData(), which memcpy()s the oversized key data into the 1024-byte stack array, overwriting saved registers/return address.

## Suggested Fix

Before any copy or in-place decrypt, bound key\_bytes\_len by both sizeof(decrypted\_data) and the actual captured key-data length, rejecting frames that exceed the buffer.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-WT5AMKP5.

---

**Reference:** ANT-2026-WT5AMKP5

Triage and disclosure were performed by Ada Logics.

```
diff --git a/epan/crypt/dot11decrypt.c b/epan/crypt/dot11decrypt.c
index 76dbbdd6251..d37c506de38 100644
--- a/epan/crypt/dot11decrypt.c
+++ b/epan/crypt/dot11decrypt.c
@@ -435,6 +435,11 @@ Dot11DecryptDecryptKeyData(PDOT11DECRYPT_CONTEXT ctx,

+    if (key_bytes_len > *decrypted_len) {
+        ws_debug("Too large EAPOL key data");
+        return DOT11DECRYPT_RET_UNSUCCESS;
+    }
+
     if ((key_bytes_len < GROUP_KEY_MIN_LEN) ||
         (eapol_parsed->len < EAPOL_RSN_KEY_LEN) ||
         (key_bytes_len > eapol_parsed->len - EAPOL_RSN_KEY_LEN)) {
diff --git a/epan/dissectors/packet-ieee80211.c b/epan/dissectors/packet-ieee80211.c
index e4145dd240f..a34850d4510 100644
--- a/epan/dissectors/packet-ieee80211.c
+++ b/epan/dissectors/packet-ieee80211.c
@@ -42652,29 +42652,38 @@ keydata_padding_len(tvbuff_t *tvb)
   return 0;

-static void
+static bool
 get_eapol_parsed(packet_info *pinfo, PDOT11DECRYPT_EAPOL_PARSED eapol_parsed)
   if (!eapol_parsed) {
-    return;
+    return false;

   proto_eapol_key_frame_t *eapol_key =
     (proto_eapol_key_frame_t *)p_get_proto_data(pinfo->pool, pinfo, proto_eapol,
                                                 EAPOL_KEY_FRAME_KEY);
   if (!eapol_key) {
-    return;
+    return false;
   eapol_parsed->len = eapol_key->len;
+  if (eapol_parsed->len > DOT11DECRYPT_EAPOL_MAX_LEN) {
+    return false;
+  }
   eapol_parsed->key_type = eapol_key->type;
   eapol_parsed->key_version = (uint8_t)
     GPOINTER_TO_UINT(p_get_proto_data(pinfo->pool, pinfo, proto_wlan, KEY_VERSION_KEY));
   eapol_parsed->key_len = (uint16_t)
     GPOINTER_TO_UINT(p_get_proto_data(pinfo->pool, pinfo, proto_wlan, KEY_LEN_KEY));
+  if (eapol_parsed->key_len > DOT11DECRYPT_EAPOL_MAX_LEN) {
+    return false;
+  }
   eapol_parsed->key_iv = (uint8_t *)p_get_proto_data(pinfo->pool, pinfo, proto_wlan, KEY_IV_KEY);
   eapol_parsed->key_data = (uint8_t *)p_get_proto_data(pinfo->pool, pinfo, proto_wlan, KEY_DATA_KEY);
   eapol_parsed->key_data_len = (uint16_t)
     GPOINTER_TO_UINT(p_get_proto_data(pinfo->pool, pinfo, proto_wlan, KEY_DATA_LEN_KEY));
+  if (eapol_parsed->key_data_len > DOT11DECRYPT_EAPOL_MAX_LEN) {
+    return false;
+  }
   eapol_parsed->nonce = (uint8_t *)p_get_proto_data(pinfo->pool, pinfo, proto_wlan, NONCE_KEY);
   eapol_parsed->group_cipher = (uint8_t)
     GPOINTER_TO_UINT(p_get_proto_data(pinfo->pool, pinfo, proto_wlan, GROUP_CIPHER_KEY));
@@ -42713,6 +42722,7 @@ get_eapol_parsed(packet_info *pinfo, PDOT11DECRYPT_EAPOL_PARSED eapol_parsed)
     (uint8_t *)p_get_proto_data(pinfo->pool, pinfo, proto_wlan, FTE_R1KH_ID_KEY);
   eapol_parsed->fte.r1kh_id_len = (uint8_t)
     GPOINTER_TO_UINT(p_get_proto_data(pinfo->pool, pinfo, proto_wlan, FTE_R1KH_ID_LEN_KEY));
+  return true;

 static void
@@ -42764,7 +42774,7 @@ get_assoc_parsed(packet_info *pinfo, PDOT11DECRYPT_ASSOC_PARSED assoc_parsed)
 static void
 try_decrypt_keydata(packet_info *pinfo)
-  uint32_t dec_caplen;
+  uint32_t dec_caplen = DOT11DECRYPT_EAPOL_MAX_LEN;
   unsigned char dec_data[DOT11DECRYPT_EAPOL_MAX_LEN];
   DOT11DECRYPT_EAPOL_PARSED eapol_parsed;
   DOT11DECRYPT_KEY_ITEM used_key;
@@ -42780,7 +42790,8 @@ try_decrypt_keydata(packet_info *pinfo)

   memset(&eapol_parsed, 0, sizeof(eapol_parsed));
-  get_eapol_parsed(pinfo, &eapol_parsed);
+  if (!get_eapol_parsed(pinfo, &eapol_parsed))
+    return;

   int ret = Dot11DecryptDecryptKeyData(&dot11decrypt_ctx,
                                         &eapol_parsed,
@@ -42818,7 +42829,8 @@ try_scan_eapol_keys(packet_info *pinfo, DOT11DECRYPT_HS_MSG_TYPE msg_type)

   memset(&eapol_parsed, 0, sizeof(eapol_parsed));
-  get_eapol_parsed(pinfo, &eapol_parsed);
+  if (!get_eapol_parsed(pinfo, &eapol_parsed))
+    return;
   eapol_parsed.msg_type = msg_type;

   Dot11DecryptScanEapolForKeys(&dot11decrypt_ctx,
```

<https://github.com/wireshark/wireshark/commit/68a91452afc0a68b37314efa969b9232e1ec6711>

1. 2026-04-02
2. 2026-07-04
3. 2026-07-08
4. 2026-08-12
5. 2026-09-28

c8ad7e4ebd888e9061b505bb8b0d77ea9cb23d23e64056eb0e4e1dc5e43146305563063b81889c7ad80959944285ef4443214c48485b52aa651cba7249c1eee2

Committed 2026-07-22 07:34 UTC

Revealed 2026-09-28 20:34 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-WT5AMKP5%22%2C%22bug_class%22%3A%22Stack%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T14%3A11%3A10%2B00%3A00%22%2C%22description%22%3A%22In%20Wireshark%27s%20802.11%20decryption%20code%2C%20Dot11DecryptDecryptKeyData%28%29%20declares%20a%201024-byte%20stack%20array%20decrypted_data%5B%5D%20and%2C%20on%20the%20RC4%20key-wrap%20path%2C%20calls%20memcpy%28decrypted_data%2C%20data%2C%20key_bytes_len%29.%20key_bytes_len%20is%20bounded%20only%20by%20eapol_parsed-%3Elen%20-%2095%2C%20where%20eapol_parsed-%3Elen%20is%20the%20raw%20attacker-controlled%2016-bit%20EAPOL%20length%20field.%20The%20existing%20DOT11DECRYPT_EAPOL_MAX_LEN%20checks%20at%20dot11decrypt.c%3A861%20and%20%3A1618-1620%20are%20on%20different%20code%20paths%20and%20do%20not%20protect%20the%20try_decrypt_keydata%20%E2%86%92%20Dot11DecryptDecryptKeyData%20path.%20An%20attacker%20who%20injects%20a%20spoofed%20EAPOL-Key%20message%203%20with%20a%20~2000%E2%80%934000%20byte%20Key%20Data%20Length%20%28or%20supplies%20a%20malicious%20pcap%29%20causes%20~900%2B%20attacker-influenced%20bytes%20to%20overwrite%20the%20stack%20frame%20of%20try_decrypt_keydata%2C%20yielding%20a%20crash%20on%20canary-protected%20builds%20and%20potential%20RCE%20otherwise.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22epan/crypt/dot11decrypt.c%3A485%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wireshark/wireshark%22%2C%22reproduction%22%3A%5B%221.%20Ensure%20Wireshark%20has%20observed/established%20an%20SA%20for%20the%20target%20BSSID/STA%20%28e.g.%2C%20deauth%20the%20client%20to%20force%20a%20fresh%204-way%20handshake%29.%22%2C%222.%20Craft%20an%20EAPOL-Key%20message%203%20with%20key_version%3D1%20%28RC4%29%20and%20a%20Key%20Data%20Length%20/%20EAPOL%20length%20of%20~2000%E2%80%934000%20bytes%2C%20padding%20the%20body%20accordingly.%22%2C%223.%20Transmit%20the%20frame%20%28or%20embed%20it%20in%20a%20pcap%20opened%20by%20the%20analyst%29.%22%2C%224.%20packet-ieee80211.c%3A43016%20calls%20try_decrypt_keydata%20%E2%86%92%20Dot11DecryptDecryptKeyData%28%29%2C%20which%20memcpy%28%29s%20the%20oversized%20key%20data%20into%20the%201024-byte%20stack%20array%2C%20overwriting%20saved%20registers/return%20address.%22%5D%2C%22technical_details%22%3A%22The%20root%20cause%20is%20a%20missing%20bounds%20check%3A%20key_bytes_len%20is%20derived%20from%20the%20packet%27s%20EAPOL%20Key%20Data%20Length%20/%20EAPOL%20length%20fields%20and%20is%20never%20compared%20against%20sizeof%28decrypted_data%29%20%281024%29%20before%20the%20memcpy%20at%20dot11decrypt.c%3A477.%20The%20RC4%20branch%20%28dot11decrypt.c%3A458-478%29%20has%20no%20integrity%20check%20and%20always%20returns%2C%20so%20once%20a%20valid%20SA%20exists%20the%20overflowing%20memcpy%20is%20reached%20unconditionally%3B%20the%20AES-unwrap%20path%20uses%20the%20same%20undersized%20output%20buffer.%22%2C%22title%22%3A%22802.11%20EAPOL%20key-data%20decryption%20stack%20buffer%20overflow%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-WT5AMKP5",
  "bug_class": "Stack Buffer Overflow",
  "created_at": "2026-04-16T14:11:10+00:00",
  "description": "In Wireshark's 802.11 decryption code, Dot11DecryptDecryptKeyData() declares a 1024-byte stack array decrypted_data[] and, on the RC4 key-wrap path, calls memcpy(decrypted_data, data, key_bytes_len). key_bytes_len is bounded only by eapol_parsed->len - 95, where eapol_parsed->len is the raw attacker-controlled 16-bit EAPOL length field. The existing DOT11DECRYPT_EAPOL_MAX_LEN checks at dot11decrypt.c:861 and :1618-1620 are on different code paths and do not protect the try_decrypt_keydata → Dot11DecryptDecryptKeyData path. An attacker who injects a spoofed EAPOL-Key message 3 with a ~2000–4000 byte Key Data Length (or supplies a malicious pcap) causes ~900+ attacker-influenced bytes to overwrite the stack frame of try_decrypt_keydata, yielding a crash on canary-protected builds and potential RCE otherwise.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "epan/crypt/dot11decrypt.c:485",
  "project": "wireshark/wireshark",
    "1. Ensure Wireshark has observed/established an SA for the target BSSID/STA (e.g., deauth the client to force a fresh 4-way handshake).",
    "2. Craft an EAPOL-Key message 3 with key_version=1 (RC4) and a Key Data Length / EAPOL length of ~2000–4000 bytes, padding the body accordingly.",
    "3. Transmit the frame (or embed it in a pcap opened by the analyst).",
    "4. packet-ieee80211.c:43016 calls try_decrypt_keydata → Dot11DecryptDecryptKeyData(), which memcpy()s the oversized key data into the 1024-byte stack array, overwriting saved registers/return address."
  "technical_details": "The root cause is a missing bounds check: key_bytes_len is derived from the packet's EAPOL Key Data Length / EAPOL length fields and is never compared against sizeof(decrypted_data) (1024) before the memcpy at dot11decrypt.c:477. The RC4 branch (dot11decrypt.c:458-478) has no integrity check and always returns, so once a valid SA exists the overflowing memcpy is reached unconditionally; the AES-unwrap path uses the same undersized output buffer.",
  "title": "802.11 EAPOL key-data decryption stack buffer overflow",
```
