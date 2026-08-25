<!-- source: https://privacy.claude.com/en/articles/10807912-how-does-clio-analyze-usage-patterns-while-protecting-user-data -->

# How does Clio analyze usage patterns while protecting user data?

Anthropic performs aggregated, privacy-preserving analysis of data to gain insights into the real-world impacts of AI systems and the usage patterns of our products while rigorously maintaining user privacy and the confidentiality of sensitive information. One example of our approach is [Clio](https://www.anthropic.com/research/clio), a system that enables us to understand important trends and behaviors without compromising individual privacy or customer confidentiality.

When we use Clio for research purposes or to analyze how our products are being used in aggregate, the system:

* Automatically anonymizes and aggregates information, extracting only general patterns and trends while omitting private or sensitive details
* Applies multiple privacy safeguards, including minimum aggregation thresholds and automated verification to ensure results do not reveal information about individuals or small groups of customers
* Provides no access for Anthropic employees to raw user conversations or customer-specific data
* Focuses all insights on broad, aggregate patterns only, never analyzing any specific individual or customer’s behavior

We have conducted extensive testing, auditing, and benchmarking to validate that Clio's outputs contain no identifiable private information when used for these purposes. For detailed information on Clio's architecture and our rigorous privacy evaluations, please see our [research paper](https://arxiv.org/abs/2412.13678).

To further advance our mission, we may also share aggregate, privacy-preserving insights on how our AI systems are being used with external audiences or with the public. Clio implements careful aggregation thresholds that require each insight to represent a meaningful diversity of users and inputs, which guards against identification of an individual’s specific usage patterns.

As described in our [research paper](https://arxiv.org/abs/2412.13678), we also use a different version of Clio to improve our safety systems. The results from safety-focused Clio runs can be linked back to individual accounts. We put in place strict access controls to limit who can view these results to a small number of authorized staff.

* [How Do You Use Personal Data in Model Training?](https://privacy.claude.com/en/articles/10023555-how-do-you-use-personal-data-in-model-training)
* [How does Anthropic protect the personal data of Claude users?](https://privacy.claude.com/en/articles/10458704-how-does-anthropic-protect-the-personal-data-of-claude-users)
* [How does Clio analyze usage patterns while protecting user data?](https://privacy.claude.com/en/articles/10812588-how-does-clio-analyze-usage-patterns-while-protecting-user-data)
* [How does Anthropic Interviewer collect and use my data?](https://privacy.claude.com/en/articles/12996960-how-does-anthropic-interviewer-collect-and-use-my-data)
* [Anthropic Interviewer sessions completed after March 23, 2026](https://privacy.claude.com/en/articles/14170919-anthropic-interviewer-sessions-completed-after-march-23-2026)
