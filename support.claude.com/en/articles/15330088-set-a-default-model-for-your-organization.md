<!-- source: https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization -->

# Set a default model for your organization

Updated over a week ago

This guide explains how to choose the Claude model that new conversations start on across your organization, in chat and Claude Cowork. You can set one default for your whole organization, or set different defaults for specific custom roles.

Default model settings are available in beta for Enterprise plan organizations. Owners and Primary Owners can manage them in **[Organization settings > Models](http://claude.ai/admin-settings/models)**.

## How default models work

When you set or change a default model, it replaces the model currently selected in each member’s model picker. New conversations in chat and Cowork then start on the model you’ve chosen.

**Note:** Not all models are available in every product. If the selected model is not available in the product, Anthropic’s recommendation is used as default.

Members can still select a different model for any conversation. Claude remembers each member’s last selection, so their next conversation starts on whichever model they last used. When you update the default again, the new default replaces their selection.

For example: you set the organization default to Claude Sonnet 4.6, and every member’s new conversations start on Sonnet 4.6. A member switches a conversation to Claude Opus 4.7, so their next conversations start on Opus 4.7. When you later change the organization default, the new default replaces their selection again.

You can set a default at two levels:

* Organization default: applies to every member of your organization.
* Custom role default: applies to members assigned to that role and takes precedence over the organization default.

**Note:** Default model settings apply to chat and Cowork. Claude Code model selection is managed separately. For more information, see **[Claude Code model configuration](https://support.claude.com/en/articles/11940350)**.

For member-facing instructions on switching models, see **[Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)**.

## Set the organization default model

The organization default applies to every member. To set it:

1. Navigate to **[Organization settings > Models](http://claude.ai/admin-settings/models)**.
2. Under **Default model**, select an option:

   1. “Use Anthropic’s recommended default”: Anthropic’s recommended model that updates automatically when new models are released.
   2. “Choose a specific model”: a specific model that won’t change when new models are released.
3. If you select “Choose a specific model,” choose a model from the list.
4. Click “Save changes.”

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2451362891/589a6514b79728f85a7d6315fd61/79ac3bb9-baa9-4d9e-bf78-7d6dee929a29?expires=1782459900&signature=869f15b64b79027b1438c67bf8dca200c792b8adbf8ca82fa09aa14456bee28e&req=diQiF8p4n4lWWPMW1HO4zRmMOajmI3lejH07H14UT8Fb3rrhKbmOIG0CVKLD%0AlzLrv1uGsjVrgtiDG64%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2451362891/589a6514b79728f85a7d6315fd61/79ac3bb9-baa9-4d9e-bf78-7d6dee929a29?expires=1782459900&signature=869f15b64b79027b1438c67bf8dca200c792b8adbf8ca82fa09aa14456bee28e&req=diQiF8p4n4lWWPMW1HO4zRmMOajmI3lejH07H14UT8Fb3rrhKbmOIG0CVKLD%0AlzLrv1uGsjVrgtiDG64%3D%0A)

## Set a default model for a custom role

Custom role defaults let you set different starting models for different teams. For example, you can keep most of your organization on the recommended default while a specific group starts on a different model.

1. Navigate to **[Organization settings > Roles](http://claude.ai/admin-settings/roles)**.
2. Click the role you want to edit, or create a new role.
3. Under **Default model**, select a model. Roles are set to “None selected” unless you choose a specific model.
4. Click “Save role” to save your changes.

A role’s default model takes precedence over the organization default for members assigned to that role.

If a member belongs to multiple groups whose custom roles set different default models, the most capable model will be the default. Capability is determined first by model family (Haiku, Sonnet, Opus), then release date, so more capable model families take precedence, and newer models within the same family take precedence.

**Note:** Custom roles only affect members whose role is set to “Custom.” Members with the User, Admin, or Owner roles get the default model from the organization setting, not from custom roles.

For details on creating roles and assigning them to groups, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452)**.

[Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)[Release notes](https://support.claude.com/en/articles/12138966-release-notes)[Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)[Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)[Enable US-only inference for your organization](https://support.claude.com/en/articles/15422948-enable-us-only-inference-for-your-organization)
