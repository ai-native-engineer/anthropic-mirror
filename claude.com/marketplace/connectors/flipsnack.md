<!-- source: https://claude.com/marketplace/connectors/flipsnack -->

Connector URL`https://mcp.flipsnack.com/mcp`

More[Documentation (opens in new tab)](https://help.flipsnack.com/en/how-to-connect-and-use-the-flipsnack-app-in-claude)[Support (opens in new tab)](mailto:contact@flipsnack.com)[Privacy policy (opens in new tab)](https://legal.flipsnack.com/privacy-policy)

Flipsnack is a platform for creating, publishing, and sharing digital flipbooks such as catalogs, magazines, brochures, and reports. This connector lets you work with the flipbook collections in your Flipsnack account from Claude.

What you can do:

- List and search your collections by status, folder, or keyword, and open the full details of any collection, including its direct link

- Create a new collection by importing a PDF from a public URL

- Update a collection's title, description, visibility, and display settings such as player look and feel, controls, background color, auto-flip, and password

- Control who can read a private collection: view or replace its list of allowed readers

- Share a published collection by email, using your workspace's brand settings

- Move a collection to the Flipsnack trash, from where it can be restored

- Generate the HTML embed code for a collection, with fixed or responsive dimensions and a starting page

- Read analytics for one collection (impressions, views, time spent, downloads, with an optional date range and per-page breakdown), for one reader of a collection, or totals for your whole account

The connector uses Flipsnack's own API. You sign in with your Flipsnack account through OAuth, and every call is limited to the account you signed in with. Updating a collection, replacing its reader permissions, and deleting it are marked as destructive, so Claude asks before running them.

Requires admin access to a Flipsnack workspace on a paid plan.

## Tools

* collection\_create
* collection\_delete
* collection\_get\_collection
* collection\_get\_embed
* collection\_get\_list
* collection\_get\_permissions
* collection\_get\_reader\_stats
* collection\_get\_stats
* collection\_send\_email
* collection\_set\_permissions
* collection\_update
* user\_get\_stats

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/53ca8822f4c024f9b358b1e44148a1dc3c616dbe.svg?w=128&fit=max&auto=format)

### [Gmail](https://claude.com/marketplace/connectors/gmail)

Draft replies, summarize threads, & search your inbox

[Add Gmail in Claude (opens in new tab)](https://claude.ai/directory/2701e52f-b826-4aaf-8b25-11f2a97c98b0 "Add in Claude")

![](https://assets.claude.com/20c8443aa72ae4e4d77f923e6c33314713f965e8.svg?w=128&fit=max&auto=format)

### [Microsoft 365](https://claude.com/marketplace/connectors/microsoft-365)

Access SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://assets.claude.com/e476a6c2c2f961f5f2120482f37b1daafc1506d9.jpg?w=128&fit=max&auto=format)

### [Canva](https://claude.com/marketplace/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")

![](https://assets.claude.com/bdf25f3db0bfe9b74855f504c31bd8522659edae.svg?w=128&fit=max&auto=format)

### [Slack](https://claude.com/marketplace/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")

![](https://assets.claude.com/58e9c84c9e164137b0e9f532e05cb242d46204f9.jpg?w=128&fit=max&auto=format)

### [Figma](https://claude.com/marketplace/connectors/figma)

Generate diagrams and better code from Figma context

[Add Figma in Claude (opens in new tab)](https://claude.ai/directory/c758d038-d8eb-4421-b426-9dd68dc7f84a "Add in Claude")

![](https://www.google.com/s2/favicons?domain=picsart.com&sz=96)

### [Picsart Media Studio](https://claude.com/marketplace/connectors/picsart-media-studio)

Anthropic verifiedTrending

Turn your clips and photos into finished videos

[Add Picsart Media Studio in Claude (opens in new tab)](https://claude.ai/directory/4f1ba81e-dd57-416e-a0ec-5a64c13ba74c "Add in Claude")
