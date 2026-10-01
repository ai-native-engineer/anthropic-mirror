<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-7DG11TPA -->

# ANT-2026-7DG11TPA · wolfssl/wolfssl

## other critical

[CVE-2026-5194](https://nvd.nist.gov/vuln/detail/CVE-2026-5194)

Claude critical
Security research firm -
Maintainer critical

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-7DG11TPA: [SECURITY: critical] Universal ECDSA certificate forgery for arbitrary hosts

ConfirmSignature() in wolfcrypt/src/asn.c uses the certificate's attacker-controlled sigOID to pick the hash step and the trusted CA's keyOID to pick the verifier, but never checks that the two agree. Setting sigOID to CTC\_ED25519/CTC\_ED448 makes HashForSignature() a no-op, leaving digestSz at its zero-initialized value, and the ECDSA verifier (selected by keyOID=ECDSAk) accepts a zero-length hash. With e=0 the ECDSA verification equation collapses to a relation involving only r, s, and the CA's public point Q, so the attacker can compute a valid (r,s) for arbitrary tbsCertificate content using only the CA's public key. This lets an attacker forge a leaf certificate that chains to any trusted ECDSA root (e.g., DigiCert Global Root G3) and MITM any wolfSSL TLS client.

**Project:** wolfssl/wolfssl
**Location:** `ConfirmSignature() in wolfcrypt/src/asn.c (HashForSignature at asn.c:15926-15938; verifier dispatch at asn.c:16682; wc_ecc_verify_hash at ecc.c:8578)`

The root cause is a missing cross-check between keyOID and sigOID in ConfirmSignature(): HashForSignature() intentionally skips hashing for EdDSA OIDs (asn.c:15926-15938) and returns success without setting \*digestSz, which remains 0 from the earlier XMEMSET of sigCtx (asn.c:15652). The dispatch at asn.c:16682 then calls wc\_ecc\_verify\_hash with digestSz=0; ecc.c:8578 only upper-bounds hashlen, so e is read as 0 and the verification reduces to x(r·s^-1·Q) == r, which the attacker satisfies by picking k, setting r = x(k·Q) and s = r·k^-1.

1. Extract the target ECDSA CA's public point Q from its certificate.
2. Pick random scalar k; compute P = k·Q; set r = x(P) mod n and s = r·k^-1 mod n.
3. Build an arbitrary tbsCertificate (any CN/SANs, attacker's own leaf key) with issuer = CA and signatureAlgorithm = Ed25519 (or Ed448).
4. Attach the DER-encoded (r,s) as the signature to produce forged.pem.
5. Serve forged.pem from an attacker-controlled TLS endpoint and redirect the victim to it.
6. wolfSSL's ConfirmSignature() hashes nothing (EdDSA sigOID), verifies e=0 under ECDSA against the CA key, and accepts the chain.

## Suggested Fix

Add an algorithm-compatibility check at the top of ConfirmSignature() that rejects (ASN\_SIG\_OID\_E) when keyOID and sigOID families disagree (e.g., keyOID=ECDSAk but sigOID is not a CTC\_\*wECDSA value), and as defense-in-depth reject hashlen == 0 in wc\_ecc\_verify\_hash(). Patch attached; updates test\_wc\_CheckCertSigPubKey's expected error from ASN\_PARSE\_E to ASN\_SIG\_OID\_E.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-7DG11TPA.

---

**Reference:** ANT-2026-7DG11TPA

1. 2026-03-26
2. 2026-03-26
3. 2026-04-07
4. 2026-05-14
5. 2026-06-02

795b824d3a8ae740b46f0ead862b0ea39eba87b6fe127e9eb774ef4e34a17aec032cfd1a1cfeb29958f591e5118f4525adc14699a2e0c6f103f24dc793aa9a99

Committed 2026-03-26 16:21 PT

Revealed 2026-06-02 11:00 PT

The preimage for this commitment is withheld because it references findings that are not yet disclosed. The commitment hash remains in the ledger and the full preimage will be published when the referenced findings are revealed.
