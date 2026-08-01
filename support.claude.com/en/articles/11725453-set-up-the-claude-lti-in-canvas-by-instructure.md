<!-- source: https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure -->

# Set up the Claude LTI in Canvas by Instructure

March 16, 2026

This article provides information on how to enable the Claude LTI integration in Canvas LMS. These steps are intended for Claude for Education administrators and Learning Management Systems (LMS) administrators.

## Creating Claude LTI Developer Key in Canvas

1. In Canvas, sign in as an administrator and navigate to **Admin -> Developer Keys**.
2. Click "+ Developer Key" then "+ LTI Key."
3. Enter the following:

   1. **Key Name:** Claude LTI
   2. **Description:** Enter a short description for the Canva LTI 1.3 app
   3. **Redirect URIs:** <https://claude.ai/lti/launch>
   4. **Title:** Claude LTI
   5. **Target Link URI:** <https://claude.ai/lti/launch>
   6. **OpenID Connect Initiation Url:** <https://claude.ai/api/lti/login>
   7. **JWK method:** <https://claude.ai/api/lti/keys>
4. Under **Additional Settings**, toggle Privacy Level to **Public**.
5. Under **Placements**, we recommend removing the defaults and adding "Course Navigation" and "Assignment Edit" as the options.
6. Click "Save."
7. Toggle the state to **On**.

## Installing Claude LTI as an App

1. In Canvas, go to Admin -> Settings -> Apps.
2. Click "View App Configurations" then select "+ App."
3. Select **Configuration Type** “By Client ID.”
4. Input the Client ID generated for your developer key (from Step 6 under Creating Claude LTI Developer Key in Canvas).
5. Click "Install" and refresh the course page.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1611422430/c8e0875feac1f2c7cb033be74fc9/AD_4nXfLU_bui3EXcCjQ0qm70HD97neqjGayKeDer_t76utlci8gZSUjYRhw6ZSOlDdqSEcwXBzd_shAh7pQEJ-8OoE0O21DM5coOgxmO_WD5hlwiuwtS2iYXcTavhIRyQT5zKFWvfn3NA?expires=1785544200&signature=57519caca071072619430b9ddae6c0882da8e11619085b97394362023cd9aae1&req=dSYmF818n4VcWfMW1HO4zTEDau4bn%2FeDEv2ojHLMylYRKrds7kA0PUnelvfM%0A0Nf9r%2FgYauN5ZS60JYY%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1611422430/c8e0875feac1f2c7cb033be74fc9/AD_4nXfLU_bui3EXcCjQ0qm70HD97neqjGayKeDer_t76utlci8gZSUjYRhw6ZSOlDdqSEcwXBzd_shAh7pQEJ-8OoE0O21DM5coOgxmO_WD5hlwiuwtS2iYXcTavhIRyQT5zKFWvfn3NA?expires=1785544200&signature=57519caca071072619430b9ddae6c0882da8e11619085b97394362023cd9aae1&req=dSYmF818n4VcWfMW1HO4zTEDau4bn%2FeDEv2ojHLMylYRKrds7kA0PUnelvfM%0A0Nf9r%2FgYauN5ZS60JYY%3D%0A)

## Turn on the Claude LTI Integration in Claude for Education organization settings

1. In Claude for Education, sign in as an administrator.
2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
3. Find **Canvas** and click "Enable."
4. In the settings modal that pops up, input the required information to enable the integration

   1. **Canvas Domain**
   2. **Client ID** (found in Canvas Admin -> Developer Keys)
   3. **Deployment ID** (found in Canvas Admin -> Settings -> Apps -> View App Configurations -> Claude LTI Settings Button -> Deployment ID)
5. Click "Save Changes." The integration should now show as enabled.

## Questions

If you have any questions about your Claude for Education plan account or the Claude LTI, we encourage you to contact your university’s administrator(s).

* [Get started with Claude for Education at your university (for Owners/Admins)](https://support.claude.com/en/articles/11139094-get-started-with-claude-for-education-at-your-university-for-owners-admins)
* [Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)
* [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
* [Open Claude Desktop with a link](https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link)
* [Open the Claude mobile app with a link](https://support.claude.com/en/articles/14898120-open-the-claude-mobile-app-with-a-link)
