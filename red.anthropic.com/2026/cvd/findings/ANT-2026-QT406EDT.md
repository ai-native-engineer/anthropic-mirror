<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-QT406EDT -->

# ANT-2026-QT406EDT · libreoffice/core

## other medium

[CVE-2026-63274](https://nvd.nist.gov/vuln/detail/CVE-2026-63274)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-QT406EDT: Heap overflow from unclamped /Length in hybrid-PDF stream extraction

In sdext/source/pdfimport/pdfparse/pdfentries.cxx, PDFObject::getDeflatedStream() allocates a heap buffer of nOuterStreamLen bytes (the lexically-measured distance between the 'stream' and 'endstream' tokens) but then sets the copy length to the raw dictionary /Length value via getDictLength() with no validation. The subsequent memmove at line 692 reads and writes that many bytes into the smaller allocation. This code path is reached from PDFDetector::detect() during default file-type detection whenever a PDF's trailer advertises /AdditionalStreams and a matching /DocChecksum — both of which the attacker authors and can trivially forge. An attacker who convinces a victim to open a crafted PDF therefore controls both the allocation size and the independent, larger copy length, yielding a heap OOB read+write that corrupts adjacent heap memory and is plausibly exploitable for code execution.

**Project:** libreoffice/core
**Location:** `sdext/source/pdfimport/pdfparse/pdfentries.cxx:692`

The root cause is a missing bounds clamp: nOuterStreamLen (m\_nEndOffset - m\_nBeginOffset) is determined purely lexically by the boost::spirit grammar scanning for 'stream'/'endstream', while *pBytes is set from getDictLength(), which returns the raw numeric /Length from the object dictionary unchecked. Because these two values are independent and attacker-controlled, memmove(rpStream.get(), pStream,* pBytes) at line 692 can copy far more bytes than were allocated at line 653, producing a classic heap buffer overflow (both OOB read from and OOB write to adjacent heap memory).

1. Author a PDF containing an object whose physical 'stream'...'endstream' body is small (e.g., 32 bytes) but whose dictionary declares a huge /Length (e.g., 1000000).
2. Add a trailer with /AdditionalStreams referencing that object and a /DocChecksum equal to the MD5 of the file prefix (attacker computes this); omit new-style embedded files so getEmbeddedFile() fails and control falls through to getAdditionalStream().
3. Deliver the PDF to the victim and have them open it in LibreOffice.
4. PDFDetector::detect() → getAdditionalStream() → PDFObject::writeStream() → getDeflatedStream() allocates nOuterStreamLen bytes then memmoves /Length bytes, overflowing the heap.

## Suggested Fix

Clamp the number of bytes copied and subsequently processed to the actual allocated buffer size (nOuterStreamLen) rather than trusting the file-declared /Length; reject or truncate streams whose /Length exceeds the lexical stream span.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-QT406EDT.

---

**Reference:** ANT-2026-QT406EDT

Triage and disclosure were performed by Ada Logics.

```
diff --git a/sdext/source/pdfimport/pdfparse/pdfentries.cxx b/sdext/source/pdfimport/pdfparse/pdfentries.cxx
index d000a18dcea33..3ec950e22b755 100644
--- a/sdext/source/pdfimport/pdfparse/pdfentries.cxx
+++ b/sdext/source/pdfimport/pdfparse/pdfentries.cxx
@@ -688,6 +688,12 @@ bool PDFObject::getDeflatedStream( std::unique_ptr<char[]>& rpStream, unsigned i
             pStream++;
         // get the compressed length
         *pBytes = m_pStream->getDictLength( pObjectContainer );
+        unsigned int nAvailable = nOuterStreamLen - static_cast<unsigned int>(pStream - rpStream.get());
+        if (*pBytes > nAvailable)
+        {
+            SAL_WARN("sdext.pdfimport.pdfparse", "stream /Length " << *pBytes << " exceeds " << nAvailable << " available bytes");
+            *pBytes = nAvailable;
+        }
         if( pStream != rpStream.get() )
             memmove( rpStream.get(), pStream, *pBytes );
         if( rContext.m_bDecrypt )
```

<https://github.com/LibreOffice/core/commit/dcf16d610a32861349d4e4b84e7bef4b9420929c>

1. 2026-04-02
2. 2026-07-04
3. 2026-07-24
4. 2026-08-12
5. 2026-09-28

a546a862caaa6a6280b9ca7f696d78567d009cca5ef139a0b61306b5bdbdb7c494c58aac26ce4f0314b03512abf5ee240d50af1f8905096abda281f03e6e163e

Committed 2026-07-22 07:32 UTC

Revealed 2026-09-28 20:49 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-QT406EDT%22%2C%22bug_class%22%3A%22Memory%20corruption%20%28heap%20buffer%20overflow%29%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A54%3A44%2B00%3A00%22%2C%22description%22%3A%22In%20sdext/source/pdfimport/pdfparse/pdfentries.cxx%2C%20PDFObject%3A%3AgetDeflatedStream%28%29%20allocates%20a%20heap%20buffer%20of%20nOuterStreamLen%20bytes%20%28the%20lexically-measured%20distance%20between%20the%20%27stream%27%20and%20%27endstream%27%20tokens%29%20but%20then%20sets%20the%20copy%20length%20to%20the%20raw%20dictionary%20/Length%20value%20via%20getDictLength%28%29%20with%20no%20validation.%20The%20subsequent%20memmove%20at%20line%20692%20reads%20and%20writes%20that%20many%20bytes%20into%20the%20smaller%20allocation.%20This%20code%20path%20is%20reached%20from%20PDFDetector%3A%3Adetect%28%29%20during%20default%20file-type%20detection%20whenever%20a%20PDF%27s%20trailer%20advertises%20/AdditionalStreams%20and%20a%20matching%20/DocChecksum%20%E2%80%94%20both%20of%20which%20the%20attacker%20authors%20and%20can%20trivially%20forge.%20An%20attacker%20who%20convinces%20a%20victim%20to%20open%20a%20crafted%20PDF%20therefore%20controls%20both%20the%20allocation%20size%20and%20the%20independent%2C%20larger%20copy%20length%2C%20yielding%20a%20heap%20OOB%20read%2Bwrite%20that%20corrupts%20adjacent%20heap%20memory%20and%20is%20plausibly%20exploitable%20for%20code%20execution.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22sdext/source/pdfimport/pdfparse/pdfentries.cxx%3A692%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22LibreOffice/core%22%2C%22reproduction%22%3A%5B%221.%20Author%20a%20PDF%20containing%20an%20object%20whose%20physical%20%27stream%27...%27endstream%27%20body%20is%20small%20%28e.g.%2C%2032%20bytes%29%20but%20whose%20dictionary%20declares%20a%20huge%20/Length%20%28e.g.%2C%201000000%29.%22%2C%222.%20Add%20a%20trailer%20with%20/AdditionalStreams%20referencing%20that%20object%20and%20a%20/DocChecksum%20equal%20to%20the%20MD5%20of%20the%20file%20prefix%20%28attacker%20computes%20this%29%3B%20omit%20new-style%20embedded%20files%20so%20getEmbeddedFile%28%29%20fails%20and%20control%20falls%20through%20to%20getAdditionalStream%28%29.%22%2C%223.%20Deliver%20the%20PDF%20to%20the%20victim%20and%20have%20them%20open%20it%20in%20LibreOffice.%22%2C%224.%20PDFDetector%3A%3Adetect%28%29%20%E2%86%92%20getAdditionalStream%28%29%20%E2%86%92%20PDFObject%3A%3AwriteStream%28%29%20%E2%86%92%20getDeflatedStream%28%29%20allocates%20nOuterStreamLen%20bytes%20then%20memmoves%20/Length%20bytes%2C%20overflowing%20the%20heap.%22%5D%2C%22technical_details%22%3A%22The%20root%20cause%20is%20a%20missing%20bounds%20clamp%3A%20nOuterStreamLen%20%28m_nEndOffset%20-%20m_nBeginOffset%29%20is%20determined%20purely%20lexically%20by%20the%20boost%3A%3Aspirit%20grammar%20scanning%20for%20%27stream%27/%27endstream%27%2C%20while%20%2ApBytes%20is%20set%20from%20getDictLength%28%29%2C%20which%20returns%20the%20raw%20numeric%20/Length%20from%20the%20object%20dictionary%20unchecked.%20Because%20these%20two%20values%20are%20independent%20and%20attacker-controlled%2C%20memmove%28rpStream.get%28%29%2C%20pStream%2C%20%2ApBytes%29%20at%20line%20692%20can%20copy%20far%20more%20bytes%20than%20were%20allocated%20at%20line%20653%2C%20producing%20a%20classic%20heap%20buffer%20overflow%20%28both%20OOB%20read%20from%20and%20OOB%20write%20to%20adjacent%20heap%20memory%29.%22%2C%22title%22%3A%22Heap%20overflow%20from%20unclamped%20/Length%20in%20hybrid-PDF%20stream%20extraction%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-QT406EDT",
  "bug_class": "Memory corruption (heap buffer overflow)",
  "created_at": "2026-04-16T01:54:44+00:00",
  "description": "In sdext/source/pdfimport/pdfparse/pdfentries.cxx, PDFObject::getDeflatedStream() allocates a heap buffer of nOuterStreamLen bytes (the lexically-measured distance between the 'stream' and 'endstream' tokens) but then sets the copy length to the raw dictionary /Length value via getDictLength() with no validation. The subsequent memmove at line 692 reads and writes that many bytes into the smaller allocation. This code path is reached from PDFDetector::detect() during default file-type detection whenever a PDF's trailer advertises /AdditionalStreams and a matching /DocChecksum — both of which the attacker authors and can trivially forge. An attacker who convinces a victim to open a crafted PDF therefore controls both the allocation size and the independent, larger copy length, yielding a heap OOB read+write that corrupts adjacent heap memory and is plausibly exploitable for code execution.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "sdext/source/pdfimport/pdfparse/pdfentries.cxx:692",
  "project": "LibreOffice/core",
    "1. Author a PDF containing an object whose physical 'stream'...'endstream' body is small (e.g., 32 bytes) but whose dictionary declares a huge /Length (e.g., 1000000).",
    "2. Add a trailer with /AdditionalStreams referencing that object and a /DocChecksum equal to the MD5 of the file prefix (attacker computes this); omit new-style embedded files so getEmbeddedFile() fails and control falls through to getAdditionalStream().",
    "3. Deliver the PDF to the victim and have them open it in LibreOffice.",
    "4. PDFDetector::detect() → getAdditionalStream() → PDFObject::writeStream() → getDeflatedStream() allocates nOuterStreamLen bytes then memmoves /Length bytes, overflowing the heap."
  "technical_details": "The root cause is a missing bounds clamp: nOuterStreamLen (m_nEndOffset - m_nBeginOffset) is determined purely lexically by the boost::spirit grammar scanning for 'stream'/'endstream', while *pBytes is set from getDictLength(), which returns the raw numeric /Length from the object dictionary unchecked. Because these two values are independent and attacker-controlled, memmove(rpStream.get(), pStream, *pBytes) at line 692 can copy far more bytes than were allocated at line 653, producing a classic heap buffer overflow (both OOB read from and OOB write to adjacent heap memory).",
  "title": "Heap overflow from unclamped /Length in hybrid-PDF stream extraction",
```
