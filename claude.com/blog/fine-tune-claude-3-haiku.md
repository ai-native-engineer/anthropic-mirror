<!-- source: https://claude.com/blog/fine-tune-claude-3-haiku -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d227246bc2b5a3cc3626_9f6a378a1e3592cf8d27447457409ba12284faef-1000x1000.svg)

# Fine-tune Claude 3 Haiku in Amazon Bedrock

Claude 3 Haiku can now be fine-tuned in Amazon Bedrock with custom training data, enabling faster, more accurate performance at lower cost.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Platform](https://claude.com/platform/api)
* Date

  July 10, 2024
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/fine-tune-claude-3-haiku

![Graph showing fine-tuning with Claude 3 Haiku](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9554e6002385ccd593_aaf4aaf19584a566ab3687e64cd31da018b17b44-2880x1620.png)

***Update:*** *Fine-tuning Claude 3 Haiku in Amazon Bedrock is generally available. (November 1, 2024)*

Customers can now fine-tune Claude 3 Haiku—our fastest and most cost-effective model—in [Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) to customize its knowledge and capabilities for their business, making the model more effective for specialized tasks.

## Overview of fine-tuning

Fine-tuning is a popular technique to improve model performance. By creating a customized version of the model, you can train the model to excel at highly tailored workflows.

To fine-tune Claude 3 Haiku, you first prepare a set of high quality prompt-completion pairs—the ideal outputs that you want Claude to provide for a given task. The fine-tuning API, now available in preview, will use your data to create your own custom Claude 3 Haiku. Using the Amazon Bedrock console or API, you can test and refine your custom Claude 3 Haiku model until it meets your performance goals and is ready for deployment.

## Benefits

Fine-tuning allows you to customize Claude 3 Haiku so it can acquire specialized business knowledge, leading to improved accuracy and consistency. Benefits include:

* **Better results on specialized tasks**: Enhance performance for domain-specific actions such as classification, interactions with custom APIs, or industry-specific data interpretation. Fine-tuning allows Claude 3 Haiku to excel in areas crucial to your business compared to more general models by encoding company and domain knowledge.
* **Faster speeds at lower cost**: Reduce costs for production deployments where Claude 3 Haiku can be used in place of Sonnet or Opus, while also returning results faster.
* **Consistent, brand-aligned formatting**: Generate consistently structured outputs tailored to your exact specifications like standardized reports or custom schemas, ensuring compliance with regulatory requirements and internal protocols.
* **Easy-to-use API**: Companies of all sizes can innovate efficiently without extensive in-house AI expertise or resources. Anyone can fine-tune models seamlessly, no deep technical expertise required.
* **Safe and secure**: Proprietary training data remains within customers’ AWS environment. Anthropic’s fine-tuning technique preserves the Claude 3 model family’s low risk of harmful outputs.

We fine-tuned Haiku to moderate online comments on internet forums1, including identifying insults, threats, and explicit content. Fine-tuning improved classification accuracy from 81.5% to 99.6% while reducing tokens per query by 85%.

![Graph illustrating fine-tuning on Claude 3 Haiku](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9454e6002385ccd587_7e7063ef5b33399cf7f891b43b343ab2692a2e14-2200x1936.png)

## Customer spotlight

[SK Telecom](https://www.claude.com/customers/skt), one of the largest telecommunications operators in South Korea, trained a custom Claude model to improve support workflows and enable better customer experiences by leveraging their industry-specific expertise.

"Embedding a fine-tuned Claude in our customer support operations has measurably improved our internal processes and overall customer satisfaction. **By customizing Claude, we've seen a 73% increase in positive feedback for our agents' responses and a 37% improvement in key performance indicators for telecommunications-related tasks**. The fine-tuned model now efficiently generates topics, action items, and summaries from customer call logs, and breaks down complex customer issues into manageable steps for better problem-solving," said Eric Davis, Vice President, AI Tech Collaboration Group.

[Thomson Reuters](https://www.claude.com/customers/thomson-reuters), a global content and technology company, has seen positive results with Claude 3 Haiku. The company, which serves professionals in legal, tax, accounting, compliance, government, and media, anticipates even faster and more relevant AI results by fine-tuning Claude with their industry expertise.

“We are excited to fine-tune Anthropic’s Claude 3 Haiku model in Amazon Bedrock to further enhance our Claude-powered solutions. Thomson Reuters aims to provide accurate, fast, and consistent user experiences. By optimizing Claude around our industry expertise and specific requirements, we anticipate measurable improvements that deliver high-quality results at even faster speeds. **We’ve already seen positive results with Claude 3 Haiku, and fine-tuning will enable us to tailor AI assistance more precisely**,” said Joel Hron, Head of AI and Labs, Thomson Reuters.

## How to get started

Fine-tuning for Claude 3 Haiku in Amazon Bedrock is now available in preview in the US West (Oregon) AWS Region. At launch, we're supporting text-based fine-tuning with context lengths up to 32K tokens, with plans to introduce vision capabilities in the future. Additional details are available in the [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/) and [documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-supported.html).

To request access, contact your AWS account team or submit a support ticket in the [AWS Management Console](https://console.aws.amazon.com/bedrock/).

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90479f5433ec75978f1e8a_Object-Apple.svg)

Aug 28, 2026

### Claude for Teachers, now available for U.S. K-12 schools and districts

Product announcements

[Claude for Teachers, now available for U.S. K-12 schools and districts](#)Claude for Teachers, now available for U.S. K-12 schools and districts

[Claude for Teachers, now available for U.S. K-12 schools and districts](https://claude.com/blog/claude-for-teachers-now-available-for-schools-and-districts)Claude for Teachers, now available for U.S. K-12 schools and districts

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b8840b2f6f9a40fe0_8925ac952fa2cb8eb5e845b2e44f3e71b33fd695-1000x1000.svg)

Aug 26, 2026

### Claude gets its own browser in Cowork

Product announcements

[Claude gets its own browser in Cowork](#)Claude gets its own browser in Cowork

[Claude gets its own browser in Cowork](https://claude.com/blog/cowork-built-in-browser)Claude gets its own browser in Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

Aug 26, 2026

### Claude in Chrome is generally available

Product announcements

[Claude in Chrome is generally available](#) Claude in Chrome is generally available

[Claude in Chrome is generally available](https://claude.com/blog/claude-in-chrome-generally-available) Claude in Chrome is generally available

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 11, 2026

### Compliance API coverage extends to Claude Cowork and Claude Code

Enterprise AI

[Compliance API coverage extends to Claude Cowork and Claude Code](#)Compliance API coverage extends to Claude Cowork and Claude Code

[Compliance API coverage extends to Claude Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code)Compliance API coverage extends to Claude Cowork and Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Platform

Business
