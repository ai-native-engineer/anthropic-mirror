<!-- source: https://academy.claude.com/use-cases/morning-evening -->

Loading

## Set up

### Try a plugin

The Productivity plugin ships with `/start` and `/update` as a starting point, already structured to read your calendar and channels and rank what matters. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



Productivity6 skills for inbox sweeps, daily rundowns, meeting prep, and decision logs

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=productivity)

`/start`Read calendar, inbox, and channels and write a one-page start-of-day briefing

[Run](claude://cowork/new?q=%2Fstart)

`/update`Log what landed, what slipped, and queue tomorrow's opener

[Run](claude://cowork/new?q=%2Fupdate)

Show all 4 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20width='48'%20height='48'%20viewBox='0%200%2048%2048'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M31.3678%2016.6324L24.7365%2015.8956L16.6315%2016.6324L15.8945%2024.0006L16.6313%2031.3688L23.9996%2032.2899L31.3678%2031.3688L32.1046%2023.8165L31.3678%2016.6324Z'%20fill='white'/%3e%3cpath%20d='M19.6541%2028.0627C19.1033%2027.6906%2018.722%2027.1472%2018.5138%2026.4288L19.7922%2025.902C19.9083%2026.3441%2020.1109%2026.6867%2020.4001%2026.9298C20.6875%2027.173%2021.0375%2027.2927%2021.4464%2027.2927C21.8646%2027.2927%2022.2238%2027.1656%2022.524%2026.9114C22.8241%2026.6571%2022.9753%2026.3329%2022.9753%2025.9406C22.9753%2025.5391%2022.8168%2025.2111%2022.5%2024.957C22.1832%2024.7029%2021.7853%2024.5757%2021.3101%2024.5757H20.5714V23.3103H21.2345C21.6434%2023.3103%2021.9879%2023.1998%2022.2679%2022.9787C22.5479%2022.7577%2022.6879%2022.4556%2022.6879%2022.0706C22.6879%2021.728%2022.5626%2021.4553%2022.3121%2021.2509C22.0617%2021.0465%2021.7447%2020.9434%2021.3598%2020.9434C20.984%2020.9434%2020.6855%2021.0429%2020.4645%2021.2436C20.2434%2021.4444%2020.0831%2021.6912%2019.9819%2021.9823L18.7165%2021.4555C18.8841%2020.9802%2019.1918%2020.5602%2019.643%2020.1973C20.0943%2019.8345%2020.6708%2019.652%2021.3708%2019.652C21.8884%2019.652%2022.3544%2019.7516%2022.7671%2019.9523C23.1797%2020.1531%2023.5039%2020.4313%2023.7379%2020.7849C23.9718%2021.1403%2024.0878%2021.5383%2024.0878%2021.9803C24.0878%2022.4316%2023.9792%2022.8129%2023.7618%2023.126C23.5444%2023.4392%2023.2773%2023.6786%2022.9605%2023.8463V23.9218C23.3786%2024.0968%2023.7194%2024.3639%2023.9883%2024.7231C24.2554%2025.0823%2024.3898%2025.5115%2024.3898%2026.0126C24.3898%2026.5136%2024.2627%2026.9612%2024.0085%2027.3536C23.7542%2027.746%2023.4024%2028.0554%2022.9567%2028.2801C22.5091%2028.5048%2022.0063%2028.619%2021.4481%2028.619C20.8016%2028.6208%2020.2048%2028.4348%2019.6541%2028.0627Z'%20fill='%231A73E8'/%3e%3cpath%20d='M27.4998%2021.7203L26.1035%2022.7353L25.4017%2021.6706L27.9198%2019.8543H28.8851V28.4216H27.4998V21.7203Z'%20fill='%231A73E8'/%3e%3cpath%20d='M31.3684%2038.0006L37.9997%2031.3693L34.6841%2029.8958L31.3684%2031.3693L29.8948%2034.685L31.3684%2038.0006Z'%20fill='%23EA4335'/%3e%3cpath%20d='M15.1578%2034.6838L16.6314%2037.9994H31.3677V31.3681H16.6314L15.1578%2034.6838Z'%20fill='%2334A853'/%3e%3cpath%20d='M12.2104%2010C10.9892%2010%2010%2010.9892%2010%2012.2104V31.3676L13.3156%2032.8412L16.6313%2031.3676V16.6313H31.3676L32.8412%2013.3156L31.3678%2010H12.2104Z'%20fill='%234285F4'/%3e%3cpath%20d='M10%2031.3681V35.789C10%2037.0103%2010.9892%2037.9994%2012.2104%2037.9994H16.6313V31.3681H10Z'%20fill='%23188038'/%3e%3cpath%20d='M31.3685%2016.6311V31.3674H37.9998V16.6311L34.6841%2015.1575L31.3685%2016.6311Z'%20fill='%23FBBC04'/%3e%3cpath%20d='M37.9998%2016.6313V12.2104C37.9998%2010.9891%2037.0106%2010%2035.7894%2010H31.3685V16.6313H37.9998Z'%20fill='%231967D2'/%3e%3c/svg%3e)

Google Calendar

[Connect](https://claude.ai/desktop/directory/google-calendar-calendarmcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20width='48'%20height='48'%20viewBox='0%200%2048%2048'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_4766_38693)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)

Gmail

[Connect](https://claude.ai/desktop/directory/gmail-gmailmcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%20100%20100'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%235E6AD2'%20d='M1.225%2061.523c-.222-.949.908-1.546%201.597-.857l36.512%2036.512c.689.689.092%201.819-.857%201.597a50.06%2050.06%200%200%201-37.252-37.252Zm-1.22-13.59a.98.98%200%200%200%20.283.724l50.055%2050.055a.98.98%200%200%200%20.724.283%2049.9%2049.9%200%200%200%208.636-1.518.976.976%200%200%200%20.462-1.647L2.17%2038.835a.976.976%200%200%200-1.647.462%2049.9%2049.9%200%200%200-1.518%208.636Zm4.194-17.443a.988.988%200%200%200%20.184%201.152l63.975%2063.975a.988.988%200%200%200%201.152.184%2050.4%2050.4%200%200%200%206.08-3.495.993.993%200%200%200%20.161-1.53L9.224%2024.249a.993.993%200%200%200-1.53.161%2050.4%2050.4%200%200%200-3.495%206.08Zm9.723-13.067a.99.99%200%200%201-.026-1.377C23.068%206.08%2036.765-.002%2051.888-.002c27.59%200%2049.957%2022.367%2049.957%2049.957%200%2015.123-6.082%2028.82-16.048%2038.013a.99.99%200%200%201-1.377-.026z'/%3e%3c/svg%3e)

Linear

[Connect](https://claude.ai/desktop/directory/linear)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23000'%20d='M4.46%204.44c.74.6%201.02.56%202.42.46l13.18-.79c.28%200%20.05-.28-.05-.32l-2.19-1.58c-.42-.33-.98-.7-2.05-.6L2.99%202.53c-.46.05-.56.28-.37.46l1.84%201.45Zm.8%203.1v13.87c0%20.74.37%201.02%201.21.98l14.49-.84c.84-.05.93-.56.93-1.16V6.6c0-.6-.23-.93-.74-.88l-15.14.88c-.56.05-.75.33-.75.93Zm14.3.74c.1.42%200%20.84-.42.89l-.7.14v10.24c-.6.33-1.16.51-1.63.51-.74%200-.93-.23-1.49-.93l-4.56-7.16v6.93l1.44.33s0%20.84-1.16.84l-3.21.18c-.1-.18%200-.65.33-.74l.84-.23V9.98l-1.16-.1c-.1-.42.14-1.02.79-1.07l3.44-.23%204.75%207.25V9.42l-1.21-.14c-.1-.51.28-.88.74-.93l3.21-.18Z'/%3e%3c/svg%3e)

Notion

[Connect](https://claude.ai/desktop/directory/notion)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Create a `Daily` folder and point Cowork at it. Each morning briefing and evening wrap writes there as `YYYY-MM-DD.md`, so the evening run reads what the morning run set out to do, and Monday's briefing can look back over last week. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your priorities, mute list, and tone stay attached.

Daily

2026-04-28.mdApr 28, 20263 KB

2026-04-27.mdApr 27, 20264 KB

priorities.mdApr 20, 20261 KB

In Cowork’s chat bar:Daily

## The prompt

### Copy this into Claude Cowork

Run my morning briefing. Tell me what's on fire, what's due, who's waiting on me, and the three things I should do first. Keep it under a page. Tonight I'll ask you to run /update and you'll write the wrap: what got done, what slipped, and what tomorrow opens with.



DailyOpen in Cowork

### Why this works

Prompt

**Name the sections you want.** On fire, due, waiting on me, top three: a fixed shape you can scan in thirty seconds.

Prompt

**Set a length limit.** A briefing you'll actually read, not another inbox.

Prompt

**Connect each run to the next.** The wrap feeds tomorrow's briefing, so carry-over never drops.

Source

**Let prior runs supply the context.** Each run reads yesterday's file, so context compounds without you re-explaining.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /start skill with my feedback.



DailyOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it at 8am and 6pm

The briefing should be waiting when you sit down. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skills run on their own at the start and end of every workday.

**/schedule** Run /start every weekday at 8:00am and /update every weekday at 6:00pm, both writing to Daily/<today>.md.



DailyOpen in Cowork

Scheduled taskActive

Daily bookends

Runs `/start` at 8am and `/update` at 6pm against Calendar, Slack, and Gmail and appends both to today's file in Daily.

Every **weekday at 8:00am and 6:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/start` and `/update` now carry your channel list, your priority rules, and your tone. Share them so anyone on your team starts and ends the day with the same one-page rhythm, and nobody's asking "what did I miss" in standup.



Share the skill

In Cowork, open **Skills** → `/start` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your buckets and mute list baked in, so they don't repeat Steps 1-3.

## What changes for your day

You have a one-page briefing ready each morning and an end-of-day record of what got done and what carries over. Open items continue from one day's file to the next without you tracking them.

You did this for the daily briefing. The same approach covers a weekly look-ahead, pre-meeting briefs, and project status checks — each one becomes a skill in your team's shared set.

[Next: Prep call look-ahead](https://academy.claude.com/use-cases/week-ahead-prep)
