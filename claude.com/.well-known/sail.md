<!-- source: https://claude.com/.well-known/sail -->

schema = "draft-kelley-webbotauth-sail-00"
modified = 2026-10-22T18:36:00Z
expires\_after = 3600 # seconds
[[prefix\_sets]]
name = "agentic-browser-use"
# `exclusive=true` means that all traffic from these ranges will be documented in this file.
exclusive = true
ipv4\_prefixes = [
"136.71.21.147",
"34.31.25.14",
"34.67.187.248",
"34.71.122.171",
"34.70.177.231",
"34.66.255.143",
"34.68.65.207",
"34.171.207.92",
"34.60.73.195",
]
ipv6\_prefixes = []
[[services]]
name = "Claude-Agent"
# `exhaustive=true` means that all egress traffic from this service will originate from the prefixes listed in this section.
exhaustive = true
prefix\_sets = ["agentic-browser-use"]
