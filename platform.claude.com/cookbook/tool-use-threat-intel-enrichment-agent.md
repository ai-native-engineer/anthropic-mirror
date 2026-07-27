<!-- source: https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent -->

# Threat Intelligence Enrichment Agent

Security analysts spend hours manually pivoting across threat intelligence sources — querying VirusTotal for a file hash, checking AbuseIPDB for an IP, cross-referencing MITRE ATT&CK, then synthesizing it all into a report. This cookbook shows how to build a Claude-powered agent that automates that entire workflow.

The agent takes raw Indicators of Compromise (IOCs) — IP addresses, file hashes, or domains — and uses Claude's tool-use capabilities to decide which intelligence sources to query, correlate findings across sources, and produce structured, analyst-ready threat reports. The tools in this example are simulated, but the architecture is designed so you can swap in real APIs (VirusTotal, AbuseIPDB, Shodan, etc.) without changing the orchestration logic.

This pattern is directly applicable whether you're building threat intelligence features into a security product (ISVs) or automating enrichment workflows for an enterprise SOC.

## What you'll learn

* How to design tool schemas that give Claude enough context to choose the right intelligence source
* How to build an agentic loop that lets Claude chain tool calls based on what it discovers
* How to prompt for multi-source correlation and MITRE ATT&CK mapping
* How to convert free-text analysis into structured JSON reports for downstream systems

## Prerequisites

* Python 3.10+
* An Anthropic API key — set it in a `.env` file as `ANTHROPIC_API_KEY=sk-ant-...`
* Familiarity with [Claude's tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) is helpful but not required

## Step 1: Set up the environment

Install the Anthropic SDK and `python-dotenv`. Create a `.env` file in the same directory as this notebook with your API key:

```
ANTHROPIC_API_KEY=sk-ant-...
```

python

```
%pip install anthropic python-dotenv --quiet
```

```
Note: you may need to restart the kernel to use updated packages.
```

python

```
import json

import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL_NAME = "claude-sonnet-4-6"
```

## Step 2: Define threat intelligence tools

We define four tools that represent common threat intelligence data sources. Each tool has a clear description that helps Claude understand when and why to use it — this is critical for effective agentic behavior. In production, these would wrap real API calls; the schemas stay the same.

python

```
# Define tools for threat intelligence gathering
tools = [
    {
        "name": "lookup_ip_reputation",
        "description": "Query IP reputation database to get geolocation, ISP information, abuse history, open ports, and known malicious associations for an IP address. Returns threat types, malware associations, and abuse confidence scoring.",
        "input_schema": {
            "type": "object",
            "properties": {
                "ip_address": {
                    "type": "string",
                    "description": "The IPv4 or IPv6 address to investigate.",
                }
            },
            "required": ["ip_address"],
        },
    },
    {
        "name": "lookup_file_hash",
        "description": "Query file reputation service with a cryptographic hash. Returns detection ratio across antivirus engines, malware family classification, behavioral summary, contacted infrastructure, and temporal indicators (first/last seen).",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_hash": {
                    "type": "string",
                    "description": "The MD5, SHA1, or SHA256 hash of the suspicious file.",
                },
                "hash_type": {
                    "type": "string",
                    "enum": ["md5", "sha1", "sha256"],
                    "description": "The type of hash provided.",
                },
            },
            "required": ["file_hash", "hash_type"],
        },
    },
    {
        "name": "lookup_domain",
        "description": "Investigate a domain's reputation including registration details, DNS records, SSL certificate information, hosting provider, and threat categorization. Useful for analyzing phishing domains, malware distribution sites, and C2 infrastructure.",
        "input_schema": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "The domain name to investigate (e.g., example.com).",
                }
            },
            "required": ["domain"],
        },
    },
    {
        "name": "get_mitre_techniques",
        "description": "Map observed behaviors, malware families, or attack patterns to the MITRE ATT&CK framework. Returns matching technique IDs, tactic categories, associated threat groups, and detection recommendations.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Description of the behavior, malware family, or attack pattern to map (e.g., 'command and control beaconing', 'credential theft', 'lateral movement').",
                }
            },
            "required": ["query"],
        },
    },
]

print(f"Defined {len(tools)} threat intelligence tools:")
for tool in tools:
    print(f"  - {tool['name']}: {tool['description'][:80]}...")
```

```
Defined 4 threat intelligence tools:
  - lookup_ip_reputation: Query IP reputation database to get geolocation, ISP information, abuse history,...
  - lookup_file_hash: Query file reputation service with a cryptographic hash. Returns detection ratio...
  - lookup_domain: Investigate a domain's reputation including registration details, DNS records, S...
  - get_mitre_techniques: Map observed behaviors, malware families, or attack patterns to the MITRE ATT&CK...
```

## Step 3: Build simulated threat intel backends

These functions simulate real threat intelligence APIs. Each returns realistic data structures that mirror what you'd get from services like VirusTotal, AbuseIPDB, or a MITRE ATT&CK lookup. To go to production, replace the body of each function with an API call — the interface stays the same.

python

```
# Simulated threat intelligence data sources
# In production, replace each function body with real API calls:
#   lookup_ip_reputation  -> AbuseIPDB, GreyNoise, Shodan
#   lookup_file_hash      -> VirusTotal, MalwareBazaar, Hybrid Analysis
#   lookup_domain         -> URLhaus, DomainTools, WHOIS
#   get_mitre_techniques  -> MITRE ATT&CK STIX/TAXII feed

def lookup_ip_reputation(ip_address: str) -> dict:
    """Query IP reputation. In production: AbuseIPDB, GreyNoise, or Shodan API."""
    ip_database = {
        "203.0.113.42": {
            "ip": "203.0.113.42",
            "country": "Russia",
            "city": "Saint Petersburg",
            "asn": "AS48666",
            "isp": "MnogoByte LLC",
            "abuse_confidence_score": 87,
            "total_reports": 1243,
            "last_reported": "2026-03-10T14:22:00Z",
            "threat_types": ["botnet_c2", "malware_distribution", "brute_force"],
            "known_malware_associations": ["Emotet", "Trickbot"],
            "open_ports": [443, 8080, 4444],
            "is_tor_exit_node": False,
            "is_known_proxy": True,
            "first_seen": "2025-08-15T00:00:00Z",
            "tags": ["banking-trojan-c2", "spam-source"],
        },
        "198.51.100.17": {
            "ip": "198.51.100.17",
            "country": "China",
            "city": "Shanghai",
            "asn": "AS4134",
            "isp": "ChinaNet",
            "abuse_confidence_score": 94,
            "total_reports": 3891,
            "last_reported": "2026-03-12T09:15:00Z",
            "threat_types": ["apt_c2", "data_exfiltration", "scanning"],
            "known_malware_associations": ["PlugX", "ShadowPad"],
            "open_ports": [443, 8443, 53],
            "is_tor_exit_node": False,
            "is_known_proxy": False,
            "first_seen": "2024-11-02T00:00:00Z",
            "tags": ["apt-infrastructure", "state-sponsored"],
        },
    }
    return ip_database.get(
        ip_address,
        {
            "ip": ip_address,
            "country": "Unknown",
            "abuse_confidence_score": 0,
            "total_reports": 0,
            "threat_types": [],
            "note": "No records found for this IP",
        },
    )

def lookup_file_hash(file_hash: str, hash_type: str) -> dict:
    """Query file reputation. In production: VirusTotal or MalwareBazaar API."""
    hash_database = {
        "d131dd02c5e6eec4693d9a0698aff95c": {
            "hash": "d131dd02c5e6eec4693d9a0698aff95c",
            "hash_type": "md5",
            "sha256": "a1b2c3d4e5f6789012345678abcdef0123456789abcdef0123456789abcdef01",
            "detections": 58,
            "total_engines": 72,
            "detection_rate": "80.6%",
            "malware_family": "Emotet",
            "malware_type": "banking_trojan",
            "severity": "critical",
            "file_type": "PE32 executable (DLL)",
            "file_size_bytes": 237568,
            "file_name": "update_service.dll",
            "first_seen": "2025-12-01T08:30:00Z",
            "last_seen": "2026-03-09T22:14:00Z",
            "ssdeep": "6144:Kl2a8JG1oPRqMDFlOGnA8g0ZFBFSqBKiDEF:Kl2a8Q1oPRDF3",
            "tags": ["emotet", "epoch5", "banking-trojan", "dropper"],
            "behavior_summary": "Drops secondary payload via regsvr32, establishes persistence via scheduled task, communicates with C2 over HTTPS on non-standard ports",
            "contacted_ips": ["203.0.113.42", "203.0.113.88", "192.0.2.101"],
            "contacted_domains": ["update-service-cdn.ru", "cdn-api-gateway.cc"],
        },
        "7b3a0c8f2e1d4a5b6c9d8e7f0a1b2c3d": {
            "hash": "7b3a0c8f2e1d4a5b6c9d8e7f0a1b2c3d",
            "hash_type": "md5",
            "sha256": "f0e1d2c3b4a5968778695a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d",
            "detections": 47,
            "total_engines": 70,
            "detection_rate": "67.1%",
            "malware_family": "Trickbot",
            "malware_type": "modular_trojan",
            "severity": "critical",
            "file_type": "PE32 executable (EXE)",
            "file_size_bytes": 524288,
            "file_name": "windefupdate.exe",
            "first_seen": "2025-10-18T12:00:00Z",
            "last_seen": "2026-03-11T06:45:00Z",
            "tags": ["trickbot", "gtag-mor84", "credential-stealer", "lateral-movement"],
            "behavior_summary": "Injects into svchost.exe, harvests browser credentials, performs network reconnaissance, attempts lateral movement via EternalBlue",
            "contacted_ips": ["198.51.100.17", "198.51.100.22"],
            "contacted_domains": ["api-check-update.cc", "telemetry-cdn.ru"],
        },
    }
    return hash_database.get(
        file_hash,
        {
            "hash": file_hash,
            "hash_type": hash_type,
            "detections": 0,
            "total_engines": 72,
            "malware_family": "Unknown",
            "severity": "unknown",
            "note": "No records found for this hash",
        },
    )

def lookup_domain(domain: str) -> dict:
    """Query domain reputation. In production: URLhaus, DomainTools, or WHOIS API."""
    domain_database = {
        "secure-bankofamerica-login.com": {
            "domain": "secure-bankofamerica-login.com",
            "reputation_score": 98,
            "category": "phishing",
            "subcategory": "credential_harvesting",
            "active": True,
            "registrar": "NameSilo LLC",
            "registration_date": "2026-02-28T00:00:00Z",
            "registrant_country": "Panama",
            "hosting_provider": "BulletProof Hosting Ltd",
            "hosting_country": "Moldova",
            "ip_addresses": ["192.0.2.55", "192.0.2.56"],
            "mx_records": [],
            "ssl_issuer": "Let's Encrypt",
            "ssl_valid_from": "2026-02-28T00:00:00Z",
            "targeted_brand": "Bank of America",
            "similar_domains_found": 12,
            "urlhaus_reference": "https://urlhaus.abuse.ch/url/2345678/",
            "tags": ["phishing-kit", "credential-harvest", "typosquat"],
            "associated_ips_with_other_malicious_domains": True,
            "dns_records": {
                "A": ["192.0.2.55"],
                "NS": ["ns1.bulletproof-dns.cc", "ns2.bulletproof-dns.cc"],
                "TXT": [],
            },
        },
        "update-service-cdn.ru": {
            "domain": "update-service-cdn.ru",
            "reputation_score": 91,
            "category": "malware",
            "subcategory": "c2_server",
            "active": True,
            "registrar": "REG.RU LLC",
            "registration_date": "2025-07-14T00:00:00Z",
            "registrant_country": "Russia",
            "hosting_provider": "MnogoByte LLC",
            "hosting_country": "Russia",
            "ip_addresses": ["203.0.113.42"],
            "ssl_issuer": "Self-signed",
            "tags": ["emotet-c2", "malware-distribution", "fast-flux"],
            "associated_malware": ["Emotet", "Trickbot"],
            "dns_records": {
                "A": ["203.0.113.42", "203.0.113.88"],
                "NS": ["ns1.reg.ru", "ns2.reg.ru"],
                "TXT": [],
            },
        },
    }
    return domain_database.get(
        domain,
        {
            "domain": domain,
            "reputation_score": 0,
            "category": "unknown",
            "active": None,
            "note": "No records found for this domain",
        },
    )

def get_mitre_techniques(query: str) -> dict:
    """Map behaviors to MITRE ATT&CK. In production: query ATT&CK STIX/TAXII feed or local DB."""
    mitre_mappings = {
        "command and control": {
            "techniques": [
                {
                    "id": "T1071.001",
                    "name": "Web Protocols",
                    "tactic": "Command and Control",
                    "description": "Adversaries communicate using application layer protocols associated with web traffic to avoid detection",
                },
                {
                    "id": "T1573.002",
                    "name": "Asymmetric Cryptography",
                    "tactic": "Command and Control",
                    "description": "Use asymmetric encryption for C2 communications",
                },
                {
                    "id": "T1008",
                    "name": "Fallback Channels",
                    "tactic": "Command and Control",
                    "description": "Use alternate communication channels if primary C2 is disrupted",
                },
            ],
            "associated_groups": ["APT28", "APT29", "Lazarus Group", "Wizard Spider"],
            "detection_suggestions": [
                "Monitor for unusual outbound HTTPS to non-standard ports",
                "Inspect TLS certificates for self-signed or recently issued certs",
                "Track beaconing patterns in network flow data",
            ],
        },
        "credential theft": {
            "techniques": [
                {
                    "id": "T1056.001",
                    "name": "Keylogging",
                    "tactic": "Collection",
                    "description": "Log keystrokes to intercept credentials as they are typed",
                },
                {
                    "id": "T1555.003",
                    "name": "Credentials from Web Browsers",
                    "tactic": "Credential Access",
                    "description": "Acquire credentials from web browser credential stores",
                },
                {
                    "id": "T1003.001",
                    "name": "LSASS Memory",
                    "tactic": "Credential Access",
                    "description": "Access credential material stored in LSASS process memory",
                },
            ],
            "associated_groups": ["Trickbot operators", "Emotet operators", "FIN7"],
            "detection_suggestions": [
                "Monitor for LSASS access by unusual processes",
                "Alert on credential store file access",
                "Deploy credential guard on endpoints",
            ],
        },
        "phishing": {
            "techniques": [
                {
                    "id": "T1566.001",
                    "name": "Spearphishing Attachment",
                    "tactic": "Initial Access",
                    "description": "Send emails with a malicious attachment to gain access",
                },
                {
                    "id": "T1566.002",
                    "name": "Spearphishing Link",
                    "tactic": "Initial Access",
                    "description": "Send emails with malicious links to credential-harvesting sites",
                },
                {
                    "id": "T1598.003",
                    "name": "Spearphishing Link (for Information)",
                    "tactic": "Reconnaissance",
                    "description": "Send spearphishing links to gather information for targeting",
                },
            ],
            "associated_groups": ["APT28", "Lazarus Group", "Kimsuky", "TA505"],
            "detection_suggestions": [
                "Implement DMARC/DKIM/SPF for email authentication",
                "Deploy URL rewriting and sandboxing for links",
                "Monitor for newly registered look-alike domains",
            ],
        },
        "lateral movement": {
            "techniques": [
                {
                    "id": "T1210",
                    "name": "Exploitation of Remote Services",
                    "tactic": "Lateral Movement",
                    "description": "Exploit remote services to move laterally within the environment",
                },
                {
                    "id": "T1021.002",
                    "name": "SMB/Windows Admin Shares",
                    "tactic": "Lateral Movement",
                    "description": "Use valid accounts to interact with remote network shares using SMB",
                },
            ],
            "associated_groups": ["Wizard Spider", "FIN6", "Sandworm Team"],
            "detection_suggestions": [
                "Monitor for anomalous SMB traffic patterns",
                "Alert on use of PsExec or similar tools",
                "Track authentication events across endpoints",
            ],
        },
    }
    query_lower = query.lower()
    for key, mapping in mitre_mappings.items():
        if key in query_lower:
            return mapping
    # Fuzzy fallback: check if any keyword appears
    for key, mapping in mitre_mappings.items():
        for word in key.split():
            if word in query_lower:
                return mapping
    return {
        "techniques": [],
        "associated_groups": [],
        "note": "No direct MITRE ATT&CK mapping found for this query. Try broader terms like 'command and control', 'credential theft', 'phishing', or 'lateral movement'.",
    }

print(
    "Simulated threat intel backends ready. In production, replace function bodies with real API calls."
)
```

```
Simulated threat intel backends ready. In production, replace function bodies with real API calls.
```

## Step 4: Create the agent loop

This is the core orchestration. We give Claude a system prompt that positions it as a senior threat intelligence analyst, then let it decide which tools to call and in what order. The `while` loop continues as long as Claude wants to call tools — it may call one tool, inspect the results, then decide to call another based on what it found. This multi-turn reasoning is what makes this an agent rather than a simple API wrapper.

python

```
SYSTEM_PROMPT = """You are a senior threat intelligence analyst. When given an Indicator of Compromise (IOC), you systematically investigate it by:

1. Identifying the IOC type and querying the most relevant intelligence source first
2. Analyzing initial results to determine what follow-up queries would be valuable
3. Cross-referencing findings across multiple sources when related indicators are found
4. Mapping observed behaviors and malware families to MITRE ATT&CK techniques
5. Synthesizing all findings into a clear, evidence-based assessment

Always query multiple sources when possible. If an IP lookup reveals associated malware, look up the MITRE techniques for that malware. If a hash lookup reveals contacted domains or IPs, investigate those too. Build the fullest picture you can before forming your assessment.

State your confidence level (low/medium/high) and explain what evidence supports it."""

MAX_TURNS = 10  # cap the agent loop to prevent runaway costs

def process_tool_call(tool_name: str, tool_input: dict) -> str:
    """Route tool calls to the appropriate backend function."""
    handlers = {
        "lookup_ip_reputation": lambda inp: lookup_ip_reputation(inp["ip_address"]),
        "lookup_file_hash": lambda inp: lookup_file_hash(inp["file_hash"], inp["hash_type"]),
        "lookup_domain": lambda inp: lookup_domain(inp["domain"]),
        "get_mitre_techniques": lambda inp: get_mitre_techniques(inp["query"]),
    }
    handler = handlers.get(tool_name)
    if handler is None:
        return json.dumps({"error": f"Unknown tool: {tool_name}"})
    return json.dumps(handler(tool_input), indent=2)

def run_threat_intel_agent(ioc: str, ioc_type: str) -> tuple[str, list[dict]]:
    """
    Run the threat intel enrichment agent on a single IOC.
    Returns (analysis_text, list_of_tool_calls_made).
    """
    user_message = (
        f"Investigate this indicator of compromise and provide a threat assessment:\n"
        f"  IOC: {ioc}\n"
        f"  Type: {ioc_type}\n\n"
        f"Query all relevant intelligence sources, cross-reference findings, "
        f"map to MITRE ATT&CK where applicable, and provide your assessment with "
        f"severity rating, confidence score, and recommended response actions."
    )

    messages = [{"role": "user", "content": user_message}]
    tool_calls_made = []

    for _turn in range(MAX_TURNS):
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages,
        )

        # If Claude is done reasoning, extract final text
        if response.stop_reason == "end_turn":
            final_text = next(
                (block.text for block in response.content if hasattr(block, "text")),
                "No analysis generated.",
            )
            return final_text, tool_calls_made

        # If Claude wants to use tools, process all tool calls in this turn
        if response.stop_reason == "tool_use":
            # Add assistant's response (contains both text and tool_use blocks)
            messages.append({"role": "assistant", "content": response.content})

            # Process each tool call and collect results
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"  -> Calling {block.name}({json.dumps(block.input)})")
                    tool_calls_made.append({"tool": block.name, "input": block.input})
                    result = process_tool_call(block.name, block.input)
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )

            # Send tool results back to Claude
            messages.append({"role": "user", "content": tool_results})
        else:
            # Unexpected stop reason
            return f"Agent stopped unexpectedly: {response.stop_reason}", tool_calls_made

    # Hit turn limit without end_turn
    return (
        f"Agent reached max_turns limit ({MAX_TURNS}) without completing analysis. "
        f"Consider raising MAX_TURNS or simplifying the investigation scope.",
        tool_calls_made,
    )

print("Agent loop ready.")
```

```
Agent loop ready.
```

## Step 5: Run the agent on sample IOCs

Let's test the agent with three different IOC types. Watch the tool call trace — Claude will decide which sources to query and may follow up with additional lookups based on what it finds (e.g., looking up a domain discovered in a hash analysis).

python

```
# Three test cases covering different IOC types
test_cases = [
    {
        "ioc": "203.0.113.42",
        "type": "ip_address",
        "description": "Suspicious IP flagged by firewall for outbound C2 beaconing",
    },
    {
        "ioc": "d131dd02c5e6eec4693d9a0698aff95c",
        "type": "file_hash",
        "description": "File hash from endpoint detection alert (suspected Emotet)",
    },
    {
        "ioc": "secure-bankofamerica-login.com",
        "type": "domain",
        "description": "Domain found in phishing email reported by employee",
    },
]

# Store results for structured report generation
all_results = []

for i, test in enumerate(test_cases, 1):
    print(f"\n{'=' * 70}")
    print(f"  Test Case {i}: {test['description']}")
    print(f"  IOC: {test['ioc']} (Type: {test['type']})")
    print(f"{'=' * 70}\n")
    print("Tool call trace:")

    analysis, tools_used = run_threat_intel_agent(test["ioc"], test["type"])

    all_results.append(
        {
            "ioc": test["ioc"],
            "type": test["type"],
            "description": test["description"],
            "analysis": analysis,
            "tools_used": tools_used,
        }
    )

    print(f"\n--- Agent queried {len(tools_used)} tool(s) ---")
    print(f"\nAnalysis:\n{analysis}")
    print()
```

```
======================================================================
  Test Case 1: Suspicious IP flagged by firewall for outbound C2 beaconing
  IOC: 203.0.113.42 (Type: ip_address)
======================================================================

Tool call trace:

  -> Calling lookup_ip_reputation({"ip_address": "203.0.113.42"})
  -> Calling get_mitre_techniques({"query": "malicious IP command and control beaconing reconnaissance scanning"})

  -> Calling get_mitre_techniques({"query": "Emotet banking trojan command and control lateral movement credential theft"})
  -> Calling get_mitre_techniques({"query": "TrickBot banking trojan credential stealing lateral movement ransomware dropper"})
  -> Calling get_mitre_techniques({"query": "brute force credential access initial access"})

  -> Calling get_mitre_techniques({"query": "malware distribution phishing dropper initial access malspam"})
  -> Calling get_mitre_techniques({"query": "botnet proxy obfuscation port 4444 reverse shell netcat meterpreter"})
  -> Calling get_mitre_techniques({"query": "Wizard Spider Emotet TrickBot Ryuk ransomware deployment multi-stage attack"})

  -> Calling get_mitre_techniques({"query": "ransomware deployment data encryption impact"})
  -> Calling get_mitre_techniques({"query": "proxy anonymization traffic obfuscation multi-hop C2"})

--- Agent queried 10 tool(s) ---

Analysis:
I now have comprehensive intelligence across all relevant dimensions. Let me compile the full threat assessment.

---

# 🔴 THREAT INTELLIGENCE ASSESSMENT REPORT
**IOC:** `203.0.113.42` | **Type:** IPv4 Address
**Report Generated:** 2026-03-10 | **Analyst Level:** Senior Threat Intelligence

---

## 🧭 EXECUTIVE SUMMARY

> **SEVERITY: CRITICAL** | **Confidence: HIGH (87%)**

IP `203.0.113.42` is a **confirmed high-confidence malicious infrastructure node** operating from Saint Petersburg, Russia via ISP **MnogoByte LLC (AS48666)**. With an abuse confidence score of **87/100** and **1,243 community abuse reports**, this IP is actively associated with **Emotet and TrickBot botnet C2 infrastructure** — a combination historically used as a precursor to **Ryuk/Conti ransomware deployment**. The IP is also flagged as a known proxy, expanding its threat surface to traffic obfuscation and attribution evasion.

**Any organization with traffic to/from this IP should treat it as an active compromise and respond immediately.**

---

## 📡 INTELLIGENCE FINDINGS

### 1. IP Reputation Summary

| Field | Value |
|---|---|
| **IP Address** | 203.0.113.42 |
| **Geolocation** | Saint Petersburg, Russia 🇷🇺 |
| **ASN / ISP** | AS48666 / MnogoByte LLC |
| **Abuse Confidence Score** | **87 / 100** 🔴 |
| **Total Abuse Reports** | 1,243 |
| **Last Reported** | March 10, 2026 (Active) |
| **First Observed** | August 15, 2025 |
| **Known Proxy** | ✅ Yes |
| **Tor Exit Node** | ❌ No |

### 2. Threat Type Classifications

| Threat Type | Severity | Description |
|---|---|---|
| 🔴 `botnet_c2` | Critical | Active command-and-control node for botnet operations |
| 🔴 `malware_distribution` | Critical | Serving malware payloads to victim systems |
| 🟠 `brute_force` | High | Active credential stuffing / brute-force attack source |
| 🟠 `spam-source` | High | Malspam email distribution (classic Emotet TTPs) |
| 🟠 `banking-trojan-c2` | High | Confirmed banking trojan C2 infrastructure |

### 3. Malware Associations

#### 🦠 Emotet (Primary Association)
Emotet is one of the world's most dangerous malware families. Originally a banking trojan, it evolved into a **modular malware delivery service** used by multiple threat actors. Emotet infections are a known first-stage precursor to TrickBot and ultimately **Ryuk ransomware** — a chain responsible for hundreds of millions in damages globally. Attribution is strongly linked to **Wizard Spider** (TA542).

#### 🦠 TrickBot (Primary Association)
TrickBot is a sophisticated banking trojan and post-exploitation toolkit. It specializes in **credential theft, lateral movement via SMB/Admin shares, and loading secondary payloads**. TrickBot is a primary component in the "**Big Game Hunting**" ransomware-as-a-service ecosystem (Wizard Spider / FIN6 overlaps). The presence of both Emotet AND TrickBot associations on this single IP indicates a **mature, multi-stage attack infrastructure node**.

### 4. Open Ports — Threat Analysis

| Port | Protocol | Threat Significance |
|---|---|---|
| **443** | HTTPS | C2 traffic blending with legitimate web traffic (T1071.001) |
| **8080** | HTTP-Alt | Common malware C2 and proxy relay port |
| **4444** | TCP | ⚠️ Classic Metasploit/Meterpreter default reverse shell port — strongly indicative of active exploitation tooling |

> ⚠️ **Port 4444** is a significant indicator. This is the default port for **Metasploit Framework's `meterpreter` reverse shells** and is rarely used legitimately. Its presence alongside C2 threat classifications suggests active hands-on-keyboard intrusion activity may be facilitated through this node.

---

## 🛡️ MITRE ATT&CK MAPPING

The following techniques are mapped based on observed threat types, malware associations, and behavioral evidence:

### Tactic: Initial Access
| Technique ID | Name | Evidence Basis |
|---|---|---|
| **T1566.001** | Spearphishing Attachment | Emotet's primary malspam delivery mechanism; `spam-source` tag |
| **T1566.002** | Spearphishing Link | Secondary Emotet delivery; malware distribution role |

### Tactic: Command & Control
| Technique ID | Name | Evidence Basis |
|---|---|---|
| **T1071.001** | Web Protocols (HTTP/HTTPS) | C2 traffic on ports 443/8080 blending with web traffic |
| **T1573.002** | Asymmetric Cryptography | Emotet/TrickBot use encrypted C2 channels |
| **T1008** | Fallback Channels | Botnet infrastructure redundancy; known proxy role |

### Tactic: Credential Access
| Technique ID | Name | Evidence Basis |
|---|---|---|
| **T1056.001** | Keylogging | TrickBot credential harvesting module |
| **T1555.003** | Credentials from Web Browsers | TrickBot browser credential theft |
| **T1003.001** | LSASS Memory Dumping | TrickBot's credential extraction from LSASS |

### Tactic: Lateral Movement
| Technique ID | Name | Evidence Basis |
|---|---|---|
| **T1021.002** | SMB/Windows Admin Shares | TrickBot's worm-like lateral movement capability |
| **T1210** | Exploitation of Remote Services | Active brute-force + port 4444 activity |

### Tactic: Credential Access (Brute Force)
| Technique ID | Name | Evidence Basis |
|---|---|---|
| **T1110.x** | Brute Force | Directly reported threat type: `brute_force` |

---

## 👥 THREAT ACTOR ATTRIBUTION

Based on malware associations and techniques, the following threat groups are assessed as **possible operators or customers** of this infrastructure:

| Threat Group | Confidence | Connection |
|---|---|---|
| **Wizard Spider (TA542)** | 🔴 HIGH | Primary operators of both Emotet and TrickBot; `banking-trojan-c2` tag aligns directly |
| **FIN6** | 🟠 MEDIUM | Associated with TrickBot-to-ransomware campaigns |
| **Sandworm Team** | 🟡 LOW | Russian-nexus overlap; TrickBot technique overlap only |
| **APT28** | 🟡 LOW | Geographic/ISP overlap (Russia); insufficient direct evidence |

> **Assessment Note:** The Emotet + TrickBot combination is the **defining fingerprint of Wizard Spider** operations. The `banking-trojan-c2` tag and Russian hosting strongly support this attribution. APT28/Sandworm attribution remains speculative based on geography alone.

---

## 🔍 ADDITIONAL RISK FACTORS

1. **Known Proxy Status:** This IP is flagged as a known proxy. It may be used to **relay traffic and obfuscate the true origin** of attacker infrastructure, complicating attribution and enabling multi-hop C2 chains.
2. **Infrastructure Age:** First seen August 15, 2025 — this is a **relatively recently stood-up node** (~7 months old), consistent with Emotet's pattern of rapidly cycling C2 infrastructure.
3. **Last Report Today (March 10, 2026):** The infrastructure is **actively being used right now**, not historical.
4. **High Report Volume (1,243):** This is not a borderline case. The volume of independent reports makes false-positive risk extremely low.

---

## ⚡ RECOMMENDED RESPONSE ACTIONS

### 🚨 Immediate (0–4 Hours)
- [ ] **BLOCK** `203.0.113.42` at perimeter firewall, NGFW, and all security layers immediately — inbound AND outbound
- [ ] **Query SIEM/EDR** for all historical connections to/from this IP across the entire environment (last 90 days minimum, given first-seen date of Aug 2025)
- [ ] **Isolate any hosts** that have established connections to this IP — treat as potentially compromised
- [ ] **Alert Security Operations Center (SOC)** and initiate Incident Response protocol if connections are found

### 🔎 Short-Term (4–48 Hours)
- [ ] **Threat Hunt** for Emotet/TrickBot indicators: suspicious `*.doc` / `*.xlsm` executions, `cmd.exe` spawned from `winword.exe`, LSASS access by non-system processes
- [ ] **Search for lateral movement** indicators: anomalous SMB traffic, PsExec usage, new admin share connections after first contact with this IP
- [ ] **Audit Active Directory** for new accounts, privilege escalation, or changes to group policy — TrickBot frequently precedes domain-wide ransomware
- [ ] **Check email logs** for malspam received from or relayed through this IP (ports 25, 465, 587)
- [ ] **Inspect DNS logs** for any domain resolutions associated with this IP

### 🛠️ Medium-Term (48 Hours – 2 Weeks)
- [ ] **Deploy/validate Credential Guard** on all Windows endpoints (mitigates T1003.001 LSASS dumping)
- [ ] **Review and harden SMB exposure** — disable SMBv1, restrict Admin Shares (mitigates T1021.002)
- [ ] **Submit IP to threat intelligence sharing platforms** (ISACs, MISP) to protect peer organizations
- [ ] **Threat model your environment** against Ryuk/Conti ransomware TTPs — this IP's associations represent a known ransomware delivery chain
- [ ] **Implement DMARC/DKIM/SPF** if not already in place to reduce Emotet malspam effectiveness

### 🏛️ Strategic (Ongoing)
- [ ] **Subscribe to Emotet/TrickBot IOC feeds** and automate blocking of emerging C2 infrastructure
- [ ] **Consider threat intelligence platform (TIP)** integration for automated IOC enrichment and blocking
- [ ] **Conduct tabletop exercise** simulating Emotet → TrickBot → Ransomware kill chain

---

## 📊 CONFIDENCE ASSESSMENT

| Dimension | Rating | Rationale |
|---|---|---|
| **Overall Malicious Confidence** | 🔴 HIGH (87%) | Matches abuse score; 1,243 corroborating reports |
| **Malware Attribution (Emotet/TrickBot)** | 🔴 HIGH | Direct database association; consistent with behavioral evidence |
| **Threat Actor Attribution (Wizard Spider)** | 🟠 MEDIUM-HIGH | Strongly implied by malware combo; not directly confirmed |
| **Active Threat Status** | 🔴 HIGH | Last report matches investigation date; infrastructure is live |
| **False Positive Risk** | 🟢 VERY LOW | Volume, recency, and multi-source corroboration make FP highly unlikely |

---

## 🏁 FINAL VERDICT

> `203.0.113.42` is **confirmed malicious infrastructure** with a **CRITICAL threat rating**. It represents an **active, multi-function attack node** serving as Emotet/TrickBot C2, a malware distribution point, and a brute-force source — all hallmarks of the **Wizard Spider** ransomware ecosystem. Any observed connections from your environment to this IP should be treated as a **high-priority security incident**. The presence of port 4444 alongside confirmed C2 activity suggests this node may also support **active post-exploitation operations**.

**Do not delay response actions. The threat is active.**

======================================================================
  Test Case 2: File hash from endpoint detection alert (suspected Emotet)
  IOC: d131dd02c5e6eec4693d9a0698aff95c (Type: file_hash)
======================================================================

Tool call trace:

  -> Calling lookup_file_hash({"file_hash": "d131dd02c5e6eec4693d9a0698aff95c", "hash_type": "md5"})

  -> Calling lookup_ip_reputation({"ip_address": "203.0.113.42"})
  -> Calling lookup_ip_reputation({"ip_address": "203.0.113.88"})
  -> Calling lookup_ip_reputation({"ip_address": "192.0.2.101"})
  -> Calling lookup_domain({"domain": "update-service-cdn.ru"})
  -> Calling lookup_domain({"domain": "cdn-api-gateway.cc"})
  -> Calling get_mitre_techniques({"query": "Emotet banking trojan dropper persistence scheduled task regsvr32 C2 HTTPS beaconing credential theft lateral movement"})

  -> Calling get_mitre_techniques({"query": "regsvr32 living off the land execution DLL side-loading dropper payload delivery"})
  -> Calling get_mitre_techniques({"query": "scheduled task persistence Windows registry autorun startup"})
  -> Calling get_mitre_techniques({"query": "Emotet spambot lateral movement email thread hijacking network propagation"})

--- Agent queried 10 tool(s) ---

Analysis:
I now have comprehensive intelligence across all dimensions. Let me compile the full threat assessment.

---

# 🔴 THREAT INTELLIGENCE ASSESSMENT REPORT

**IOC:** `d131dd02c5e6eec4693d9a0698aff95c` (MD5)
**Analyst Confidence:** 🔴 **HIGH**
**Severity Rating:** 🚨 **CRITICAL**
**Generated:** Active investigation — multi-source corroborated

---

## 1. IOC IDENTIFICATION

| Attribute | Detail |
|-----------|--------|
| **File Name** | `update_service.dll` |
| **File Type** | PE32 Executable (DLL) |
| **File Size** | 237,568 bytes |
| **SHA256** | `a1b2c3d4...abcdef01` |
| **First Seen** | 2025-12-01 |
| **Last Seen** | 2026-03-09 (very recent — **actively circulating**) |
| **Malware Family** | **Emotet (Epoch 5)** |
| **Malware Type** | Banking Trojan / Dropper |

---

## 2. FILE REPUTATION

- **Detection Rate: 58/72 engines (80.6%) — widely flagged as CRITICAL**
- Tagged as: `emotet`, `epoch5`, `banking-trojan`, `dropper`
- The **Epoch 5** designation identifies this as part of Emotet's post-2021 resurgence infrastructure, a well-documented and highly sophisticated botnet cluster operated by **Wizard Spider / TA542**.

---

## 3. INFRASTRUCTURE ANALYSIS

### Contacted IPs

| IP | Country | ISP | Abuse Score | Threat Types | Notes |
|----|---------|-----|-------------|--------------|-------|
| `203.0.113.42` | 🇷🇺 Russia (St. Petersburg) | MnogoByte LLC | **87/100** 🔴 | Botnet C2, Malware Distribution, Brute Force | 1,243 abuse reports; Emotet + TrickBot C2; open ports 443/8080/**4444** |
| `203.0.113.88` | Unknown | — | 0 (no data) | — | ⚠️ Listed in `update-service-cdn.ru` DNS A records — likely a rotating fast-flux node |
| `192.0.2.101` | Unknown | — | 0 (no data) | — | ⚠️ No reputation data — potentially new/undetected infrastructure |

### Contacted Domains

| Domain | Category | Reputation | Registrar | Hosting | Notes |
|--------|----------|------------|-----------|---------|-------|
| `update-service-cdn.ru` | **C2 Server / Malware** | **91/100** 🔴 | REG.RU LLC | MnogoByte LLC, 🇷🇺 Russia | Active; Self-signed SSL; Fast-flux DNS; Emotet + TrickBot tagged |
| `cdn-api-gateway.cc` | Unknown | No data | — | — | ⚠️ No records — likely newly registered or sinkholed; warrants blocking |

### 🔗 Infrastructure Overlap
`update-service-cdn.ru` resolves to **both** `203.0.113.42` AND `203.0.113.88`, directly confirming these IPs are part of the same C2 cluster. The shared hosting provider (MnogoByte LLC) and registrar (REG.RU LLC) are consistent with known Emotet bulletproof hosting patterns.

---

## 4. MITRE ATT&CK MAPPING

| Technique ID | Name | Tactic | Evidence |
|---|---|---|---|
| **T1218.010** *(inferred)* | **Regsvr32** | Execution | Behavior summary: *"Drops secondary payload via regsvr32"* — classic Emotet LOLBin abuse |
| **T1053.005** *(inferred)* | **Scheduled Task/Job** | Persistence | Behavior summary: *"Establishes persistence via scheduled task"* |
| **T1071.001** | **Web Protocols (HTTPS)** | Command & Control | C2 comms over HTTPS on non-standard ports (8080, 4444) |
| **T1573.002** | **Asymmetric Cryptography** | Command & Control | Encrypted C2 channel using self-signed SSL cert |
| **T1008** | **Fallback Channels** | Command & Control | Multiple C2 IPs/domains suggest resilient fallback routing |
| **T1056.001** | **Keylogging** | Collection | Emotet's well-documented credential harvesting capability |
| **T1555.003** | **Credentials from Web Browsers** | Credential Access | Browser credential store extraction |
| **T1003.001** | **LSASS Memory** | Credential Access | Credential dumping from LSASS — enables lateral movement |
| **T1021.002** | **SMB/Windows Admin Shares** | Lateral Movement | Network propagation via stolen credentials + SMB shares |
| **T1210** | **Exploitation of Remote Services** | Lateral Movement | Emotet's worm-like spreading capability |

### 🎭 Associated Threat Actors
- **Wizard Spider / TA542** — Primary Emotet operators
- **TrickBot operators** — Secondary payload delivery (co-infrastructure confirmed)
- **FIN7** — Associated TTPs overlap

> ⚠️ **Critical Escalation Risk:** The co-presence of **Emotet + TrickBot** infrastructure strongly suggests this is a **multi-stage attack chain**. Emotet historically serves as the initial access broker → delivers TrickBot → TrickBot facilitates **Ryuk/Conti ransomware**. This is a known and devastating kill chain.

---

## 5. BEHAVIORAL SUMMARY

```
Execution Chain:
[update_service.dll]
      │
      ├─▶ Regsvr32 (T1218.010) — LOLBin execution, bypasses AppLocker
      │
      ├─▶ Scheduled Task creation (T1053.005) — survives reboots
      │
      ├─▶ C2 Beacon → 203.0.113.42 / update-service-cdn.ru
      │         └── HTTPS on ports 443, 8080, 4444 (encrypted, non-standard)
      │
      ├─▶ Credential Harvesting (Keylogging, LSASS, Browser stores)
      │
      └─▶ Lateral Movement via SMB → Potential TrickBot/Ransomware stage-2
```

---

## 6. CONFIDENCE ASSESSMENT

| Factor | Confidence |
|--------|-----------|
| Malware identification (Emotet Epoch 5) | ✅ HIGH — 80.6% AV detection across 72 engines |
| C2 infrastructure linkage | ✅ HIGH — IP/domain cross-corroborated, shared hosting |
| Threat actor attribution (Wizard Spider) | ✅ HIGH — Epoch 5 tag, TrickBot co-infrastructure |
| Stage-2 ransomware risk | ⚠️ MEDIUM-HIGH — Strongly implied by TrickBot co-infrastructure; not directly observed yet |
| `cdn-api-gateway.cc` / `192.0.2.101` role | ⚠️ LOW — No reputation data; may be new/unregistered infrastructure |

**Overall Confidence: 🔴 HIGH**

---

## 7. RECOMMENDED RESPONSE ACTIONS

### 🛑 Immediate (0–4 Hours)
1. **ISOLATE** any host where `update_service.dll` or MD5 `d131dd02c5e6eec4693d9a0698aff95c` has been detected — assume full compromise.
2. **BLOCK** at all perimeter controls (firewall, proxy, DNS, EDR):
   - IPs: `203.0.113.42`, `203.0.113.88`, `192.0.2.101`
   - Domains: `update-service-cdn.ru`, `cdn-api-gateway.cc`
   - Ports: outbound 8080, 4444 (non-standard HTTPS)
3. **HUNT** across all endpoints for the SHA256 `a1b2c3d4...abcdef01` and filename `update_service.dll`.
4. **RESET** credentials for any accounts active on affected hosts — assume keylogging occurred.

### 🔍 Short-Term (4–48 Hours)
5. **Audit scheduled tasks** across the environment for unauthorized entries (especially recently created ones).
6. **Review regsvr32 execution logs** in EDR/SIEM for any `regsvr32 /s *.dll` invocations.
7. **Inspect LSASS access logs** — look for non-system processes accessing `lsass.exe`.
8. **Analyze network flow data** for beaconing patterns (periodic outbound HTTPS, consistent byte sizes, non-standard ports).
9. **Check for TrickBot IOCs** — the shared infrastructure makes a co-infection highly plausible.
10. **Engage your email security team** — Emotet spreads via malicious email; audit inbound/outbound email gateways and warn users.

### 🏗️ Medium-Term (48 Hours – 2 Weeks)
11. **Deploy Credential Guard** on Windows endpoints to protect LSASS.
12. **Restrict regsvr32** via AppLocker/WDAC policy to prevent LOLBin abuse.
13. **Enable MFA everywhere** — particularly for VPN, email, and privileged accounts.
14. **Implement SMB signing and segmentation** to limit lateral movement.
15. **Conduct full threat hunt** using Emotet Epoch 5 IOC feeds from CISA, Abuse.ch, and MalwareBazaar.
16. **Preserve forensic images** of affected hosts for potential law enforcement engagement — Emotet is a federally tracked criminal enterprise.

### 📢 Escalation Recommendation
> Given the confirmed **Emotet Epoch 5 + TrickBot co-infrastructure**, the risk of **ransomware deployment (Ryuk/Conti/BlackBasta)** is credible and imminent. **Escalate to executive leadership and consider engaging an incident response retainer immediately.** Notify relevant authorities (CISA, FBI IC3) if data exfiltration or ransomware is confirmed.

---

*Report based on multi-source threat intelligence including file reputation (72 AV engines), IP reputation, domain analysis, and MITRE ATT&CK framework mapping. All findings are cross-corroborated across independent intelligence sources.*

======================================================================
  Test Case 3: Domain found in phishing email reported by employee
  IOC: secure-bankofamerica-login.com (Type: domain)
======================================================================

Tool call trace:

  -> Calling lookup_domain({"domain": "secure-bankofamerica-login.com"})
  -> Calling get_mitre_techniques({"query": "phishing credential harvesting fake banking login page brand impersonation"})

  -> Calling lookup_ip_reputation({"ip_address": "192.0.2.55"})
  -> Calling lookup_ip_reputation({"ip_address": "192.0.2.56"})
  -> Calling get_mitre_techniques({"query": "bulletproof hosting infrastructure credential theft web form data exfiltration"})

  -> Calling get_mitre_techniques({"query": "typosquatting domain spoofing lookalike domain brand impersonation financial institution"})
  -> Calling get_mitre_techniques({"query": "phishing kit deployment credential exfiltration C2 data collection victim redirection"})

--- Agent queried 7 tool(s) ---

Analysis:
I now have comprehensive intelligence across all dimensions. Let me synthesize everything into a full threat assessment.

---

# 🚨 THREAT INTELLIGENCE ASSESSMENT REPORT

**IOC:** `secure-bankofamerica-login.com`
**IOC Type:** Domain
**Report Generated:** Based on multi-source intelligence correlation
**Analyst Confidence:** 🔴 **HIGH (92%)**
**Severity Rating:** 🔴 **CRITICAL**

---

## 📋 EXECUTIVE SUMMARY

`secure-bankofamerica-login.com` is a **confirmed, actively operating phishing domain** impersonating Bank of America. It is registered on privacy-shielding infrastructure in Panama, hosted by a bulletproof hosting provider in Moldova, and has already been indexed by URLhaus as a known malicious URL. The domain uses multiple evasion and legitimacy-spoofing tactics — including a valid TLS certificate and deceptive subdomain-style naming — to deceive victims into surrendering banking credentials. **This is a live, ongoing threat requiring immediate containment action.**

---

## 🔬 DETAILED FINDINGS

### 1. Domain Intelligence
| Attribute | Finding | Threat Signal |
|---|---|---|
| **Reputation Score** | 98/100 (Malicious) | 🔴 Critical |
| **Category** | Phishing / Credential Harvesting | 🔴 Critical |
| **Status** | **ACTIVE** | 🔴 Critical |
| **Registrar** | NameSilo LLC | 🟡 Privacy-enabling registrar commonly abused |
| **Registration Date** | 2026-02-28 | 🔴 Newly registered — classic phishing tactic |
| **Registrant Country** | **Panama** | 🔴 Jurisdiction chosen to avoid takedown cooperation |
| **Hosting Provider** | **BulletProof Hosting Ltd** | 🔴 Critical — provider known for ignoring abuse reports |
| **Hosting Country** | **Moldova** | 🔴 Low law-enforcement cooperation jurisdiction |
| **SSL Certificate** | Let's Encrypt (auto-issued) | 🟡 Lends false legitimacy; trivially obtained |
| **Similar Domains Found** | **12 related domains** | 🔴 Part of organized, scalable phishing campaign |
| **URLhaus Reference** | Confirmed malicious listing | 🔴 Critical |
| **Associated IPs w/ Malicious Domains** | TRUE | 🔴 Infrastructure reuse across campaigns |
| **Tags** | `phishing-kit`, `credential-harvest`, `typosquat` | 🔴 Critical |

---

### 2. Infrastructure Analysis

**DNS Architecture:**
```
secure-bankofamerica-login.com
    ├── A Record  →  192.0.2.55  (Primary hosting)
    ├── A Record  →  192.0.2.56  (Redundant/failover)
    └── NS Records → ns1.bulletproof-dns.cc
                     ns2.bulletproof-dns.cc
```

> ⚠️ **Key Finding:** The nameservers (`bulletproof-dns.cc`) are operated by the same bulletproof hosting ecosystem. This creates a **fully insulated, abuse-resistant infrastructure chain** from DNS resolution through to page serving. Takedown requests through standard channels (registrar abuse, hosting provider) are likely to be **ignored or significantly delayed**.

> ⚠️ **Key Finding:** The hosting IPs (192.0.2.55/56) returned **no prior abuse history** — consistent with **freshly provisioned infrastructure**, a deliberate tactic to evade IP reputation blocklists at campaign launch. Expect these IPs to accumulate abuse reports rapidly.

**No MX records** are present, suggesting this domain is used purely for phishing page hosting rather than spear-phishing email delivery from the same domain — email lures likely originate from separate infrastructure.

---

### 3. Attack Anatomy — How This Campaign Likely Operates

```
PHASE 1: LURE DELIVERY
  └─ Victims receive phishing email/SMS/social media link
     containing URL to secure-bankofamerica-login.com
     [T1566.002 - Spearphishing Link]

PHASE 2: DECEPTION
  └─ Victim lands on convincing Bank of America clone page
     • Valid HTTPS/TLS certificate (Let's Encrypt) ✓
     • Domain contains "secure", "bankofamerica", "login" ✓
     • Visually cloned banking portal ✓
     [T1598.003 - Spearphishing Link for Information]

PHASE 3: CREDENTIAL HARVESTING
  └─ Victim enters banking credentials (username, password,
     OTP, security questions, account numbers)
     [T1056.001 - Keylogging / Form Capture]
     [T1555.003 - Credentials from Web Browsers]

PHASE 4: DATA EXFILTRATION
  └─ Captured credentials POSTed to attacker C2
     over HTTPS (T1071.001 - Web Protocols)
     Victim redirected to real BofA site to avoid suspicion

PHASE 5: MONETIZATION / LATERAL DAMAGE
  └─ Credentials sold on dark web marketplaces OR
     used directly for unauthorized account access,
     wire fraud, account takeover
```

---

### 4. MITRE ATT&CK Framework Mapping

| Tactic | Technique ID | Technique Name | Confidence |
|---|---|---|---|
| **Reconnaissance** | T1598.003 | Spearphishing Link (for Information) | High |
| **Initial Access** | T1566.002 | Phishing: Spearphishing Link | High |
| **Credential Access** | T1056.001 | Input Capture: Keylogging / Web Form | High |
| **Credential Access** | T1555.003 | Credentials from Web Browsers | Medium |
| **Collection** | T1056.001 | Input Capture | High |
| **Command & Control** | T1071.001 | Application Layer Protocol: Web | High |
| **Command & Control** | T1573.002 | Encrypted Channel: Asymmetric Crypto (HTTPS) | Medium |
| **Command & Control** | T1008 | Fallback Channels (dual IP hosting) | Medium |

> **Threat Actor Association:** Behavioral patterns are consistent with **TA505**, **FIN7**, **Wizard Spider**, and financially motivated cybercriminal groups. The bulletproof hosting selection and Panama-registered domain are tactics favored by **Eastern European financially motivated threat actors**.

---

### 5. Domain Name Deception Analysis

The domain name `secure-bankofamerica-login.com` is a textbook **combo-squatting / typosquatting** attack:

| Deception Tactic | Detail |
|---|---|
| **Keyword Stuffing** | Contains "secure," "bankofamerica," and "login" — all legitimate-sounding trust signals |
| **Brand Hijacking** | "bankofamerica" is the exact brand name of the targeted institution |
| **False Authority** | "secure" prefix mimics secure subdomain conventions (e.g., `secure.bankofamerica.com`) |
| **TLD Anchoring** | `.com` TLD matches consumer expectations for legitimate banking sites |
| **Visual Similarity** | At a glance, especially on mobile, easily mistaken for the legitimate domain |

**Legitimate domain:** `bankofamerica.com`
**Phishing domain:** `secure-bankofamerica-login.com` ← **NOT affiliated**

---

## ⚡ RECOMMENDED RESPONSE ACTIONS

### 🔴 IMMEDIATE (0–4 Hours)
- [ ] **Block** `secure-bankofamerica-login.com` and IPs `192.0.2.55`, `192.0.2.56` at all DNS resolvers, proxies, firewalls, and email security gateways
- [ ] **Block** nameservers `ns1.bulletproof-dns.cc` / `ns2.bulletproof-dns.cc` to prevent resolution of other domains on same infrastructure
- [ ] **Search** email gateway logs for any inbound messages containing this URL or the string `bankofamerica-login` — quarantine matches
- [ ] **Search** web proxy/DNS logs for any **internal hosts that have already resolved or accessed** this domain — treat any such hosts as potentially compromised
- [ ] **Alert** your security operations center and incident response team

### 🟠 SHORT-TERM (4–24 Hours)
- [ ] **Investigate** the 12 similar domains identified by threat intelligence — submit each for lookup and block confirmed malicious variants
- [ ] **Submit** formal abuse reports to NameSilo (registrar), URLhaus, PhishTank, APWG, and Google Safe Browsing for accelerated blocklisting
- [ ] **Notify** Bank of America's dedicated anti-phishing/brand protection team: `abuse@bankofamerica.com` — they have legal resources for expedited takedowns
- [ ] **Conduct** targeted user communications warning employees and customers about this specific campaign
- [ ] **Deploy** detection rules for the domain pattern `*bankofamerica*login*` across SIEM, EDR, and proxy solutions

### 🟡 MEDIUM-TERM (24–72 Hours)
- [ ] **Conduct** threat hunting across your environment using the full MITRE ATT&CK technique list above, particularly T1566.002 and T1056.001
- [ ] **Enumerate** all 12 similar domains using domain similarity/permutation tools (dnstwist, URLcrazy) and preemptively block plausible variants
- [ ] **Implement** or validate DMARC/DKIM/SPF policies to reduce spoofed email delivery risk
- [ ] **Register** defensive domains for common typosquatting variants of your own brand (if applicable)
- [ ] **Report** infrastructure to bulletproof hosting upstream providers and national CERTs (CERT-MD for Moldova)

### 🔵 LONG-TERM (Ongoing)
- [ ] **Integrate** lookalike domain monitoring (e.g., DomainTools Iris, BrandShield, Recorded Future) to detect new phishing infrastructure early
- [ ] **Implement** FIDO2/hardware MFA for banking and critical accounts — renders harvested credentials non-replayable
- [ ] **Conduct** security awareness training with real examples of this domain spoofing technique
- [ ] **Establish** threat intelligence sharing with your ISAC (FS-ISAC for financial sector) regarding this campaign cluster

---

## 📊 CONFIDENCE ASSESSMENT

| Evidence Factor | Weight | Finding |
|---|---|---|
| Domain reputation score (98/100) | High | Confirms malicious classification |
| Active status confirmed | High | Live threat, not historical |
| URLhaus confirmed listing | High | Third-party corroboration |
| Bulletproof hosting provider | High | Intentional abuse-resistant infrastructure |
| Panama registration + Moldova hosting | Medium | Deliberate jurisdictional evasion |
| 12 similar domains identified | High | Organized, scaled campaign — not opportunistic |
| Phishing-kit tags | Medium | Indicates use of packaged tooling |
| Fresh IPs with no abuse history | Medium | Consistent with new infrastructure, not exculpatory |
| Let's Encrypt SSL | Low-Medium | Legitimacy spoofing, widely abused |

**Overall Confidence: HIGH (92%)** — Multiple independent, corroborating data sources all point to the same conclusion. The only minor uncertainty is the absence of a captured phishing kit binary for hash analysis, which would further confirm specific tooling and actor attribution.

---

> **⚖️ LEGAL NOTE:** This domain constitutes potential criminal trademark infringement, computer fraud, and wire fraud under applicable laws. Organizations with affected customers should engage legal counsel for civil injunction options in addition to standard abuse reporting.
```

## Step 6: Generate structured threat reports

The raw agent analysis is great for a human analyst, but downstream systems (SIEMs, ticketing, SOC dashboards) need structured data. This step takes the agent's free-text analysis and transforms it into a standardized JSON report. In production, you could output STIX 2.1 objects or feed directly into your incident response platform.

python

```
REPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "ioc": {
            "type": "string",
            "description": "The indicator of compromise that was investigated",
        },
        "ioc_type": {
            "type": "string",
            "enum": ["ip_address", "file_hash", "domain", "url", "email"],
        },
        "severity": {
            "type": "string",
            "enum": ["critical", "high", "medium", "low", "informational"],
        },
        "confidence": {"type": "integer", "description": "Confidence score from 0-100"},
        "threat_classification": {
            "type": "string",
            "description": "Primary threat category (e.g., 'banking_trojan_c2', 'phishing', 'apt_infrastructure')",
        },
        "summary": {"type": "string", "description": "One-paragraph executive summary of findings"},
        "related_malware": {"type": "array", "items": {"type": "string"}},
        "related_threat_groups": {"type": "array", "items": {"type": "string"}},
        "mitre_techniques": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "technique_id": {"type": "string"},
                    "technique_name": {"type": "string"},
                    "tactic": {"type": "string"},
                },
            },
        },
        "recommended_actions": {"type": "array", "items": {"type": "string"}},
        "related_iocs": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Other IOCs discovered during investigation",
        },
    },
    "required": [
        "ioc",
        "ioc_type",
        "severity",
        "confidence",
        "threat_classification",
        "summary",
        "recommended_actions",
    ],
}

def generate_structured_report(analysis: str, ioc: str, ioc_type: str) -> dict:
    """Transform free-text agent analysis into a structured JSON report."""
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        system=(
            "You are a threat intelligence report formatter. Convert the analyst's "
            "findings into a structured JSON report matching the provided schema EXACTLY. "
            "Include ONLY the fields listed in the schema — do not add extra fields, "
            "nested objects, or elaboration. Keep array values as simple strings, not "
            "objects. Keep the summary to 2-3 sentences. Return ONLY valid JSON, no "
            "markdown fences."
        ),
        messages=[
            {
                "role": "user",
                "content": (
                    f"Convert this threat intelligence analysis into a structured JSON report.\n\n"
                    f"IOC investigated: {ioc} (type: {ioc_type})\n\n"
                    f"Analysis:\n{analysis}\n\n"
                    f"Schema (include ONLY these fields):\n{json.dumps(REPORT_SCHEMA, indent=2)}\n\n"
                    f"Return the JSON object directly with no markdown formatting."
                ),
            }
        ],
    )

    response_text = response.content[0].text

    # Extract JSON from response (handle markdown code blocks if present)
    if "```json" in response_text:
        json_str = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        json_str = response_text.split("```")[1].split("```")[0].strip()
    else:
        json_str = response_text.strip()

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse structured report: {e}", "raw": response_text}

# Generate structured reports for all test cases
print("=" * 70)
print("  STRUCTURED THREAT INTELLIGENCE REPORTS")
print("=" * 70)

structured_reports = []
for result in all_results:
    report = generate_structured_report(result["analysis"], result["ioc"], result["type"])
    structured_reports.append(report)

    print(f"\n--- {result['ioc']} ---")
    print(json.dumps(report, indent=2))
    print()
```

```
======================================================================
  STRUCTURED THREAT INTELLIGENCE REPORTS
======================================================================

--- 203.0.113.42 ---
{
  "ioc": "203.0.113.42",
  "ioc_type": "ip_address",
  "severity": "critical",
  "confidence": 87,
  "threat_classification": "botnet_c2",
  "summary": "IP 203.0.113.42 is a confirmed malicious infrastructure node hosted in Saint Petersburg, Russia via MnogoByte LLC (AS48666), with an abuse confidence score of 87/100 and 1,243 community abuse reports. It is actively associated with Emotet and TrickBot botnet C2 operations, malware distribution, brute-force attacks, and banking trojan activity \u2014 a combination strongly attributed to the Wizard Spider threat group and historically used as a precursor to Ryuk/Conti ransomware deployment. The infrastructure is currently active as of March 10, 2026, and any observed connections from an organization's environment should be treated as a high-priority security incident requiring immediate response.",
  "related_malware": [
    "Emotet",
    "TrickBot",
    "Ryuk",
    "Conti"
  ],
  "related_threat_groups": [
    "Wizard Spider",
    "TA542",
    "FIN6",
    "Sandworm Team",
    "APT28"
  ],
  "mitre_techniques": [
    {
      "technique_id": "T1566.001",
      "technique_name": "Spearphishing Attachment",
      "tactic": "Initial Access"
    },
    {
      "technique_id": "T1566.002",
      "technique_name": "Spearphishing Link",
      "tactic": "Initial Access"
    },
    {
      "technique_id": "T1071.001",
      "technique_name": "Web Protocols",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1573.002",
      "technique_name": "Asymmetric Cryptography",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1008",
      "technique_name": "Fallback Channels",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1056.001",
      "technique_name": "Keylogging",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1555.003",
      "technique_name": "Credentials from Web Browsers",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1003.001",
      "technique_name": "LSASS Memory",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1110",
      "technique_name": "Brute Force",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1021.002",
      "technique_name": "SMB/Windows Admin Shares",
      "tactic": "Lateral Movement"
    },
    {
      "technique_id": "T1210",
      "technique_name": "Exploitation of Remote Services",
      "tactic": "Lateral Movement"
    }
  ],
  "recommended_actions": [
    "Block 203.0.113.42 at perimeter firewall, NGFW, and all security layers immediately for both inbound and outbound traffic",
    "Query SIEM and EDR for all historical connections to or from this IP across the entire environment for at least the last 90 days",
    "Isolate any hosts that have established connections to this IP and treat them as potentially compromised",
    "Alert the Security Operations Center and initiate Incident Response protocol if connections are found",
    "Threat hunt for Emotet and TrickBot indicators including suspicious Office document executions and cmd.exe spawned from winword.exe",
    "Search for lateral movement indicators such as anomalous SMB traffic, PsExec usage, and new admin share connections",
    "Audit Active Directory for new accounts, privilege escalation, or group policy changes that may indicate TrickBot post-exploitation activity",
    "Review email logs for malspam received from or relayed through this IP",
    "Inspect DNS logs for any domain resolutions associated with this IP",
    "Deploy or validate Credential Guard on all Windows endpoints to mitigate LSASS credential dumping",
    "Disable SMBv1 and restrict Admin Shares to mitigate TrickBot lateral movement techniques",
    "Subscribe to Emotet and TrickBot IOC feeds and automate blocking of emerging C2 infrastructure",
    "Implement DMARC, DKIM, and SPF if not already in place to reduce Emotet malspam effectiveness",
    "Conduct a tabletop exercise simulating the Emotet to TrickBot to ransomware kill chain"
  ],
  "related_iocs": []
}

--- d131dd02c5e6eec4693d9a0698aff95c ---
{
  "ioc": "d131dd02c5e6eec4693d9a0698aff95c",
  "ioc_type": "file_hash",
  "severity": "critical",
  "confidence": 85,
  "threat_classification": "banking_trojan_dropper",
  "summary": "The investigated MD5 hash corresponds to update_service.dll, identified as Emotet Epoch 5, a banking trojan and dropper operated by Wizard Spider/TA542, detected by 80.6% of 72 AV engines. The sample communicates with confirmed C2 infrastructure hosted in Russia and exhibits credential harvesting, persistence, and lateral movement behaviors consistent with a multi-stage attack chain. The co-presence of TrickBot infrastructure indicates a high risk of downstream ransomware deployment via Ryuk, Conti, or BlackBasta.",
  "related_malware": [
    "Emotet",
    "TrickBot",
    "Ryuk",
    "Conti",
    "BlackBasta"
  ],
  "related_threat_groups": [
    "Wizard Spider",
    "TA542",
    "FIN7"
  ],
  "mitre_techniques": [
    {
      "technique_id": "T1218.010",
      "technique_name": "Regsvr32",
      "tactic": "Execution"
    },
    {
      "technique_id": "T1053.005",
      "technique_name": "Scheduled Task/Job",
      "tactic": "Persistence"
    },
    {
      "technique_id": "T1071.001",
      "technique_name": "Web Protocols (HTTPS)",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1573.002",
      "technique_name": "Asymmetric Cryptography",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1008",
      "technique_name": "Fallback Channels",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1056.001",
      "technique_name": "Keylogging",
      "tactic": "Collection"
    },
    {
      "technique_id": "T1555.003",
      "technique_name": "Credentials from Web Browsers",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1003.001",
      "technique_name": "LSASS Memory",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1021.002",
      "technique_name": "SMB/Windows Admin Shares",
      "tactic": "Lateral Movement"
    },
    {
      "technique_id": "T1210",
      "technique_name": "Exploitation of Remote Services",
      "tactic": "Lateral Movement"
    }
  ],
  "recommended_actions": [
    "Isolate any host where update_service.dll or MD5 d131dd02c5e6eec4693d9a0698aff95c has been detected and assume full compromise",
    "Block IPs 203.0.113.42, 203.0.113.88, and 192.0.2.101 at all perimeter controls including firewall, proxy, DNS, and EDR",
    "Block domains update-service-cdn.ru and cdn-api-gateway.cc across all perimeter controls",
    "Block outbound traffic on non-standard ports 8080 and 4444",
    "Hunt across all endpoints for SHA256 a1b2c3d4...abcdef01 and filename update_service.dll",
    "Reset credentials for any accounts active on affected hosts due to confirmed keylogging capability",
    "Audit scheduled tasks across the environment for unauthorized or recently created entries",
    "Review regsvr32 execution logs in EDR/SIEM for suspicious DLL invocations",
    "Inspect LSASS access logs for non-system processes accessing lsass.exe",
    "Analyze network flow data for beaconing patterns on non-standard ports",
    "Check for TrickBot IOCs given shared infrastructure confirming likely co-infection",
    "Engage email security team to audit gateways and warn users as Emotet spreads via malicious email",
    "Deploy Credential Guard on Windows endpoints to protect LSASS",
    "Restrict regsvr32 via AppLocker or WDAC policy to prevent LOLBin abuse",
    "Enable MFA on VPN, email, and all privileged accounts",
    "Implement SMB signing and network segmentation to limit lateral movement",
    "Conduct full threat hunt using Emotet Epoch 5 IOC feeds from CISA, Abuse.ch, and MalwareBazaar",
    "Preserve forensic images of affected hosts and consider notifying CISA and FBI IC3",
    "Escalate to executive leadership and engage an incident response retainer given imminent ransomware risk"
  ],
  "related_iocs": [
    "203.0.113.42",
    "203.0.113.88",
    "192.0.2.101",
    "update-service-cdn.ru",
    "cdn-api-gateway.cc",
    "a1b2c3d4...abcdef01",
    "update_service.dll"
  ]
}

--- secure-bankofamerica-login.com ---
{
  "ioc": "secure-bankofamerica-login.com",
  "ioc_type": "domain",
  "severity": "critical",
  "confidence": 92,
  "threat_classification": "phishing",
  "summary": "secure-bankofamerica-login.com is a confirmed, actively operating phishing domain impersonating Bank of America, registered via a privacy-shielding registrar in Panama and hosted on bulletproof infrastructure in Moldova. The domain employs credential harvesting tactics including TLS certificate spoofing and deceptive keyword-stuffed naming, and has been corroborated as malicious by URLhaus. Immediate blocking and incident response actions are required, as this domain is part of an organized phishing campaign cluster with 12 identified related domains.",
  "related_malware": [
    "phishing-kit"
  ],
  "related_threat_groups": [
    "TA505",
    "FIN7",
    "Wizard Spider"
  ],
  "mitre_techniques": [
    {
      "technique_id": "T1598.003",
      "technique_name": "Spearphishing Link for Information",
      "tactic": "Reconnaissance"
    },
    {
      "technique_id": "T1566.002",
      "technique_name": "Phishing: Spearphishing Link",
      "tactic": "Initial Access"
    },
    {
      "technique_id": "T1056.001",
      "technique_name": "Input Capture: Keylogging / Web Form",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1555.003",
      "technique_name": "Credentials from Web Browsers",
      "tactic": "Credential Access"
    },
    {
      "technique_id": "T1071.001",
      "technique_name": "Application Layer Protocol: Web",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1573.002",
      "technique_name": "Encrypted Channel: Asymmetric Cryptography",
      "tactic": "Command and Control"
    },
    {
      "technique_id": "T1008",
      "technique_name": "Fallback Channels",
      "tactic": "Command and Control"
    }
  ],
  "recommended_actions": [
    "Block secure-bankofamerica-login.com at all DNS resolvers, proxies, firewalls, and email security gateways immediately",
    "Block hosting IPs 192.0.2.55 and 192.0.2.56 at perimeter firewall and proxy",
    "Block nameservers ns1.bulletproof-dns.cc and ns2.bulletproof-dns.cc to prevent resolution of related domains",
    "Search email gateway logs for inbound messages containing this URL or the string 'bankofamerica-login' and quarantine matches",
    "Search DNS and web proxy logs for internal hosts that have already resolved or accessed this domain and treat as potentially compromised",
    "Investigate and block the 12 similar domains identified during the investigation",
    "Submit abuse reports to NameSilo, URLhaus, PhishTank, APWG, and Google Safe Browsing",
    "Notify Bank of America brand protection team at abuse@bankofamerica.com for expedited takedown",
    "Deploy SIEM and EDR detection rules for the domain pattern *bankofamerica*login*",
    "Conduct threat hunting using MITRE techniques T1566.002 and T1056.001 across the environment",
    "Implement or validate DMARC, DKIM, and SPF policies to reduce spoofed email delivery risk",
    "Implement FIDO2 or hardware MFA for banking and critical accounts to render harvested credentials non-replayable",
    "Report infrastructure to CERT-MD and notify FS-ISAC regarding this campaign cluster",
    "Integrate lookalike domain monitoring tooling for ongoing early detection of new phishing infrastructure"
  ],
  "related_iocs": [
    "192.0.2.55",
    "192.0.2.56",
    "ns1.bulletproof-dns.cc",
    "ns2.bulletproof-dns.cc"
  ]
}
```

## Summary and next steps

This cookbook demonstrated how to build a threat intelligence enrichment agent that autonomously investigates IOCs by querying multiple data sources, cross-referencing findings, and producing structured reports. The key patterns you can take away:

* **Tool-use agentic loop**: Claude decides which tools to call and follows up based on results — no hardcoded query sequences
* **Modular tool design**: Each intelligence source is a clean function with a well-defined schema, making it straightforward to swap in real APIs
* **Multi-source correlation**: The system prompt encourages Claude to pivot across sources (e.g., hash → contacted IPs → IP reputation → MITRE mapping)
* **Structured output**: Raw analysis is transformed into machine-readable reports for downstream systems

### Making this production-ready

**Swap in real APIs**: Replace mock functions with calls to VirusTotal, AbuseIPDB, Shodan, GreyNoise, URLhaus, DomainTools, or your organization's internal threat intel feeds. The tool schemas and agent loop stay the same.

**Add more tools**: WHOIS lookups, passive DNS, SSL certificate transparency logs, sandbox detonation (e.g., Joe Sandbox, Hybrid Analysis), and EDR/SIEM enrichment queries.

**Scale with async**: For bulk IOC processing, use `asyncio` to run tool calls in parallel and process IOC queues. Consider caching results with TTLs to avoid redundant API calls.

**Harden structured output**: Use Claude's tool-use capability to force JSON schema compliance instead of parsing free text, or validate reports against the `REPORT_SCHEMA` defined in Step 6.

**Integrate with your stack**: Export structured reports as STIX 2.1 bundles, push to Splunk/Elastic/SOAR platforms, or feed into ticketing systems for automated incident creation.

**Add confidence calibration**: Weight confidence scores based on source reliability, data freshness, and cross-source corroboration. Sources that agree independently should boost confidence.

### Further reading

* [Building effective agents](https://anthropic.com/research/building-effective-agents) — Anthropic's research on agent patterns
* [Tool use documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) — Complete guide to Claude's tool-use capabilities
* [MITRE ATT&CK](https://attack.mitre.org/) — Framework referenced in this cookbook
