<!-- source: https://claude.com/customers/irc-qa -->

Q&A | Claude Enterprise

# A conversation with IRC on turning frontline health data into action in Burkina Faso

[Try Claude](https://claude.ai)

![IRC (Rescue) logo](https://assets.claude.com/e63d6d26bb5c35a117de419a1a7a8452f081db25.svg)

Industry:
:   Nonprofit

Company size:
:   Large

Product:
:   Claude Enterprise

Location:
:   North America

2,700+

health facilities across 40 countries

20 minutes

to create HTML dashboards in Claude

The International Rescue Committee (IRC) delivers health care and humanitarian aid in some of the hardest places to work, serving 16.8 million people annually through more than 2,700 health facilities in 40 countries. Kristy Crabtree, the IRC’s global lead of technology for programs, has spent 15 years at the organization working where humanitarian programs and technology meet. We spoke with her about a pilot in Burkina Faso that uses Claude to turn inconsistent frontline health data into offline dashboards.

## Anthropic: As the IRC’s global lead for technology in programs, you describe yourself as an AI skeptic. How do those fit together?

**Kristy Crabtree, IRC:** As excited as I am about new technology, I start from a place of caution. My approach to any of these tools is, ‘Prove it to me.’ I don’t go into it thinking, ‘This is going to save us all.’ I needed to see the actual impact on our work for myself, and that’s what convinced me.

## Anthropic: You’ve been at the IRC for 15 years. What does “technology for programs” mean day to day?

**Crabtree:** The way IRC is structured, we have technical units at headquarters that drive our global practice areas: malnutrition, immunization, contraception, cash assistance, anticipatory action, early education, infectious disease control, violence prevention, social work and crisis. In Technology for Programs, we work with the global practice leads on priority projects that have identified some way that technology can help drive or deliver or measure or scale the program. This example in Burkina Faso came from a higher level need around visualization for our data across sub-Saharan Africa. We reached out to six different countries, and Burkina Faso was one of them. They were actually the ones that raised their hands first.

## Anthropic: For you, a lot of that proof came from a pilot in Burkina Faso. Give us the short version: what were you testing?

**Crabtree:** We did a pilot in Burkina Faso that was starting with our real world constraints and seeing where AI could address some of these challenges. We went into this truly as an experiment of saying, can Claude efficiently generate high quality visualizations of this data that’s in these inconsistent formats that we’re taking from tally sheets? Will people trust these visualizations? Can they use them in sites that have low or poor connectivity? And are they going to bring these visualizations into their decision-making around programs?

We really weren’t sure with any of those things how it was going to turn out, because it’s a pretty big change for folks. What we found was, even in the early weeks of the pilot, we started seeing really positive results, and I’d say results we weren’t expecting as well. And when you consider that nearly 3,000 health facilities across sub-Saharan Africa face the same data challenge, what works in Burkina Faso has the potential to change how health teams across the region use data.

## Anthropic: What makes frontline health data so hard to work with in the places where the IRC operates?

**Crabtree:** The ministries of health in different countries are organized in different ways, some more top down, and some more local. What they decide to track could be static, or it could change rapidly depending on who’s in leadership at a local, subnational, or national level. So even within a country, there’s no chance for IRC to change all of the indicators the Ministry of Health is deciding to collect or their means for collecting the data.

## Anthropic: Where does that data live before it reaches your team?

**Crabtree:** Because of electricity issues, connectivity issues, and lack of resourcing, especially in sub-Saharan Africa, a lot of data often goes into a register. A register is just a paper notebook that holds aggregate numbers from that health facility. They might record things like: “We served four children in the zero-to-two age group with malnutrition treatment.” Our staff will then go into the facility and transfer that information to Excel. It’s all a very manual process, and the staff doesn’t have time to develop unique visualizations for each of these sites on a regular, recurring basis.

## Anthropic: Why did this feel like the right problem for AI?

**Crabtree:** We really want data to drive our decisions. And yet to utilize this data, there are significant barriers. It’s unique to each facility, it could change at any moment, and the scale of this challenge is significant. It’s close to 23,000 healthcare facilities in sub-Saharan Africa that have the same problem. We want to take action based on data, but the scale of the data problem made that insurmountable until AI was an opportunity.

## Anthropic: Walk me through what you actually built.

**Crabtree:** We wanted to test if we could make a custom visualization template that could be applied at a facility level and modified at a facility level by someone with no coding or engineering experience, just a measurement specialist. How can we just change the visualization as one variable in this process? We asked Burkina Faso to come up with indicators that they are commonly tracking.

We worked on a visualization template with the team, which became just an HTML dashboard. For us to create an HTML dashboard would normally have required engineers involved in the process. It would have been costly. We just wouldn’t have gone down that road. And we don’t have connectivity in a lot of these settings, so we can’t build a fancy dashboard that requires the internet. The beautiful thing about the HTML is it’s a super light file that I can send to a facility manager. Then they can take their Excel file from that local facility and just drag and drop it in there. No connectivity needed.

And we just did it in the chat. We didn’t even need Claude Code, that’s the amazing thing. Once you have the base HTML file, making changes is a quick process you can just do with natural language.

> “We want to take action based on data, but the scale of the data problem made that insurmountable until AI was an opportunity.”

Kristy CrabtreeGlobal Lead of Technology for Programs, IRC

## Anthropic: What surprised you about how the teams responded?

**Crabtree:** Normally with these kinds of tech projects it would require a lot more coaching. But in this case, they just took this template that myself and the Regional Measurement Advisor made and ran with it because of the ease of use. They said things like: “I want to change this, and I actually just did it myself.” They came up with better ideas because they’re health professionals working with measurement professionals. They started to track things like targets versus actuals, and associated grants, which is not something I would have normally tracked on my own.

The quality of the visualizations also made it easier for non-measurement staff like health professionals to engage with the information, instead of the pivot table. Having these visualizations that they were able to adjust and adapt over time made it so they could have better discussions about the data than they had ever had before.

## Anthropic: What results are you seeing so far?

**Crabtree:** The Burkina Faso team wants to continue using this, and I think might protest if we refused, because they’re already taking action based on the visualizations. For example, the health team was able to see this visualization really quickly and speak with the truly frontline workers about what they were doing. It turns out, the frontline workers had already changed how they communicate about STI prevention and response with youth in health facilities. The dashboard surfaced the spike, and rather than this being a cause for alarm, the team was able to confirm that their modified outreach approach was actually working. More young people were coming in to seek services.

Both the nutrition and economic recovery teams want to do the same thing, just from word of mouth. This is trying to scale on its own.

We have traditionally always been worried about what if something doesn’t work out. Now we have to worry about what if something *does* work. AI adoption will spread organically, which is what you want, but it also brings up new governance questions. Banny Attiey, the Regional Measurement Advisor for the IRC leading the pilot in Burkina Faso, put it well: “Now that adoption seems to be moving so quickly, we’re focusing on how to better guide its use and ensure its security, reliability, and integrity.” That’s something we’re addressing both centrally and within our local programs.

> “We have traditionally always been worried about what if something doesn’t work out. Now we have to worry about what if something does work.”

Kristy CrabtreeGlobal Lead of Technology for Programs, IRC

## Anthropic: Why is data agility so crucial in humanitarian work specifically?

**Crabtree:** For us to get funding for a program, it takes a lot of advance planning. If we put out a proposal to do a mobile outreach program, we will do a mobile outreach program even if things change on the ground. But if we find out in real time that a community-based model for service provision would actually be more effective—because there was just a flood or a drought in this area that no one could have planned for—it can be difficult to pivot.

Everybody wants the whole industry to do more with less. Now more than any other time, while funding is so tight everywhere, the ability to be more flexible and more responsive to what the community needs is huge. The data allows us to make that decision, instead of a gut feeling.

## Anthropic: What would you tell other organizations trying to figure out where to start with AI?

**Crabtree:** There’s not a perfect place to start. Start with something that’s easy to measure or easy to know if it’s working well or not. We really understood the problem that Burkina Faso was having, and we still spent a majority of our time defining that problem; that actually took a lot more time than developing the dashboard. The dashboard was the easiest part of that process.

The other advice I’d give is where you can get a cross-functional team together, you will build something better than you would have built on your own. People will be bought into the process because they developed their own judgment as part of the process. I would suggest organizations think beyond the immediately shiny thing and think about the thing that’s annoying and painful for staff to do, because then it will allow them to do more of the stuff that they want to do.

## Anthropic: How should the sector be talking about AI?

**Crabtree:** Having these visualizations made for better health outcomes in Burkina Faso—that’s the story that we need to share. The STI prevention and response worked, and the reason we know it worked is because we had better visualizations, and we had better visualizations because we were able to address this really unique challenge that was also really huge at scale, in the data visualization. Instead of “AI did this thing,” it’s “health outcomes changed in this way, and AI was a part of that.”

[![IRC (Rescue)](https://assets.claude.com/e63d6d26bb5c35a117de419a1a7a8452f081db25.svg)

### The International Rescue Committee turns fragmented health data into faster decisions with Claude](https://claude.com/customers/irc)
