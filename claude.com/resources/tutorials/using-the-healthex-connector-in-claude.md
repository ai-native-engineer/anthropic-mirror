<!-- source: https://claude.com/resources/tutorials/using-the-healthex-connector-in-claude -->

# Using the HealthEx Connector in Claude

  Healthcare
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-healthex-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

HealthEx connects Claude to your personal health records from all your care providers. This article explains how to set up and use the HealthEx integration with Claude to understand and manage your health data.

The HealthEx integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

More details about this integration can also be found in [HealthEx’s Connector Support Guide](https://healthex.io/guides/claude).

## **What this integration provides**

HealthEx allows you to connect Claude to your health records, securely pulling data from all your care providers into one place. Ask Claude to summarize your health, understand lab results, help prep for your next doctor's visit, and guide your daily routine.  Setup takes minutes: Verify your identity using biometrics and a government ID to ensure only you are getting access to your own health data then connect your healthcare portal logins. Currently free, HealthEx is a Patient-First Privacy platform that follows the HIPAA Privacy Rule and is SOC2 compliant.

## **Who should use the HealthEx integration**

The HealthEx connector is for patients, including:

* Individuals managing chronic conditions (diabetes, heart disease, autoimmune illness, etc.)
* Individuals coordinating care across multiple providers or systems
* Individuals preparing for procedures, follow-ups, or second opinions
* Health-literate individuals wanting clearer explanations of labs, imaging, and notes
* Biohackers or proactive wellness users seeking deeper insight into their history
* People navigating new diagnoses or confusing medical documentation
* Any individual looking to better manage their health and take control of their health journey

## **Who can access the HealthEx integration**

The HealthEx connector is available to all Claude Max users in the United States at no additional charge. Consumers complete CLEAR-powered identity verification and provide explicit, revocable consent before any clinical records are retrieved. HealthEx uses CLEAR to verify your identity, but doesn't share biometric data or ID information with Claude.

Key requirements across all HealthEx connector users:

* CLEAR-verified identity is required before any record retrieval.
* Explicit, task-scoped consent governs all data access.
* Permissions can be viewed, limited, or revoked at any time.
* HealthEx applies a privacy-first, minimum-necessary access model, with data retrieved only when requested.

More details on accessing the integration can be found in [HealthEx’s Connector Support Guide](https://healthex.io/guides/claude).

## **Example use cases**

The HealthEx connector helps people understand, organize, and act on their own health through clear, personalized insights grounded in their real medical history.

* **Get an overview:** “*Show me a summary of my health records.*”
* **Learn about your health:** “*Help me understand my most recent lab results.*”
* **Plan your care:** “*What questions should I ask my doctor at my next visit?*”
* **Guide your daily routine:** “*What types of exercise would be best for me?”*

## **Setting up the HealthEx integration in Claude**

**For Individual Claude Users**

1. From [Claude.ai](http://claude.ai) or the Claude Desktop App, navigate to Settings > Connectors (Note: initial connector set-up cannot be completed from the Claude Mobile app)
2. Find “**HealthEx**”
3. Click “Connect”
4. Choose whether to grant permission for Claude to access HealthEx
5. Follow HeathEx’s instructions to complete CLEAR-powered identity verification and provide explicit, revocable consent before any clinical records are retrieved (See How to [securely connect to your HealthEx account](https://healthex.io/guides/claude) for more details)

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

Technical details of the HealthEx integration can be found in [HealthEx’s MCP Server Documentation](https://docs.healthex.io/category/healthex-mcp-server).

## **How to securely connect to your HealthEx account**

Setup can take a few minutes. Users will need a phone, a valid US government ID, and logins for health portals.

1. Click get started
2. Begin with identity verification by clicking Verify with CLEAR   
   1. You will typically need to enter a phone number, email address, take a selfie, and take a picture of the front and back of your valid US government ID.
   2. CLEAR will transition you to your phone from the desktop via a text code or QR code. Once you are done, you will automatically be transitioned back to the HealthEx Connector experience on the desktop.
3. Next, you will be asked to consent to access and connect your health records     
   1. You will authorize HealthEx to access your records on your behalf for up to 1 year. You have the ability to withdraw your consent at any time.
   2. You will authorize that Claude can connect to your data for up to 1 year for any conversations that will access the HealthEx MCP server. You can disconnect the HealthEx Connector at any time and/or withdraw consent at any time.
4. Next, you will review and log in to health systems where records were automatically found    
   1. You can login to your health portals one by one.
   2. If you do not have a specific login available or do not want to include a set of records, you can choose Skip Records from this Provider
   3. When you login to each portal, you will be asked to consent for your provider to give HealthEx access–this is expected.    
      1. For EPIC sites, data sets are checked by default and you can unselect any items you wish to not include. Then you will need to select a duration–you can select any timeframe here.
5. Next, you have the option to Add a Provider to create a complete set of your health records.    
   1. Search for a clinic name or health system where you have received care. The ones closest to you will populate at the top of the search results
   2. Select one and login. You will do this with each provider you add.
   3. Add as many providers to create your complete list
6. Next, you will review your complete list and click Access Records   
   1. In the background, HealthEx will be retrieving records and preparing them for use in Claude. This can take anywhere from 10-30 minutes given the types and size of the health records.
7. Lastly, click Finish and Return to Claude   
   1. You are done with your part. We will notify you via email as soon as your records are connected to Claude so you can begin your first conversation.

## **How does Claude protect my data privacy and safety?**

Your health information is personal. That's why we've built Claude to work with integrations like HealthEx with privacy and user empowerment at the core.

‍

**Connected only with your consent**

Claude connects to HealthEx only when you explicitly choose to enable the integration. [Anthropic’s Consumer Health Data Privacy Policy](https://anthropic.com/legal/consumer-health-data-privacy-policy) describes exactly how we collect, use, and protect your information—so you always know what to expect. We also protect sensitive health data from inadvertent sharing to other integrated connectors by requiring you to consent to each integration in conversations where HealthEx data is being discussed.

**Minimal data, maximum relevance**

When you ask a health-related question, Claude pulls only the data it needs to answer that specific question. Your full health record isn't accessed unless it's relevant to what you're asking.

**Your conversations stay private**

Chats that use the HealthEx integration are never used to train our models. We’ve designed our memory feature so that Claude does not use sensitive health data in future conversations, while still keeping in mind your areas of concern to inform your conversations.

**Empowering you, not replacing your doctor**

Claude is designed to help you better understand and take ownership of your healthcare journey — not to provide medical advice, diagnoses, or treatment recommendations. Always consult your physician for medical decisions.

‍

## Related tutorials

[How to use the Prior Auth Review sample skill with Claude](/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8)How to use the Prior Auth Review sample skill with Claude

How to use the Prior Auth Review sample skill with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8)Tutorial

[Using the Function Connector in Claude](/resources/tutorials/using-the-function-connector-in-claude)Using the Function Connector in Claude

Using the Function Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-function-connector-in-claude)Tutorial

[How to use the FHIR Developer agent skill with Claude Code](/resources/tutorials/how-to-use-the-fhir-developer-agent-skill-with-claude-code)How to use the FHIR Developer agent skill with Claude Code

How to use the FHIR Developer agent skill with Claude Code

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-fhir-developer-agent-skill-with-claude-code)Tutorial

[Using the NPI Registry Connector in Claude](/resources/tutorials/using-the-npi-registry-connector-in-claude)Using the NPI Registry Connector in Claude

Using the NPI Registry Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-npi-registry-connector-in-claude)Tutorial
