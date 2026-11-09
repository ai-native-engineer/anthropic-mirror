<!-- source: https://claude.com/customers/mid-ohio-food-collective -->

Case Study

# Mid-Ohio Food Collective rebuilds the software behind 2,500 food pantries with Claude

[Try Claude](https://claude.ai)

![Mid-Ohio Food Collective logo](https://assets.claude.com/a4f5b421b8bc247c633aa9d91942f5aa4ac01734.svg)

Industry:
:   Nonprofit

Company size:
:   Large

Product:
:   [Claude Tag](https://claude.com/product/tag)[Claude Design](https://claude.com/product/design)[Claude Platform](https://claude.com/platform/api)

Location:
:   North America

24 to 36 hours from idea to production

for new features across the FreshTrak platform, down from two to three months

35,000 families a day

served through FreshTrak nationwide, more than 12.5 million household visits a year

Mid-Ohio Food Collective is Ohio’s largest food bank, serving a 20-county region across central and eastern Ohio through more than 500 partner agencies and programs. It is also, less visibly, a software maker. Its platform, FreshTrak, runs at some 2,500 pantries, soup kitchens, shelters and food banks across the country, where it has logged 68 million visits since launch. To keep pace, the Food Collective runs one of the largest software and data teams in the charitable food system, and that team builds with Claude Code, Claude Tag, Claude Design, and the Claude Developer Platform.

## With Claude, Mid-Ohio Food Collective:

* Ships new features from idea to production in 24 to 36 hours, down from two to three months.
* Serves 35,000 families a day on average through FreshTrak nationwide
* Rebuilt FreshTrak from a pantry check-in system into a platform neighbors use directly: a mobile app to find food, create a profile, reserve a visit at participating pantries, and get nutrition guidance, healthy recipes, health referrals and the other assistance they qualify for
* Cut onboarding and training time for partner food banks by 50%, and is now bringing on five more of the country’s largest food banks
* Put a technical support team member’s first pull request into production in under 12 hours, working through Slack
* Built a new design system and modern UI for all of its applications with Claude Design
* Turned a business analyst’s food bank visit into a working prototype over one weekend, starting with a Claude voice mode conversation on his drive home
* Keeps leadership current on agricultural, economic, regulatory and environmental trends through a recurring research environment built on the Claude Developer Platform

## The challenge

## Serving more people with less food

Food banks have always depended on surplus. For decades, the food that grocers and manufacturers could not sell flowed to regional food banks, and from there to the pantries that serve families directly. That flow is shrinking. “As grocers get better at supply chain management and demand forecasting, some of the supply that used to end up at food banks is captured before it reaches us,” explained Nick Davis, Chief Innovation Officer at Mid-Ohio Food Collective.

The drop in donated pounds has arrived at a difficult moment. In the Food Collective’s central and eastern Ohio service area, changes to SNAP and disruptions to federal and state funding have landed while the number of people asking for help has nearly doubled compared to before the pandemic. With less food and more need, the Food Collective has had to become more precise about where each item goes. “Right food, right time, right place, right service,” Davis said. “We have to get the right unit of food, that individual item, to the right person exactly when they need it, so we can get them stabilized as fast as we can.”

A pantry visit is usually a symptom of something else, a lost shift, a medical bill, a rent increase, and food alone does not fix it. So the Food Collective works to connect households with the services and supports that help them regain stability, and to reduce how long they need charitable food assistance. Doing that depends on knowing more about each household than that they visited a pantry, and on connecting them to housing, health and benefits support.

Mark Mollenkopf, Director of Software Engineering, built FreshTrak to manage these assessments. In the 17 years since its first iteration, FreshTrak has become the system on the pantry side of the desk, there to record a visit so every neighbor is welcomed with the same consistency and clarity, and never has to repeat information they have already shared. But the team has been limited by bandwidth when trying to improve and expand the software. “Nick and I have been in rooms with those big post-it notes on the wall, dot voting on ideas, for almost a decade,” he said. “We could only ever go after a fraction of them, because there was time, there was money, there was knowledge. Hundreds of them are rolled up in cardboard tubes in the corner of my office.”

Taking the platform to other food banks at scale was the largest of those unbuilt ideas. Every food bank is its own organization, and every state has its own regulations for federal food programs like TEFAP and CSFP, so each deployment meant adapting the software by hand. “There’s an adage in our world, if you’ve seen one food bank, you’ve seen one food bank,” Davis said. “Until AI, that made it extremely difficult to scale to the next state or the next location.”

## The solution

## Building FreshTrak, and the tools around it, with Claude

The Food Collective’s engineers tried several AI tools and over the past six months found that most of the organization had settled on Claude. “I haven’t sent Mark an approval for one of the other tools in months,” Davis said. “As the institution gets better at being on the same tool, we’re learning tricks and trades we can share, which accelerates our own capability to deploy it.”

The deciding moment was a state-rules problem. Every state that adopts FreshTrak brings its own eligibility logic, reporting formats and consent language, and adapting to each one had always been done by hand. Given the full FreshTrak codebase and a new state’s regulations, Claude Code produced a working, tested implementation that respected how the platform was already built. The Food Collective’s engineers and local program staff still own the content expertise and the relationships with state agencies: they interpret each requirement, review every rule Claude implements against the state’s guidance, and sign off before anything ships. “Other tools could write a function,” Davis said. “Claude understood the whole system. It read our code the way a senior engineer who had been here for years would read it, and it was willing to be reviewed, challenged and sent back.”

Claude is now part of how the whole engineering team works. Engineers brief Claude Tag in Slack, and it works through the FreshTrak codebase, opens a pull request, and takes the team through rounds of review before anything reaches the CI/CD pipeline. Claude Code is where engineers do the deeper work: larger refactors, migrations and multi-service changes. Nothing merges without a human engineer’s approval, passing automated tests, and at least one round of Claude-assisted code review on the pull request.

Much of that deeper work is modernization. FreshTrak’s codebase goes back more than 15 years, and Claude Code is how the team is bringing it forward. “We’ve been using Claude Code to help us refactor our legacy code base. That goes back fifteen-plus years, and we’re now modernizing it with new levels of access, security, and an enhanced user interface,” Mollenkopf said.

That new interface is being designed with Claude too. The team uses Claude Design to combine its UI partners’ Figma designs with requirements gathered in customer interviews and is turning the result into a single design system for every FreshTrak application. “We’re now building our own design system and modern UI for all of our applications using Claude’s support,” Mollenkopf said. “Converting Figma to a design system has enabled us to accelerate what we’re doing on our new application.”

Claude Tag has opened the codebase to people who never expected to work in it. A technical support team member, set up on Claude Tag and talked through her first task by phone, had a pull request waiting in Slack by the time Mollenkopf got home, and it went to production the next day. “She’s not an engineer. She is now,” Mollenkopf said. “That’s why she wanted to be on our team.” The rest of the support team uses Claude chat the same way when something unusual breaks, asking Claude to look through the codebase for the likely cause, which gets them to the source of an issue faster.

### Beyond FreshTrak

FreshTrak was the first focus for the team. With Claude, the team has refactored it into a platform neighbors use directly. The FreshTrak mobile app, launching this fall, puts it in a neighbor’s pocket. Someone can find open pantries near them, create a profile once, reserve a visit at participating pantries, and arrive with their check-in already done. The team used Claude to build the app’s neighbor-facing flows and the APIs that feed it. Next is agentic verification, a planned use of the Claude Developer Platform in which Claude confirms pantry hours directly with agencies, so a family is never sent to a closed door.

The same rebuild connected the pantry to the clinic. Through FreshTrak Health, the platform behind the Mid-Ohio Farmacy program, providers at partner health systems screen patients for food insecurity and refers them to the Food Collective while linking to their electronic health record. With Claude, the team built the integration that carries that referral into FreshTrak, enrolls the patient, records every Farmacy visit, and sends the outcome back to the care team. The team also built, in a matter of weeks, a self-sufficiency assessment that case managers record in the same system: a picture of a household’s housing, income and health needs beyond the food visit. Health plan partners can now see whether a referral became a visit, and whether a visit became a healthier patient.

### Empowering the entire team to build

Staff outside engineering prototype with Claude on their own and hand working ideas to the engineering team to ship. The Food Collective’s Director of Research and Nutrition built a feature that lets someone photograph what is in their refrigerator and pantry and get back healthy recipes they can make tonight with what they already have. Engineering took her prototype to production in days.

Much of that prototyping now starts as a conversation. “One of the game-changing uses of Claude for me and members of my team has been using Claude in voice mode to have a two-way conversation on a particular topic,” Mollenkopf said. He uses voice mode to work through infrastructure, architecture and pipeline options, and the team’s business analysts use it to turn what they see in the field into prototypes. “Our business analyst spent several hours at a food bank in northeast Ohio, and on his two-and-a-half-hour drive home, he had a Claude conversation. By Monday morning, he had a working prototype to send to me.”

The Claude Developer Platform keeps the Food Collective looking outward, too. One developer built a recurring research environment on the Claude API that scans news and publications for anything that could affect food banking: crop losses and overproduction of particular crops; economic conditions for the people the Food Collective serves, such as fuel and utility prices; regulatory changes in Ohio, or in other states, that could spill over into its work; and environmental and technology changes. “We use the APIs to help us do that fundamental research on a recurring basis so we can stay current and keep our leadership team current on conditions that could be affecting the neighbors we serve,” Mollenkopf said.

> “Everything we’ve dreamed of for the last 15 years is on those post-it notes. Now, if I can have a conversation with someone and put it into Claude on my drive home, we’re off and running.”

Mark MollenkopfDirector of Software Engineering, Mid-Ohio Food Collective

## The outcome

## What it has meant for neighbors and partner food banks

FreshTrak now serves 35,000 families a day on average across the country, more than 12.5 million household visits a year, and those visits are no longer just a count. Every neighbor who arrives through a physician’s referral is enrolled in the food Farmacy before they walk in. Every household that sits down with a benefits or neighbor services staff member can be assessed across housing, income and health. The mobile app will give families a way to find food, reserve a visit at participating pantries, and get recipes and referrals without filling out a form at a folding table. The Food Collective is also exploring ways to track households from their first visit through the services and supports they receive, helping identify which interventions most effectively and quickly restore family stability.

The platform is also reaching more food banks beyond the 22 it already serves. The Food Collective has launched the new version of FreshTrak live with expanded deployments across the country, with several new food banks in the process of onboarding currently. Onboarding and training time has fallen by half since the team started building with Claude, because the state-specific adaptation that once took months of hand work now takes days. In Houston, where the food bank serves roughly 1,600 partner agencies across 18 counties, the Food Collective mapped the food bank’s entire neighbor-services model against FreshTrak in a single working session and left with a 90-day build plan. “We know this work well. We know how to build the solutions for it. We just couldn’t have taken it everywhere so quickly,” Davis said. “Now we can.”

The next build is for neighbors themselves. The FreshTrak mobile app will carry an assistant built on the Claude Developer Platform. It will help someone who needs housing, rent, food and childcare assistance to find the right resources in their own language and understand what each program asks of them. Helping neighbors prepare paperwork for programs such as SNAP, Medicaid, housing and utility assistance is a future capability the team is working to build, test and validate, in partnership with the agencies involved, to see whether it works and belongs in the platform. The assistant will also coordinate care with partners through the Food Collective’s 211 and housing data connections. The local pilot, specific to central Ohio, is being scoped now, with the hope of helping families regain stability more quickly.

For Mollenkopf, the measure of all of it is the same as it was on his first day in a pantry. “The idea that we can achieve the things that were never achievable, that I can feed more people, find more food, help more people,” he said. “That’s a big thing.”

“Hunger is an income and root cause problem, and software is how we get at the problem one household at a time,” Davis said. “Claude did not change what we believe. It changed how fast we can act on it.”

> “The idea that we can achieve the things that were never achievable, that I can feed more people, find more food, help more people. That’s a big thing.”

Mark MollenkopfDirector of Software Engineering, Mid-Ohio Food Collective

[![Montgomery County Food Bank](https://assets.claude.com/07a7c659a67267cb5cdc870284f7b3c7c4bdb6dd.svg)

### Montgomery County Food Bank extends a small team’s reach across the county with Claude](https://claude.com/customers/montgomery-county-food-bank)[![IRC (Rescue)](https://assets.claude.com/e63d6d26bb5c35a117de419a1a7a8452f081db25.svg)

### A conversation with IRC on turning frontline health data into action in Burkina Faso](https://claude.com/customers/irc-qa)[![IRC (Rescue)](https://assets.claude.com/e63d6d26bb5c35a117de419a1a7a8452f081db25.svg)

### The International Rescue Committee turns fragmented health data into faster decisions with Claude](https://claude.com/customers/irc)
