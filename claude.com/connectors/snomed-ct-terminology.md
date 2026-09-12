<!-- source: https://claude.com/connectors/snomed-ct-terminology -->

[Skip to main content](#main-content)

Connector URL`https://snowstorm-mcp.snomedtools.org/mcp`

More[Documentation (opens in new tab)](https://github.com/IHTSDO/snowstorm-mcp-server)[Support (opens in new tab)](mailto:techsupport@snomed.org)[Privacy policy (opens in new tab)](https://github.com/IHTSDO/snowstorm-mcp-server/blob/main/PRIVACY.md)

SNOMED CT is the world's most comprehensive clinical terminology, used in electronic health records across more than 80 countries. This connector gives Claude direct access to it through SNOMED International's terminology server.

Use it to look up concepts by code or name, validate that a code exists and is active, test subsumption between concepts, navigate the hierarchy (ancestors, children, descendants), and expand value sets using Expression Constraint Language (ECL). It works across all SNOMED CT editions available on the connected backend, including the International, US and Australian editions.

Every tool is read-only, the connector never modifies terminology data. It runs as a stateless proxy to the configured Snowstorm instance, holding no query content or personal data between requests.

Built and maintained by SNOMED International, the owners of SNOMED CT.

## Tools

* fhir\_metadata
* list\_terminologies
* server\_capabilities
* server\_health
* snomed\_expand
* snomed\_get\_ancestors
* snomed\_get\_children
* snomed\_get\_descendants
* snomed\_lookup
* snomed\_subsumes
* snomed\_validate\_code
* snowstorm\_get\_concept\_native
* snowstorm\_list\_codesystems
* snowstorm\_list\_versions
* snowstorm\_search\_concepts

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://storage.googleapis.com/media-assets-299d7136-cb52-d546-ee02-34bc1307c35f/mcp-directory/icons/pubmed.svg)

### [PubMed](https://claude.com/connectors/pubmed)

Search biomedical literature from PubMed

[Add PubMed in Claude (opens in new tab)](https://claude.ai/directory/81cc5080-a204-4aa1-a694-fa868a3c8721 "Add in Claude")

![](https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/20/99/8f/20998fe7-dd23-ba49-aa02-8d0d939c5d7e/AppIcon-0-0-1x_U007emarketing-0-0-0-2-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/1200x630wa.png)

### [Cortellis CMC Intelligence](https://claude.com/connectors/cortellis-cmc-intelligence)

Trusted regulatory CMC insights, powered by Clarivate’s Cortellis CMC Intelligence.

[Add Cortellis CMC Intelligence in Claude (opens in new tab)](https://claude.ai/directory/6d85e32b-e41b-44bc-b451-aa020b7640b1 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=consensus.app&sz=96)

### [Consensus](https://claude.com/connectors/consensus)

Explore scientific research

[Add Consensus in Claude (opens in new tab)](https://claude.ai/directory/65247229-f0c7-49df-9044-fcbb8b3894c6 "Add in Claude")

![](https://storage.googleapis.com/media-assets-299d7136-cb52-d546-ee02-34bc1307c35f/mcp-directory/icons/clinical-trials.png)

### [Clinical Trials](https://claude.com/connectors/clinical-trials)

Access ClinicalTrials.gov data

[Add Clinical Trials in Claude (opens in new tab)](https://claude.ai/directory/c1754944-3ad1-49ab-bec5-9aeae3a6a9a3 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=scholargateway.ai&sz=96)

### [Scholar Gateway](https://claude.com/connectors/scholar-gateway)

Enhance responses with scholarly research and citations

[Add Scholar Gateway in Claude (opens in new tab)](https://claude.ai/directory/ff091334-0f12-4d0e-a973-c00467dd3818 "Add in Claude")

![](https://storage.googleapis.com/media-assets-299d7136-cb52-d546-ee02-34bc1307c35f/mcp-directory/icons/biorxiv.png)

### [bioRxiv](https://claude.com/connectors/biorxiv)

Access bioRxiv and medRxiv preprint data

[Add bioRxiv in Claude (opens in new tab)](https://claude.ai/directory/7f750eb6-c3cb-47d7-9269-d35c43fe9925 "Add in Claude")
