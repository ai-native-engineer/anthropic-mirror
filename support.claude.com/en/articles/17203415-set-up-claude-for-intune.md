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
* An admin in your Microsoft Entra tenant has granted admin consent for Claude for Intune. This is required for every organization.

## Get your organization ready

### 1. Ask Anthropic to enable Microsoft sign-in

Before employees can sign in to Claude for Intune, Anthropic needs to enable Microsoft sign-in for your organization's email domains. Contact your Anthropic account team or support, and tell them which email domains your employees use to sign in.

### 2. Register Claude for Intune in your Entra tenant

Before employees can sign in, an admin in your Microsoft Entra tenant needs to grant admin consent for Claude for Intune. This is required for every organization. It approves the permission Claude for Intune uses to work with Microsoft Intune app protection, and it registers the app in your tenant so you can select it in a Conditional Access policy.

**Grant admin consent.** A tenant admin opens the following URL, replacing {organization} with your tenant ID or domain: `https://login.microsoftonline.com/{organization}/adminconsent?client_id=bb747f0e-002b-4882-9960-916fe00a2b90`

To confirm it worked, in the Microsoft Entra admin center go to Enterprise applications, open "Claude for Intune (Public)", and select Permissions. "Microsoft Mobile Application Management" should be listed on the "Admin consent" tab. If it isn't, select "Grant admin consent" on that page.

**Note:** Employees signing in to Claude for Intune with "Continue with Microsoft" does not grant this consent; an Entra admin has to grant it.

If employees are signed out within a few seconds of signing in, this step has most likely not been completed. After granting admin consent, ask them to delete Claude for Intune, reinstall it, and sign in again.

To require app protection at sign-in, target the Conditional Access rule at "All resources" with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Install Claude for Intune on employees’ devices

How employees get Claude for Intune depends on how their iPhone or iPad is managed:

* **Personal devices not enrolled in Intune (app protection only):** You don’t need to add or assign the app in Intune. Employees install Claude for Intune from the App Store (it appears there as "**[Claude Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**") and sign in with "Continue with Microsoft." Your app-protection policy (step 2) applies after they sign in.

  + Optional: to also list it in Company Portal, add it as an iOS store app and assign the user group as "Available with or without enrollment."
* **Devices enrolled with Apple User Enrollment:** Employees install Claude for Intune from the App Store themselves. Intune can’t install an app added as an "iOS store app" on these devices, and Company Portal shows "This device needs to be managed before you can install apps."
* **Company-owned devices enrolled in Intune:** Add Claude for Intune as an iOS store app and assign it to a user or device group using the steps below. Employees install it from Company Portal, or you can make the assignment Required to push it to their devices.

To add Claude for Intune for enrolled company-owned devices:

1. In the Microsoft Intune admin center, select "Apps" from the left side navigation panel:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1794098700&signature=7127fd1e53e206ea49e6c93b5be91a20138a01f69c177df0e46f026764d2c885&req=dicnFsh3n4NZUPMW1HO4ze7khjXR62NnAMLV2Uu0R4Xo2jYdYO5T0%2BQ0S5ra%0AIOTN%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1794098700&signature=7127fd1e53e206ea49e6c93b5be91a20138a01f69c177df0e46f026764d2c885&req=dicnFsh3n4NZUPMW1HO4ze7khjXR62NnAMLV2Uu0R4Xo2jYdYO5T0%2BQ0S5ra%0AIOTN%0A)
2. Under Platforms, select "iOS/iPadOS":

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1794098700&signature=1a2809d87a2826d67db00159b23dbdfb40428b60aa64ab72a1457a3d53745f3b&req=dicnFsh3mIFcX%2FMW1HO4zeH1oUnnuHuTQ7hR7Wh%2Bi70WN8%2FFqYaNJjZQmwB8%0A3M8J%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1794098700&signature=1a2809d87a2826d67db00159b23dbdfb40428b60aa64ab72a1457a3d53745f3b&req=dicnFsh3mIFcX%2FMW1HO4zeH1oUnnuHuTQ7hR7Wh%2Bi70WN8%2FFqYaNJjZQmwB8%0A3M8J%0A)
3. Click "+ Create." For the App type, select the "iOS store app," and click the "Select" button on the bottom:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1794098700&signature=8db7c0b2cdeec28950631c6ee36856b811b386597a42bd8850e65a0c2e0e489b&req=dicnFsh3mIZWWPMW1HO4zTni3cIpa5Yr2SRx6amjj9H%2B4HAAvhn5kSHm6wiB%0AvckH%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1794098700&signature=8db7c0b2cdeec28950631c6ee36856b811b386597a42bd8850e65a0c2e0e489b&req=dicnFsh3mIZWWPMW1HO4zTni3cIpa5Yr2SRx6amjj9H%2B4HAAvhn5kSHm6wiB%0AvckH%0A)
4. Search "Claude for Intune" and click the "Select" button on the bottom.
5. In **App Information**, set **Minimum operating system** to iOS 18, then click the "Next" button:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1794098700&signature=66a461365bde8d13a7310adee055f5cea72d38a6c96335088ff9f2a20cd92d56&req=dicnFsh3m4VaUfMW1HO4zbxl5YxXfjopDNNSLAHCCFqtR5OFcpKMXHnuV8f8%0A6ZP1%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1794098700&signature=66a461365bde8d13a7310adee055f5cea72d38a6c96335088ff9f2a20cd92d56&req=dicnFsh3m4VaUfMW1HO4zbxl5YxXfjopDNNSLAHCCFqtR5OFcpKMXHnuV8f8%0A6ZP1%0A)
6. For **Assignments**, add the groups that should get the app: under Required to install it automatically, or under Available for enrolled devices so employees can install it from Company Portal. You can use user groups or device groups.

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2741107114/8f15b0d179a54c2ca4effaad8577/55bed25a-4b20-47b0-9e89-7f8adc86c04f?expires=1794098700&signature=f7c5b5fd3b9458fb10e9bbb48d9c86433c090ba0423d96a5015d8dda4412da3a&req=dicjF8h%2BmoBeXfMW1HO4zYaZMey8cPuZmN%2B6UXepdg9SqP0hkfFkgJsUS%2FPi%0ARLKS%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2741107114/8f15b0d179a54c2ca4effaad8577/55bed25a-4b20-47b0-9e89-7f8adc86c04f?expires=1794098700&signature=f7c5b5fd3b9458fb10e9bbb48d9c86433c090ba0423d96a5015d8dda4412da3a&req=dicjF8h%2BmoBeXfMW1HO4zYaZMey8cPuZmN%2B6UXepdg9SqP0hkfFkgJsUS%2FPi%0ARLKS%0A)
7. Click "Next," review and create.
8. If you assigned the app as Required, it installs automatically; if Available, employees install it from Company Portal.

### 2. Apply an app-protection policy to Claude for Intune

1. In the Microsoft Intune admin center, select "Apps" from the left side navigation panel:

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1794098700&signature=0ce876adbd2dde3462397b70be8c4a2f09f577f9dd4c08fffd0d85d74c7c2913&req=dicnFsh3nYZZWfMW1HO4zQwrZI4CWto7LtTCoSp4D6q9y97t6b3jpPAxRcL%2B%0A3qWr%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1794098700&signature=0ce876adbd2dde3462397b70be8c4a2f09f577f9dd4c08fffd0d85d74c7c2913&req=dicnFsh3nYZZWfMW1HO4zQwrZI4CWto7LtTCoSp4D6q9y97t6b3jpPAxRcL%2B%0A3qWr%0A)
2. Under **Manage apps**, select "Protection":

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1794098700&signature=7c740c6b819595d845bb363af55b3efcd76e99f7754d5fcf8b22dccee29b3490&req=dicnFst%2BnYlaUfMW1HO4zeBHXBs9%2FPXqnJWY0xu8hzJHnDrpb0fup9Ix9ZFi%0AMOG0%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1794098700&signature=7c740c6b819595d845bb363af55b3efcd76e99f7754d5fcf8b22dccee29b3490&req=dicnFst%2BnYlaUfMW1HO4zeBHXBs9%2FPXqnJWY0xu8hzJHnDrpb0fup9Ix9ZFi%0AMOG0%0A)
3. Click "+ Create" and then select "iOS/iPadOS":

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1794098700&signature=1be90d1b1ddb15a9a593fec2c60e9880e372910c1e731a3f86dc7f991c06c909&req=dicnFst%2BnIJXW%2FMW1HO4zc89y09WC3JJV2VWh%2B9zzEpp76iidFb46sXyt9yw%0Ag9XJ%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1794098700&signature=1be90d1b1ddb15a9a593fec2c60e9880e372910c1e731a3f86dc7f991c06c909&req=dicnFst%2BnIJXW%2FMW1HO4zc89y09WC3JJV2VWh%2B9zzEpp76iidFb46sXyt9yw%0Ag9XJ%0A)
4. Enter Name in the **Basics** tab, then click "Next" to **Apps**. Set **Target policy to** "Selected apps." Click "+ Select custom apps":

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1794098700&signature=14db25c5ea1e7d69a69ce76b91a79a069bd647f18e2e564313628888c3c62df6&req=dicnFst%2BnIhdUPMW1HO4zVmMRJUUWjUPKETwku7gMsv3AHxD4%2FAnIBA69350%0AmvXx%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1794098700&signature=14db25c5ea1e7d69a69ce76b91a79a069bd647f18e2e564313628888c3c62df6&req=dicnFst%2BnIhdUPMW1HO4zVmMRJUUWjUPKETwku7gMsv3AHxD4%2FAnIBA69350%0AmvXx%0A)
5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking "Select":

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1794098700&signature=a6095c5260767628679ace917d3a3b4f7e4295fd23375a94fc1c4ae24f9c4a00&req=dicnFst%2Bn4leX%2FMW1HO4zf6tYicowaJw12LT9vQL0W7GCncdezbpS8dC5nAV%0AC15S%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1794098700&signature=a6095c5260767628679ace917d3a3b4f7e4295fd23375a94fc1c4ae24f9c4a00&req=dicnFst%2Bn4leX%2FMW1HO4zf6tYicowaJw12LT9vQL0W7GCncdezbpS8dC5nAV%0AC15S%0A)
6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking "Next":

   [![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1794098700&signature=98962f732e2d377ed54c4ec7bb8b257a9253ffe22af928dfeb41e1c8fc79464d&req=dicnFst%2BnoZXWfMW1HO4zQd95NGK0sDY8F6Cfy2R7u%2B6ROsQGtdAt5Cpcnj4%0Ay%2F%2B4%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1794098700&signature=98962f732e2d377ed54c4ec7bb8b257a9253ffe22af928dfeb41e1c8fc79464d&req=dicnFst%2BnoZXWfMW1HO4zQd95NGK0sDY8F6Cfy2R7u%2B6ROsQGtdAt5Cpcnj4%0Ay%2F%2B4%0A)
7. Configure the Data protection, Access requirements, and Conditional launch settings as needed.
8. In the **Assignments** tab, assign the policy to a user group that includes everyone who will use Claude for Intune—app-protection policies can only target user groups, not device groups. Make sure it also applies to unmanaged devices: don't limit it to Intune-managed devices with the device-type setting or an assignment filter, or employees on personal phones get signed out right after signing in*.*
9. Review and create.
10. The app only becomes "managed" after the user signs in with org credentials post-install (may require a restart).

## Tell employees which app to install

Claude for Intune and the standard Claude app are separate apps. Your Intune app-protection policies apply to Claude for Intune.

Wherever your organization requires Intune protection, tell employees on managed or employee-owned iPhones and iPads to install **[Claude for Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**, not the standard Claude app.

## Before Microsoft lists Claude for Intune as a protected app

Claude for Intune doesn't yet appear in Microsoft's list of protected apps, so you can't search for it when you create an app-protection policy. Until it's listed, add it to your policy by entering its bundle ID manually:

1. Follow the steps in **[Apply an app-protection policy to Claude for Intune](#h_5fda0300e8).**
2. When you select apps, choose "Select custom apps" and enter the bundle ID `com.anthropic.claudeforintune`.

After Microsoft adds Claude for Intune to its protected apps list, you'll select it from the list of public apps instead of using "Select custom apps."

* [Install Claude for iOS](https://support.claude.com/en/articles/9266462-install-claude-for-ios)
* [Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)
* [Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)
* [Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)
* [Deploy Claude Desktop for Windows](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)
