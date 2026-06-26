<!-- source: https://www.anthropic.com/news/us-elections-readiness -->

# U.S. Elections Readiness

Oct 8, 2024

![U.S. Elections Readiness](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd349f9f92aaf574702f002fbb2b01159e6e4c659-1200x631.png&w=3840&q=75)

2024 marks the first United States (U.S.) election cycle where generative AI tools are widely available. Since July 2023, we have [taken concrete steps](https://www.anthropic.com/news/preparing-for-global-elections-in-2024) to [help detect and mitigate](https://www.anthropic.com/news/testing-and-mitigating-elections-related-risks) against the potential misuse of our tools and to direct users to authoritative election information. Ahead of federal, state, and local elections in the U.S. on November 5, 2024, we are sharing a summary of our work thus far.

## Our policy approach

In May, we updated our [Usage Policy](https://www.anthropic.com/legal/aup) to provide clarity around prohibited uses when it comes to elections and voting:

* **Prohibit campaigning & lobbying:** We prohibit the use of our products for political campaigning and lobbying. Under our policy, Claude cannot be used to promote a specific candidate, party or issue; for targeted political campaigns; or for soliciting votes or financial contributions.
* **Combating misinformation & election interference:** We prohibit the use of our products to generate misinformation on election laws, candidates, and other related topics. We also do not allow Claude to be used to target voting machines or obstruct the counting or certification of votes.
* **Limiting outputs to text only:** Claude cannot generate images, audio or videos, eliminating the risk of election related deepfakes.

We have also developed improved tools for detecting coordinated behavior or other elections-related misuse of our systems:

* **Strict enforcement:** To detect and prevent misuse, we deploy automated systems to enforce our policies and audit those systems with human review. We use a variety of methods to mitigate misuse, including:
  + Leveraging prompt modifications on claude.ai
  + Auditing use cases on our first-party API
  + In some extreme cases, suspending accounts
  + Working closely with Amazon Web Services (AWS) and Google Cloud Platform (GCP) to detect and mitigate election-related harms from users accessing Anthropic models on those platforms.

## Evaluating and refining our interventions

We regularly conduct targeted red-teaming to examine how our systems respond to prompts related to election issues.

* **Ongoing vulnerability testing:** We use in-depth testing conducted in collaboration with external subject matter experts, called [Policy Vulnerability Testing](https://www.anthropic.com/news/testing-and-mitigating-elections-related-risks) (PVT), to identify potential risks. We focus on misinformation, bias and adversarial abuse by identifying relevant questions (e.g., asking where and how someone can vote in the US election), document model responses, and note the presence of “safety interventions,” like declining to answer harmful questions.
* **Preventing misinformation at scale**: We have built automated evaluations to test our systems at scale for a variety of election-related risks and assess the effectiveness of our interventions. These include ways of testing for:
  + Political parity in model responses across candidates and topics
  + The degree to which our systems refuse to respond to harmful queries about the election
  + How robust our systems are in preventing misinformation and voter profiling tactics
* **Improving our controls:** In response to the findings, we continuously adapt our policies, strengthen our enforcement processes, and make technical refinements to the models themselves to address identified risks and make our systems more robust.

## Providing accurate information and ensuring transparency

Because our models are not trained frequently enough to provide real-time information about elections, we redirect users to accurate, up-to-date and authoritative voting information for elections-related queries.

* **Redirecting to reliable voting information**: We implemented a pop-up giving users the option to be redirected to TurboVote (a nonpartisan resource from Democracy Works) if they ask for voting information.
  + Recently, Turbovote was updated to include the names of all candidates running in federal and state elections, as well as ballot propositions.
* **Referencing the model’s “knowledge cut off date:”** We have also updated Claude’s system prompt to include a clear reference to its knowledge cutoff date (the date up to which Claude’s training data extends).
* **Sharing learnings:** To help others improve their own election integrity efforts and drive better safety outcomes across the industry, we released some of the automated evaluationswe developed and launched an [initiative to fund third-party evaluations](https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations) that effectively measure AI capabilities and risks.

Throughout this year, we’ve met with global policymakers, civil society organizations, and others in industry to discuss our election work and inform our efforts. We’ve also engaged in proactive scenario planning to better prepare for potential election related abuse in the lead-up to election day in the U.S.

We cannot anticipate every way people might use our models related to elections, but we have and will continue to learn from and iterate on our processes, testing and improving our systems along the way.

Additional resources:

* February 2024, [Preparing for global elections in 2024](https://www.anthropic.com/news/preparing-for-global-elections-in-2024)
* May 2024, [Updating our Usage Policy](https://www.anthropic.com/news/updating-our-usage-policy)
* June 2024, [Testing and mitigating elections-related risks](https://www.anthropic.com/news/testing-and-mitigating-elections-related-risks)

Relevant safety work:

* June 2024, [Claude 3.5 Sonnet launch](https://www.anthropic.com/news/claude-3-5-sonnet),
* June 2024, [Claude 3.5 Model Card Addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf)
