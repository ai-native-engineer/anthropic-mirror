<!-- source: https://claude.com/docs/claude-science/literature-access -->

Claude retrieves open-access full text without credentials. Add publisher keys or your library’s proxy in **Settings > Credentials, under Literature access,** to reach paywalled text you’re entitled to. No key bypasses a paywall.
Given a DOI or title, Claude tries in order: open-access copy (Unpaywall, Semantic Scholar, PubMed Central), publisher routes you hold keys for, your library proxy, then the publisher page. Retrieved files (PDF, XML, or text) are saved into the session.

##  Available credentials

| Credential | Effect |
| --- | --- |
| **Elsevier API key** + institutional token | Enables the Elsevier route (subscription still required) |
| **Springer Nature API key** | Enables the Springer Nature route |
| **Semantic Scholar API key** | Speeds the Semantic Scholar step |
| **NCBI API key** | Raises PubMed rate limit from 3 to 10 requests per second |
| Institutional **EZproxy URL** + session cookie | Retries publisher links through your library |

NCBI, EBI, and OurResearch (Unpaywall) ask callers to provide a contact email. The first time this applies, a **Share a contact email with research data services?** card appears. Sharing an email enables the Unpaywall step. You can also set this in **Settings** > General > **Contact email**.
Claude paces requests to each provider at one per second, backs off when asked, and identifies itself in every request. Paywalled HTML isn’t scraped.

[Cloud storage](/docs/claude-science/cloud-storage)[Custom connectors](/docs/claude-science/custom-connectors)
