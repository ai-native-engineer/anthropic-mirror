<!-- source: https://support.claude.com/en/articles/16764810-assign-a-program-to-workspaces-in-claude-console -->

Anthropic offers several verification programs, such as the Cyber Verification Program, or access to models that might not be generally available. In order to gain access to these programs, go to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available to you, and apply.

Once you’ve applied and been approved for a program, Anthropic issues a “program” to your organization. In order for it to be used, you must assign it to a group of people within the organization. In the Claude Console, a program applies to workspaces, either automatically (for programs like the Cyber Verification Program) or by assignment.

This article covers how to enable programs for the Console.

## Before you start

* Your organization must already have a grant. Grants appear only after Anthropic issues one to your organization. To apply to a specific program, go to our **[Verification Portal](https://portal.anthropic.com/)** to see what programs are available.
* In the Console, you need to be an organization Admin. Other roles cannot view or manage grants.

## Give a Console workspace access

In the Console, programs are issued to your organization and apply to workspaces. Some programs, such as the Cyber Verification Program, apply automatically to every workspace that meets their requirements. Others need workspaces assigned. A program only applies to API traffic from workspaces that meet its requirements.

**Follow these steps:**

1. **[Sign in to the Console](https://platform.claude.com/)** as an organization Admin. Go to **[Organization settings > Programs](https://platform.claude.com/settings/organization/programs)**. The program card shows whether it applies automatically or needs workspaces assigned.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1790571600&signature=578af7a3004e40774f4e7c124a99b34c46d2d1e94b08213e148ad7a1a31214b0&req=diYjFM56mYRXXvMW1HO4zT%2FymUmCEwihktHcEoeKC4c9FhZWF8%2FGUkg9dJXl%0ALPim%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1790571600&signature=578af7a3004e40774f4e7c124a99b34c46d2d1e94b08213e148ad7a1a31214b0&req=diYjFM56mYRXXvMW1HO4zT%2FymUmCEwihktHcEoeKC4c9FhZWF8%2FGUkg9dJXl%0ALPim%0A)
2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1790571600&signature=4171fb2d513c65ca925f36a8351fc57514cd11379a1b88e8f72def2113245e4c&req=diYjFM56mIRZW%2FMW1HO4zc116w5tR1G3MCr%2B42fbmkbxhzDam8WwIKhWfHXi%0A3Np8%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1790571600&signature=4171fb2d513c65ca925f36a8351fc57514cd11379a1b88e8f72def2113245e4c&req=diYjFM56mIRZW%2FMW1HO4zc116w5tR1G3MCr%2B42fbmkbxhzDam8WwIKhWfHXi%0A3Np8%0A)

   Hover over the issue to see which requirement is not met.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1790571600&signature=a3590f22425dbc5ff093603820ecc07007027963bb13f7ff8a867fb228902976&req=diYjFM56m4VZX%2FMW1HO4zaveaOZnkXzGVPpeIJbmktRcVijgsZ7CWbrxmrzF%0AV97G%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1790571600&signature=a3590f22425dbc5ff093603820ecc07007027963bb13f7ff8a867fb228902976&req=diYjFM56m4VZX%2FMW1HO4zaveaOZnkXzGVPpeIJbmktRcVijgsZ7CWbrxmrzF%0AV97G%0A)
3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1790571600&signature=0cd3b7a34395dcc42ef5d5eef4159d6f0b856f6af7db4efffd8ae5e3b0044db2&req=diYjFM54lYBeXvMW1HO4zTU0lduVLEdB9BWcjfiNKI05yBYHorGsnpixBcC5%0AJ4jQ%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1790571600&signature=0cd3b7a34395dcc42ef5d5eef4159d6f0b856f6af7db4efffd8ae5e3b0044db2&req=diYjFM54lYBeXvMW1HO4zTU0lduVLEdB9BWcjfiNKI05yBYHorGsnpixBcC5%0AJ4jQ%0A)
4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1790571600&signature=b8111c09addf9d37d3378df4f57a4c85dc3a73506a2fe09f0792eb1420b23c67&req=diYjFM56m4hWXPMW1HO4zQfcHDur6H8t9apHi%2BiM8ogjfQW6YZy4K3neI07N%0AGLC0%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1790571600&signature=b8111c09addf9d37d3378df4f57a4c85dc3a73506a2fe09f0792eb1420b23c67&req=diYjFM56m4hWXPMW1HO4zQfcHDur6H8t9apHi%2BiM8ogjfQW6YZy4K3neI07N%0AGLC0%0A)
5. The program shows **Active** for the workspace.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1790571600&signature=9c0f7d5059c30236cdf735d56b00f8c8fe551b9137f085036471d0d2f956e8ef&req=diYjFM56moNfWfMW1HO4zaUR86Zi8f8%2BfTukdAE3MWvXiFS1w3oLjnv98roZ%0Ahj6j%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1790571600&signature=9c0f7d5059c30236cdf735d56b00f8c8fe551b9137f085036471d0d2f956e8ef&req=diYjFM56moNfWfMW1HO4zaUR86Zi8f8%2BfTukdAE3MWvXiFS1w3oLjnv98roZ%0Ahj6j%0A)

## Troubleshooting

* **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.
* **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.
* **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.
* **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.

* [Creating and managing Workspaces in the Claude Console](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console)
* [Claude Console roles and permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)
* [Real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)
* [Claude Team plan for scientists](https://support.claude.com/en/articles/16634237-claude-team-plan-for-scientists)
* [Turn on data retention for a Workspace in a zero data retention organization](https://support.claude.com/en/articles/16824617-turn-on-data-retention-for-a-workspace-in-a-zero-data-retention-organization)
