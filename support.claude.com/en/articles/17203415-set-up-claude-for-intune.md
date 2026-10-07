<!-- source: https://support.claude.com/en/articles/17203415-set-up-claude-for-intune -->

Claude for Intune is a managed version of Claude for iOS for organizations that use Microsoft Intune. This article explains how Intune admins add Claude for Intune in the Microsoft Intune admin center and which app to tell employees to install.

## What is Claude for Intune?

Claude for Intune is built for organizations that manage mobile devices with Microsoft Intune, including organizations that let employees work from personal iPhones and iPads.

* Claude for Intune is a separate app from the standard Claude app. Both are listed on the App Store.
* IT teams can apply Intune app-protection policies to Claude for Intune on company-owned and employee-owned iPhones and iPads.
* It signs in with Microsoft only.
* It supports Intune app-protection policies and Microsoft Entra Conditional Access.

## Requirements

Before you set up Claude for Intune, check that you meet these requirements:

* You have an Enterprise plan.
* Your organization uses Microsoft Intune, and you have access to the Microsoft Intune admin center.
* Employees sign in to Claude for Intune with Microsoft. Other sign-in methods aren't available in Claude for Intune.
* You’re using iOS or iPadOS version 18.0 or later.
* Anthropic has enabled Microsoft sign-in for your organization's email domains.
* If you use Conditional Access, Claude for Intune is registered in your Microsoft Entra tenant.

## Get your organization ready

### 1. Ask Anthropic to enable Microsoft sign-in

Before employees can sign in to Claude for Intune, Anthropic needs to enable Microsoft sign-in for your organization's email domains. Contact your Anthropic account team or support, and tell them which email domains your employees use to sign in.

### 2. Register Claude for Intune in your Entra tenant

If you want to use Conditional Access with Claude for Intune, the app has to be registered in your Microsoft Entra tenant first. Until it is, Claude for Intune doesn't appear in the list of apps you can select in a Conditional Access policy.

Claude for Intune is registered the first time someone who is authorized to consent on behalf of the organization signs in with Microsoft. Choose one of these options:

* **Have a user sign in.** Go to claude.ai and select “Continue with Microsoft.” One successful sign-in is enough.
* **Grant admin consent.** A tenant admin opens the following URL, replacing {organization} with your tenant ID or domain: `https://login.microsoftonline.com/{organization}/adminconsent?client_id=bb747f0e-002b-4882-9960-916fe00a2b90`

After either option, Claude for Intune appears in Microsoft Entra and your Conditional Access admin can target it in a policy.

To require app protection at sign-in, target the Conditional Access rule at “All resources” with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Add Claude for Intune to your managed apps and make it available to BYOD devices.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1791333900&signature=6fc6c08f5b94b67fc20c4cf6a5ea71ad5cce8fae0c9f2f5539d4f1e1eae0bee0&req=dicnFsh3n4NZUPMW1HO4ze7khjDS4WhpAMLV2Uu0R4WjUXW2HqXfjJwVkS7Q%0ARlWZ%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1791333900&signature=6fc6c08f5b94b67fc20c4cf6a5ea71ad5cce8fae0c9f2f5539d4f1e1eae0bee0&req=dicnFsh3n4NZUPMW1HO4ze7khjDS4WhpAMLV2Uu0R4WjUXW2HqXfjJwVkS7Q%0ARlWZ%0A)
2. Under Platforms, select “iOS/iPadOS”:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1791333900&signature=c6cb256d9e1e1f248aa44319b573db45818a959bf8bf834f803445f92eb68e04&req=dicnFsh3mIFcX%2FMW1HO4zeH1oUzksnCdQ7hR7Wh%2Bi72cv5UBUcGDOaA8KTe%2F%0AwbV0%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1791333900&signature=c6cb256d9e1e1f248aa44319b573db45818a959bf8bf834f803445f92eb68e04&req=dicnFsh3mIFcX%2FMW1HO4zeH1oUzksnCdQ7hR7Wh%2Bi72cv5UBUcGDOaA8KTe%2F%0AwbV0%0A)
3. Click “+ Create.” For the App type, select the “iOS store app,” and click the “Select” button on the bottom:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1791333900&signature=c7b35dda58ae9c4b5db182993e4dbb1027ad627de76ce295ccebe41dc756af87&req=dicnFsh3mIZWWPMW1HO4zTni3ccqYZ0l2SRx6amjj9HpKNBu8Aj8Lx%2BSD%2BeB%0Ak994%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1791333900&signature=c7b35dda58ae9c4b5db182993e4dbb1027ad627de76ce295ccebe41dc756af87&req=dicnFsh3mIZWWPMW1HO4zTni3ccqYZ0l2SRx6amjj9HpKNBu8Aj8Lx%2BSD%2BeB%0Ak994%0A)
4. Search “Claude for Intune” and click the “Select" button on the bottom.
5. In **App Information**, set **Minimum operating system** to iOS 18, then click the “Next” button:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1791333900&signature=7cc6fdb46e466e65620f9ba11c750fb946e51d142e96f1a3a1b469683b87c84e&req=dicnFsh3m4VaUfMW1HO4zbxl5YlUdDEnDNNSLAHCCFpEiwOQi7tRdQiZ2Abm%0AaRkc%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1791333900&signature=7cc6fdb46e466e65620f9ba11c750fb946e51d142e96f1a3a1b469683b87c84e&req=dicnFsh3m4VaUfMW1HO4zbxl5YlUdDEnDNNSLAHCCFpEiwOQi7tRdQiZ2Abm%0AaRkc%0A)
6. For **Assignments**, add a group of users to make it available in their device’s Company Portal:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1791333900&signature=ee51bd58ec5cc81c2ba315a9d795d77b7312bfc2c7894d0b0bb7138f144c5505&req=dicnFsh3moZeXPMW1HO4zeVx8DQa4i%2BEoVYQxJ7ndH7XFSAaxh9x%2BIIjS8ux%0AJ3t0%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1791333900&signature=ee51bd58ec5cc81c2ba315a9d795d77b7312bfc2c7894d0b0bb7138f144c5505&req=dicnFsh3moZeXPMW1HO4zeVx8DQa4i%2BEoVYQxJ7ndH7XFSAaxh9x%2BIIjS8ux%0AJ3t0%0A)
7. Click “Next,” review and create.
8. Users have to download the app from Company Portal on their devices for access.

### 2. Apply an app-protection policy to Claude for Intune.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1791333900&signature=6e49de5220316b36e155cc897c3495fa029fbf206baaf2ecd51ce79c0638d57b&req=dicnFsh3nYZZWfMW1HO4zQwrZIsBUNE1LtTCoSp4D6ocg9sIP18DSnWppNZg%0AsNI%2B%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1791333900&signature=6e49de5220316b36e155cc897c3495fa029fbf206baaf2ecd51ce79c0638d57b&req=dicnFsh3nYZZWfMW1HO4zQwrZIsBUNE1LtTCoSp4D6ocg9sIP18DSnWppNZg%0AsNI%2B%0A)
2. Under **Manage apps**, select “Protection”:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1791333900&signature=62b12b28cc13dd5bd120b124851b151b4fbaa9e4fe24b5a05a59a36989f706f0&req=dicnFst%2BnYlaUfMW1HO4zeBHXB4%2B9v7knJWY0xu8hzI3YguKDwFrXYpfARr5%0Aabb2%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1791333900&signature=62b12b28cc13dd5bd120b124851b151b4fbaa9e4fe24b5a05a59a36989f706f0&req=dicnFst%2BnYlaUfMW1HO4zeBHXB4%2B9v7knJWY0xu8hzI3YguKDwFrXYpfARr5%0Aabb2%0A)
3. Click “+ Create” and then select “iOS/iPadOS”:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1791333900&signature=614192ea6ee8ecf940779ee41db0fcf94b863094cd701389ff91496ac6889cf7&req=dicnFst%2BnIJXW%2FMW1HO4zc89y0pVAXlHV2VWh%2B9zzErb0tdbUZK%2B1gmO0y7W%0AGA4u%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1791333900&signature=614192ea6ee8ecf940779ee41db0fcf94b863094cd701389ff91496ac6889cf7&req=dicnFst%2BnIJXW%2FMW1HO4zc89y0pVAXlHV2VWh%2B9zzErb0tdbUZK%2B1gmO0y7W%0AGA4u%0A)
4. Enter Name in the **Basics** tab, then click “Next” to **Apps**. Set **Target policy to** “Selected apps.” Click “+ Select custom apps”:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1791333900&signature=122e00e7613f6de0023be24f784fc8be5ba42cbbcb0a952178727d8c6432188d&req=dicnFst%2BnIhdUPMW1HO4zVmMRJAXUD4BKETwku7gMsvY5%2FSnrivewRgbYkhs%0AcysD%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1791333900&signature=122e00e7613f6de0023be24f784fc8be5ba42cbbcb0a952178727d8c6432188d&req=dicnFst%2BnIhdUPMW1HO4zVmMRJAXUD4BKETwku7gMsvY5%2FSnrivewRgbYkhs%0AcysD%0A)
5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking “Select”:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1791333900&signature=e5a2cb4472ed9cd3472804497197ced4a05af50d97b689df917e58efd72a556a&req=dicnFst%2Bn4leX%2FMW1HO4zf6tYiIry6l%2B12LT9vQL0W4WKEyOav2GQTVkI%2BTJ%0AWLUz%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1791333900&signature=e5a2cb4472ed9cd3472804497197ced4a05af50d97b689df917e58efd72a556a&req=dicnFst%2Bn4leX%2FMW1HO4zf6tYiIry6l%2B12LT9vQL0W4WKEyOav2GQTVkI%2BTJ%0AWLUz%0A)
6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking “Next”:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1791333900&signature=1b5af243eb40d615ec058644c42459e3b6a8236ea7250c165e9bd51256f18df3&req=dicnFst%2BnoZXWfMW1HO4zQd95NSJ2MvW8F6Cfy2R7u8RiUSurP1mH2Io3RYf%0AD4lr%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1791333900&signature=1b5af243eb40d615ec058644c42459e3b6a8236ea7250c165e9bd51256f18df3&req=dicnFst%2BnoZXWfMW1HO4zQd95NSJ2MvW8F6Cfy2R7u8RiUSurP1mH2Io3RYf%0AD4lr%0A)
7. Configure the Data protection, Access requirements, and Conditional launch settings as needed.
8. In the **Assignments** tab, add a user group to assign the policy to them.
9. Review and create.
10. The app only becomes "managed" after the user signs in with org credentials post-install (may require a restart).

## Tell employees which app to install

Claude for Intune and the standard Claude app are separate apps. Your Intune app-protection policies apply to Claude for Intune.

Wherever your organization requires Intune protection, tell employees on managed or employee-owned iPhones and iPads to install **[Claude for Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**, not the standard Claude app.

## Before Microsoft lists Claude for Intune as a protected app

Claude for Intune doesn't yet appear in Microsoft's list of protected apps, so you can't search for it when you create an app-protection policy. Until it's listed, add it to your policy by entering its bundle ID manually:

1. Follow the steps in **[Apply an app-protection policy to Claude for Intune](#h_5fda0300e8).**
2. When you select apps, choose “Select custom apps” and enter the bundle ID `com.anthropic.claudeforintune`.

After Microsoft adds Claude for Intune to its protected apps list, you'll select it from the list of public apps instead of using “Select custom apps.”

* [Install Claude for iOS](https://support.claude.com/en/articles/9266462-install-claude-for-ios)
* [Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)
* [Deploy Claude Desktop for Windows](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)
* [Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)
* [Log in to your Claude account](https://support.claude.com/en/articles/13189465-log-in-to-your-claude-account)
