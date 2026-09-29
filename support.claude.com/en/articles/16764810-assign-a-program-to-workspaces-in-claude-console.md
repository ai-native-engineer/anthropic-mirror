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

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1790642700&signature=0d94e87ede68a05f953883df191388e89800552e91627998ccf965bfce863375&req=diYjFM56mYRXXvMW1HO4zT%2FymUmBEAugktHcEoeKC4chDrV0pDMtD5MVsb4S%0AxZ4x%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642744587/d4584e035604f3b7c08afa53a1c6/ee1183ff-e591-4484-a989-1f754245d39c?expires=1790642700&signature=0d94e87ede68a05f953883df191388e89800552e91627998ccf965bfce863375&req=diYjFM56mYRXXvMW1HO4zT%2FymUmBEAugktHcEoeKC4chDrV0pDMtD5MVsb4S%0AxZ4x%0A)
2. Select the program to open its page. The **Workspaces** table shows each workspace's status. A workspace marked with an issue does not meet a requirement yet.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1790642700&signature=81f09a37fb3f457ac8565a435aa3e0c9caf456dc3eb72319e812d4a1835f0fea&req=diYjFM56mIRZW%2FMW1HO4zc116w5uRFK2MCr%2B42fbmkZi9OUXP%2FjKqoNPllEU%0AhkSY%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642745562/253e55a3292b35f728fb5dc89fb2/0878a8a9-dce5-4df2-9826-3796605b52a0?expires=1790642700&signature=81f09a37fb3f457ac8565a435aa3e0c9caf456dc3eb72319e812d4a1835f0fea&req=diYjFM56mIRZW%2FMW1HO4zc116w5uRFK2MCr%2B42fbmkZi9OUXP%2FjKqoNPllEU%0AhkSY%0A)

   Hover over the issue to see which requirement is not met.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1790642700&signature=e77544df648d03477cfed4b70dde6c7857ccd3ad5071d61be6cab1c10a3f68c0&req=diYjFM56m4VZX%2FMW1HO4zaveaOZkkn%2FHVPpeIJbmktSlxLdyxe%2B69YT0Jkck%0AOiLm%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746466/c49291119729e99f4dba8ec924e4/3f802c0e-7fbc-4e80-935a-05da58f65bde?expires=1790642700&signature=e77544df648d03477cfed4b70dde6c7857ccd3ad5071d61be6cab1c10a3f68c0&req=diYjFM56m4VZX%2FMW1HO4zaveaOZkkn%2FHVPpeIJbmktSlxLdyxe%2B69YT0Jkck%0AOiLm%0A)
3. To give a workspace access, make it meet the requirements. Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1790642700&signature=6771446bd56372aa8fec6090ad5e5b2292b1ffd5b8e7590560733e57c9f56786&req=diYjFM54lYBeXvMW1HO4zTU0lduWL0RA9BWcjfiNKI3wVmCqvKKJnfWyiP6G%0AD0tr%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642768117/1304e6b1350fc9bd88c4238a00e3/db606eb5-39d5-4309-a5a9-ee33847fc233?expires=1790642700&signature=6771446bd56372aa8fec6090ad5e5b2292b1ffd5b8e7590560733e57c9f56786&req=diYjFM54lYBeXvMW1HO4zTU0lduWL0RA9BWcjfiNKI3wVmCqvKKJnfWyiP6G%0AD0tr%0A)
4. Fix the requirement. For the Cyber Verification Program, turn on data retention under Manage, then Privacy controls. Then select "Rerun."

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1790642700&signature=3d5c2bf77b50f308d6e83153a8f9a56ab1d65b6b972e92cba04b6e8ed5498b82&req=diYjFM56m4hWXPMW1HO4zQfcHDuo63ws9apHi%2BiM8oj%2FfdFpY30b7s58wVX7%0AQJMf%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642746995/87151a11687a9c631b7a9d681390/d40a6c12-283d-4b3b-b6d6-9f631a73e7c0?expires=1790642700&signature=3d5c2bf77b50f308d6e83153a8f9a56ab1d65b6b972e92cba04b6e8ed5498b82&req=diYjFM56m4hWXPMW1HO4zQfcHDuo63ws9apHi%2BiM8oj%2FfdFpY30b7s58wVX7%0AQJMf%0A)
5. The program shows **Active** for the workspace.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1790642700&signature=c72d954d51e50fbecb0674979aad0274c0892f5bbce0e7c7e10884d187695cea&req=diYjFM56moNfWfMW1HO4zaUR86Zh8vw%2FfTukdAE3MWvPnLskU92HVOvGZXMk%0A6zO9%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2642747200/a18bdccde474c9f4eba371cf6050/b0e9d5e3-1e5f-4f27-b682-5684084f92e8?expires=1790642700&signature=c72d954d51e50fbecb0674979aad0274c0892f5bbce0e7c7e10884d187695cea&req=diYjFM56moNfWfMW1HO4zaUR86Zh8vw%2FfTukdAE3MWvPnLskU92HVOvGZXMk%0A6zO9%0A)

## Troubleshooting

* **The Grants page is missing.** Your organization does not have a grant yet, or you are not an organization Admin. Contact your Anthropic account team or your admin.
* **The workspace shows as inactive.** Open the workspace, select "Manage," then "Programs," and check the **Qualifications** panel for an unmet requirement. Fix each unmet requirement and try again.
* **The grant is over its seat limit.** Some programs have a seat cap. Assigned workspaces lose access until your organization is back under the limit. Reduce the number of members counted toward the grant, then check again.
* **You are trying to use the default Console workspace.** Some programs don't allow the program to be assigned to the default workspace. If the default workspace isn’t working, assign a different workspace or create a new one.

* [Creating and managing Workspaces in the Claude Console](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console)
* [Real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)
* [Data retention practices for Covered Models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models)
* [Claude Team plan for scientists](https://support.claude.com/en/articles/16634237-claude-team-plan-for-scientists)
* [Turn on data retention for a Workspace in a zero data retention organization](https://support.claude.com/en/articles/16824617-turn-on-data-retention-for-a-workspace-in-a-zero-data-retention-organization)
