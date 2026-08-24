<!-- source: https://academy.claude.com/use-cases/week-ahead-prep -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Prep call look-ahead

Agendas and context for every meeting next week.

10 minClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-c17k7zsz.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-hmn3kocy.png)

## Set up

### Try a plugin

The Productivity plugin ships with `/start` and other personal-planning skills as a starting point, already structured to walk a calendar and gather context per event. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Productivity6 skills for inbox sweeps, daily rundowns, meeting prep, and decision logs

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=productivity)

`/start`Walk next week's calendar and write a context-and-agenda brief per meeting

[Run](claude://cowork/new?q=%2Fstart)

`/task-management`Track the prep tasks and owners that fall out of the week-ahead

[Run](claude://cowork/new?q=%2Ftask-management)

Show all 4 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20width='48'%20height='48'%20viewBox='0%200%2048%2048'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M31.3678%2016.6324L24.7365%2015.8956L16.6315%2016.6324L15.8945%2024.0006L16.6313%2031.3688L23.9996%2032.2899L31.3678%2031.3688L32.1046%2023.8165L31.3678%2016.6324Z'%20fill='white'/%3e%3cpath%20d='M19.6541%2028.0627C19.1033%2027.6906%2018.722%2027.1472%2018.5138%2026.4288L19.7922%2025.902C19.9083%2026.3441%2020.1109%2026.6867%2020.4001%2026.9298C20.6875%2027.173%2021.0375%2027.2927%2021.4464%2027.2927C21.8646%2027.2927%2022.2238%2027.1656%2022.524%2026.9114C22.8241%2026.6571%2022.9753%2026.3329%2022.9753%2025.9406C22.9753%2025.5391%2022.8168%2025.2111%2022.5%2024.957C22.1832%2024.7029%2021.7853%2024.5757%2021.3101%2024.5757H20.5714V23.3103H21.2345C21.6434%2023.3103%2021.9879%2023.1998%2022.2679%2022.9787C22.5479%2022.7577%2022.6879%2022.4556%2022.6879%2022.0706C22.6879%2021.728%2022.5626%2021.4553%2022.3121%2021.2509C22.0617%2021.0465%2021.7447%2020.9434%2021.3598%2020.9434C20.984%2020.9434%2020.6855%2021.0429%2020.4645%2021.2436C20.2434%2021.4444%2020.0831%2021.6912%2019.9819%2021.9823L18.7165%2021.4555C18.8841%2020.9802%2019.1918%2020.5602%2019.643%2020.1973C20.0943%2019.8345%2020.6708%2019.652%2021.3708%2019.652C21.8884%2019.652%2022.3544%2019.7516%2022.7671%2019.9523C23.1797%2020.1531%2023.5039%2020.4313%2023.7379%2020.7849C23.9718%2021.1403%2024.0878%2021.5383%2024.0878%2021.9803C24.0878%2022.4316%2023.9792%2022.8129%2023.7618%2023.126C23.5444%2023.4392%2023.2773%2023.6786%2022.9605%2023.8463V23.9218C23.3786%2024.0968%2023.7194%2024.3639%2023.9883%2024.7231C24.2554%2025.0823%2024.3898%2025.5115%2024.3898%2026.0126C24.3898%2026.5136%2024.2627%2026.9612%2024.0085%2027.3536C23.7542%2027.746%2023.4024%2028.0554%2022.9567%2028.2801C22.5091%2028.5048%2022.0063%2028.619%2021.4481%2028.619C20.8016%2028.6208%2020.2048%2028.4348%2019.6541%2028.0627Z'%20fill='%231A73E8'/%3e%3cpath%20d='M27.4998%2021.7203L26.1035%2022.7353L25.4017%2021.6706L27.9198%2019.8543H28.8851V28.4216H27.4998V21.7203Z'%20fill='%231A73E8'/%3e%3cpath%20d='M31.3684%2038.0006L37.9997%2031.3693L34.6841%2029.8958L31.3684%2031.3693L29.8948%2034.685L31.3684%2038.0006Z'%20fill='%23EA4335'/%3e%3cpath%20d='M15.1578%2034.6838L16.6314%2037.9994H31.3677V31.3681H16.6314L15.1578%2034.6838Z'%20fill='%2334A853'/%3e%3cpath%20d='M12.2104%2010C10.9892%2010%2010%2010.9892%2010%2012.2104V31.3676L13.3156%2032.8412L16.6313%2031.3676V16.6313H31.3676L32.8412%2013.3156L31.3678%2010H12.2104Z'%20fill='%234285F4'/%3e%3cpath%20d='M10%2031.3681V35.789C10%2037.0103%2010.9892%2037.9994%2012.2104%2037.9994H16.6313V31.3681H10Z'%20fill='%23188038'/%3e%3cpath%20d='M31.3685%2016.6311V31.3674H37.9998V16.6311L34.6841%2015.1575L31.3685%2016.6311Z'%20fill='%23FBBC04'/%3e%3cpath%20d='M37.9998%2016.6313V12.2104C37.9998%2010.9891%2037.0106%2010%2035.7894%2010H31.3685V16.6313H37.9998Z'%20fill='%231967D2'/%3e%3c/svg%3e)

Google Calendar

[Connect](https://claude.ai/desktop/directory/google-calendar-calendarmcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20width='48'%20height='48'%20viewBox='0%200%2048%2048'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_4766_38693)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)

Gmail

[Connect](https://claude.ai/desktop/directory/gmail-gmailmcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google DriveOptional

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Create a `Week-of-<date>` folder and point Cowork at it. The week-ahead doc, each meeting's agenda, and any prep notes you add through the week land there together. If you run this every week, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the parent folder so your agenda format and prep preferences stay attached.

Planning / Week-of-2026-04-27

week-ahead.mdApr 26, 20269 KB

staff-meeting-agenda.docxApr 26, 202614 KB

open-items-carryover.mdApr 24, 20262 KB

In Cowork’s chat bar:Planning / Week-of-2026-04-27

## The prompt

### Copy this into Claude Cowork

Look at my calendar for next week. For each meeting, pull the context: the last time we met, related Slack threads, attached or mentioned docs, and open items I owe them. Draft a one-paragraph agenda for each and flag the three I most need to prep for. Write it all to a single week-ahead doc for Sunday night.

Planning / Week-of-2026-04-27Open in Cowork

### Why this works

Source

**List the sources to pull from.** Listing "last time we met, related Slack threads, attached docs, open items I owe" tells Cowork exactly which sources to chase per meeting, so the brief is grounded rather than generic.

Prompt

**Ask which ones matter most.** "Flag the three I most need to prep for" makes Cowork commit to a priority call instead of treating every meeting as equal weight.

Prompt

**Ask for one combined output.** "Write it all to a single week-ahead doc" gives you something you can read top to bottom on Sunday instead of clicking through a folder of files.

Source

**Send output to a folder you'll reuse.** The Week-of folder is where the briefing, the agendas, and your own notes accumulate through the week, so Friday's retro can read straight from it.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /start skill with my feedback.

PlanningOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it every Sunday at 5pm

The briefing should be waiting before the week starts. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs every Sunday afternoon and writes to a fresh Week-of folder.

**/schedule** Run /start every Sunday at 5:00pm, create a Week-of-<next-monday> folder under Planning, and write the week-ahead doc and per-meeting agendas there.

PlanningOpen in Cowork

Scheduled taskActive

Week-ahead chief of staff

Runs `/start` against Calendar, Slack, Gmail, and Drive and writes the briefing and agendas to a new Week-of folder.

Every **Sunday at 5:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/start` now carries your skip list, your prep tiers, and your agenda format. Share it so your directs and your EA produce briefings in the same shape, and anyone covering for you walks into Monday with the same context you would.

Share the skill

In Cowork, open **Skills** → `/start` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your agenda format and prep tiers baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Productivity plugin

Your tools

![](data:image/svg+xml,%3csvg%20width='48'%20height='48'%20viewBox='0%200%2048%2048'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M31.3678%2016.6324L24.7365%2015.8956L16.6315%2016.6324L15.8945%2024.0006L16.6313%2031.3688L23.9996%2032.2899L31.3678%2031.3688L32.1046%2023.8165L31.3678%2016.6324Z'%20fill='white'/%3e%3cpath%20d='M19.6541%2028.0627C19.1033%2027.6906%2018.722%2027.1472%2018.5138%2026.4288L19.7922%2025.902C19.9083%2026.3441%2020.1109%2026.6867%2020.4001%2026.9298C20.6875%2027.173%2021.0375%2027.2927%2021.4464%2027.2927C21.8646%2027.2927%2022.2238%2027.1656%2022.524%2026.9114C22.8241%2026.6571%2022.9753%2026.3329%2022.9753%2025.9406C22.9753%2025.5391%2022.8168%2025.2111%2022.5%2024.957C22.1832%2024.7029%2021.7853%2024.5757%2021.3101%2024.5757H20.5714V23.3103H21.2345C21.6434%2023.3103%2021.9879%2023.1998%2022.2679%2022.9787C22.5479%2022.7577%2022.6879%2022.4556%2022.6879%2022.0706C22.6879%2021.728%2022.5626%2021.4553%2022.3121%2021.2509C22.0617%2021.0465%2021.7447%2020.9434%2021.3598%2020.9434C20.984%2020.9434%2020.6855%2021.0429%2020.4645%2021.2436C20.2434%2021.4444%2020.0831%2021.6912%2019.9819%2021.9823L18.7165%2021.4555C18.8841%2020.9802%2019.1918%2020.5602%2019.643%2020.1973C20.0943%2019.8345%2020.6708%2019.652%2021.3708%2019.652C21.8884%2019.652%2022.3544%2019.7516%2022.7671%2019.9523C23.1797%2020.1531%2023.5039%2020.4313%2023.7379%2020.7849C23.9718%2021.1403%2024.0878%2021.5383%2024.0878%2021.9803C24.0878%2022.4316%2023.9792%2022.8129%2023.7618%2023.126C23.5444%2023.4392%2023.2773%2023.6786%2022.9605%2023.8463V23.9218C23.3786%2024.0968%2023.7194%2024.3639%2023.9883%2024.7231C24.2554%2025.0823%2024.3898%2025.5115%2024.3898%2026.0126C24.3898%2026.5136%2024.2627%2026.9612%2024.0085%2027.3536C23.7542%2027.746%2023.4024%2028.0554%2022.9567%2028.2801C22.5091%2028.5048%2022.0063%2028.619%2021.4481%2028.619C20.8016%2028.6208%2020.2048%2028.4348%2019.6541%2028.0627Z'%20fill='%231A73E8'/%3e%3cpath%20d='M27.4998%2021.7203L26.1035%2022.7353L25.4017%2021.6706L27.9198%2019.8543H28.8851V28.4216H27.4998V21.7203Z'%20fill='%231A73E8'/%3e%3cpath%20d='M31.3684%2038.0006L37.9997%2031.3693L34.6841%2029.8958L31.3684%2031.3693L29.8948%2034.685L31.3684%2038.0006Z'%20fill='%23EA4335'/%3e%3cpath%20d='M15.1578%2034.6838L16.6314%2037.9994H31.3677V31.3681H16.6314L15.1578%2034.6838Z'%20fill='%2334A853'/%3e%3cpath%20d='M12.2104%2010C10.9892%2010%2010%2010.9892%2010%2012.2104V31.3676L13.3156%2032.8412L16.6313%2031.3676V16.6313H31.3676L32.8412%2013.3156L31.3678%2010H12.2104Z'%20fill='%234285F4'/%3e%3cpath%20d='M10%2031.3681V35.789C10%2037.0103%2010.9892%2037.9994%2012.2104%2037.9994H16.6313V31.3681H10Z'%20fill='%23188038'/%3e%3cpath%20d='M31.3685%2016.6311V31.3674H37.9998V16.6311L34.6841%2015.1575L31.3685%2016.6311Z'%20fill='%23FBBC04'/%3e%3cpath%20d='M37.9998%2016.6313V12.2104C37.9998%2010.9891%2037.0106%2010%2035.7894%2010H31.3685V16.6313H37.9998Z'%20fill='%231967D2'/%3e%3c/svg%3e)Google Calendar![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)Slack![](data:image/svg+xml,%3csvg%20width='48'%20height='48'%20viewBox='0%200%2048%2048'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_4766_38693)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)Gmail![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive

Your workspace

Week-of-<date>

Every meeting on next week's calendar has its context gathered and an agenda drafted in one document, with the ones needing real preparation flagged. `/start` produces it the same way each week.

[Next: My voice skill](https://academy.claude.com/use-cases/my-voice)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
