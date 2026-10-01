<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-PQ3CNCCK -->

# ANT-2026-PQ3CNCCK · firecracker-microvm/firecracker

## oob-read high

[CVE-2026-5747](https://nvd.nist.gov/vuln/detail/CVE-2026-5747)
[GHSA-776c-mpj7-jm3r](https://github.com/advisories/GHSA-776c-mpj7-jm3r)

Security research firm -
Maintainer -

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-PQ3CNCCK: Virtio-PCI queue size writable after activation enables host OOB

In Firecracker's virtio-PCI transport, a 2-byte BAR write to offset 0x18 reaches `self.with_queue_mut(queues, |q| q.size = value)` at common\_config.rs:202 with no check on device status, unlike the MMIO transport which gates the same write behind DRIVER\_OK (mmio.rs:130-142). Queue::initialize() validates size and caches raw host pointers (desc\_table\_ptr/avail\_ring\_ptr/used\_ring\_ptr) bounds-checked only for the validated size, but the hot path later indexes those cached pointers using the live `self.size` inside unsafe blocks (queue.rs:392-398, 417-426, 445-456, 541-546, 574-582). A malicious guest can enlarge size to 0xFFFF after DRIVER\_OK, yielding guest-controlled-index 2-byte reads and 2/8-byte writes up to ~512 KiB past the validated guest-memory mapping into host VMM process memory. This is a sliding OOB write primitive usable as a building block for guest-to-host escape, or at minimum reliable host DoS.

**Project:** firecracker-microvm/firecracker
**Location:** `src/vmm/src/devices/virtio/transport/pci/common_config.rs:202`

The PCI common-config write path assigns guest-supplied queue\_size directly (`q.size = value`) without gating on activation/DRIVER\_OK and without re-running Queue::initialize(), so the safety invariants of the cached raw pointers derived at activation time are broken. Subsequent unsafe pointer arithmetic such as `used_ring_ptr.add(size_of::<u16>()*2 + size_of::<UsedElement>()*size)` uses the new, unvalidated size against stale pointers whose backing slice was bounds-checked only for the original size, producing host-process OOB reads and writes. Queue ring addresses (offsets 0x20-0x34) and queue\_enable (0x1c) are similarly ungated.

1. Operator starts Firecracker with --enable-pci and a virtio-pci device (e.g. virtio-net).
2. Guest negotiates the device with minimum queue size and places the used ring at the highest valid guest-physical page so the validated mapping ends at the top of the GuestMemoryMmap region.
3. Guest sets DRIVER\_OK; Queue::initialize() caches used\_ring\_ptr for the validated size.
4. Guest performs a 2-byte write to BAR0 at COMMON\_CONFIG\_BAR\_OFFSET+0x18 with value 0xFFFF, silently overwriting q.size.
5. Guest kicks the queue / manipulates avail idx so the VMM runs used\_ring\_used\_element\_set() and used\_ring\_avail\_event\_set(), whose unsafe .add() offsets now land hundreds of KiB past the guest-memory mmap, writing an 8-byte UsedElement and a 2-byte avail\_event at attacker-influenced offsets; repeat with varying next\_used for a sliding OOB write primitive.

## Suggested Fix

Make queue geometry (size, ring addresses, enable) immutable from the guest once the device is activated / DRIVER\_OK is set; reject post-activation writes or force full queue re-validation and re-derivation of cached raw pointers before they are used again.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-PQ3CNCCK.

---

**Reference:** ANT-2026-PQ3CNCCK

ADVISORY

<https://github.com/firecracker-microvm/firecracker/security/advisories/GHSA-776c-mpj7-jm3r>

1. 2026-03-31
2. 2026-03-31
3. 2026-04-06
4. 2026-04-15

97cd06851823987565a3f40bce0a69f65bdf9fe68e2ab7303ee3b5d58780e4e5a65f21cd44d70f53e4d97898416ddc420f50c71d4bb4164bedef94b9e5f03077

Committed 2026-03-31 17:00 PT

Revealed 2026-08-17 16:50 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-PQ3CNCCK%22%2C%22bug_class%22%3A%22Memory%20Safety%20/%20Out-of-Bounds%20Read%2BWrite%20%28unsafe%20Rust%29%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T02%3A27%3A08%2B00%3A00%22%2C%22description%22%3A%22In%20Firecracker%27s%20virtio-PCI%20transport%2C%20a%202-byte%20BAR%20write%20to%20offset%200x18%20reaches%20%60self.with_queue_mut%28queues%2C%20%7Cq%7C%20q.size%20%3D%20value%29%60%20at%20common_config.rs%3A202%20with%20no%20check%20on%20device%20status%2C%20unlike%20the%20MMIO%20transport%20which%20gates%20the%20same%20write%20behind%20DRIVER_OK%20%28mmio.rs%3A130-142%29.%20Queue%3A%3Ainitialize%28%29%20validates%20size%20and%20caches%20raw%20host%20pointers%20%28desc_table_ptr/avail_ring_ptr/used_ring_ptr%29%20bounds-checked%20only%20for%20the%20validated%20size%2C%20but%20the%20hot%20path%20later%20indexes%20those%20cached%20pointers%20using%20the%20live%20%60self.size%60%20inside%20unsafe%20blocks%20%28queue.rs%3A392-398%2C%20417-426%2C%20445-456%2C%20541-546%2C%20574-582%29.%20A%20malicious%20guest%20can%20enlarge%20size%20to%200xFFFF%20after%20DRIVER_OK%2C%20yielding%20guest-controlled-index%202-byte%20reads%20and%202/8-byte%20writes%20up%20to%20~512%20KiB%20past%20the%20validated%20guest-memory%20mapping%20into%20host%20VMM%20process%20memory.%20This%20is%20a%20sliding%20OOB%20write%20primitive%20usable%20as%20a%20building%20block%20for%20guest-to-host%20escape%2C%20or%20at%20minimum%20reliable%20host%20DoS.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22src/vmm/src/devices/virtio/transport/pci/common_config.rs%3A202%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22firecracker-microvm/firecracker%22%2C%22reproduction%22%3A%5B%221.%20Operator%20starts%20Firecracker%20with%20--enable-pci%20and%20a%20virtio-pci%20device%20%28e.g.%20virtio-net%29.%22%2C%222.%20Guest%20negotiates%20the%20device%20with%20minimum%20queue%20size%20and%20places%20the%20used%20ring%20at%20the%20highest%20valid%20guest-physical%20page%20so%20the%20validated%20mapping%20ends%20at%20the%20top%20of%20the%20GuestMemoryMmap%20region.%22%2C%223.%20Guest%20sets%20DRIVER_OK%3B%20Queue%3A%3Ainitialize%28%29%20caches%20used_ring_ptr%20for%20the%20validated%20size.%22%2C%224.%20Guest%20performs%20a%202-byte%20write%20to%20BAR0%20at%20COMMON_CONFIG_BAR_OFFSET%2B0x18%20with%20value%200xFFFF%2C%20silently%20overwriting%20q.size.%22%2C%225.%20Guest%20kicks%20the%20queue%20/%20manipulates%20avail%20idx%20so%20the%20VMM%20runs%20used_ring_used_element_set%28%29%20and%20used_ring_avail_event_set%28%29%2C%20whose%20unsafe%20.add%28%29%20offsets%20now%20land%20hundreds%20of%20KiB%20past%20the%20guest-memory%20mmap%2C%20writing%20an%208-byte%20UsedElement%20and%20a%202-byte%20avail_event%20at%20attacker-influenced%20offsets%3B%20repeat%20with%20varying%20next_used%20for%20a%20sliding%20OOB%20write%20primitive.%22%5D%2C%22technical_details%22%3A%22The%20PCI%20common-config%20write%20path%20assigns%20guest-supplied%20queue_size%20directly%20%28%60q.size%20%3D%20value%60%29%20without%20gating%20on%20activation/DRIVER_OK%20and%20without%20re-running%20Queue%3A%3Ainitialize%28%29%2C%20so%20the%20safety%20invariants%20of%20the%20cached%20raw%20pointers%20derived%20at%20activation%20time%20are%20broken.%20Subsequent%20unsafe%20pointer%20arithmetic%20such%20as%20%60used_ring_ptr.add%28size_of%3A%3A%3Cu16%3E%28%29%2A2%20%2B%20size_of%3A%3A%3CUsedElement%3E%28%29%2Asize%29%60%20uses%20the%20new%2C%20unvalidated%20size%20against%20stale%20pointers%20whose%20backing%20slice%20was%20bounds-checked%20only%20for%20the%20original%20size%2C%20producing%20host-process%20OOB%20reads%20and%20writes.%20Queue%20ring%20addresses%20%28offsets%200x20-0x34%29%20and%20queue_enable%20%280x1c%29%20are%20similarly%20ungated.%22%2C%22title%22%3A%22Virtio-PCI%20queue%20size%20writable%20after%20activation%20enables%20host%20OOB%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-PQ3CNCCK",
  "bug_class": "Memory Safety / Out-of-Bounds Read+Write (unsafe Rust)",
  "created_at": "2026-04-16T02:27:08+00:00",
  "description": "In Firecracker's virtio-PCI transport, a 2-byte BAR write to offset 0x18 reaches `self.with_queue_mut(queues, |q| q.size = value)` at common_config.rs:202 with no check on device status, unlike the MMIO transport which gates the same write behind DRIVER_OK (mmio.rs:130-142). Queue::initialize() validates size and caches raw host pointers (desc_table_ptr/avail_ring_ptr/used_ring_ptr) bounds-checked only for the validated size, but the hot path later indexes those cached pointers using the live `self.size` inside unsafe blocks (queue.rs:392-398, 417-426, 445-456, 541-546, 574-582). A malicious guest can enlarge size to 0xFFFF after DRIVER_OK, yielding guest-controlled-index 2-byte reads and 2/8-byte writes up to ~512 KiB past the validated guest-memory mapping into host VMM process memory. This is a sliding OOB write primitive usable as a building block for guest-to-host escape, or at minimum reliable host DoS.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "src/vmm/src/devices/virtio/transport/pci/common_config.rs:202",
  "project": "firecracker-microvm/firecracker",
    "1. Operator starts Firecracker with --enable-pci and a virtio-pci device (e.g. virtio-net).",
    "2. Guest negotiates the device with minimum queue size and places the used ring at the highest valid guest-physical page so the validated mapping ends at the top of the GuestMemoryMmap region.",
    "3. Guest sets DRIVER_OK; Queue::initialize() caches used_ring_ptr for the validated size.",
    "4. Guest performs a 2-byte write to BAR0 at COMMON_CONFIG_BAR_OFFSET+0x18 with value 0xFFFF, silently overwriting q.size.",
    "5. Guest kicks the queue / manipulates avail idx so the VMM runs used_ring_used_element_set() and used_ring_avail_event_set(), whose unsafe .add() offsets now land hundreds of KiB past the guest-memory mmap, writing an 8-byte UsedElement and a 2-byte avail_event at attacker-influenced offsets; repeat with varying next_used for a sliding OOB write primitive."
  "technical_details": "The PCI common-config write path assigns guest-supplied queue_size directly (`q.size = value`) without gating on activation/DRIVER_OK and without re-running Queue::initialize(), so the safety invariants of the cached raw pointers derived at activation time are broken. Subsequent unsafe pointer arithmetic such as `used_ring_ptr.add(size_of::<u16>()*2 + size_of::<UsedElement>()*size)` uses the new, unvalidated size against stale pointers whose backing slice was bounds-checked only for the original size, producing host-process OOB reads and writes. Queue ring addresses (offsets 0x20-0x34) and queue_enable (0x1c) are similarly ungated.",
  "title": "Virtio-PCI queue size writable after activation enables host OOB",
  "vendor_severity": null
```
