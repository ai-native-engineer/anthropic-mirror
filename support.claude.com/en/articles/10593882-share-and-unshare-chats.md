<!-- source: https://support.claude.com/en/articles/10593882-share-and-unshare-chats -->

Learn how to create shareable links to your chats with Claude. While chats are always private by default, you can easily create snapshots of your conversations to share via direct link. This guide walks you through the process of sharing and unsharing chats.

## Share chats

To share a chat:

1. Click the "Share" button in the upper right corner of your chat.
2. Click the "Share" button in the pop out to create a shareable link.

Once a chat has been shared, anyone with the link can view the chat snapshot. The chat snapshot includes all messages that were sent prior to sharing the chat, including any artifacts. All messages sent after sharing a chat will remain private by default. However, if you unshare the chat and share it again, the snapshot will be updated to include any new messages.

**Note:** Users on Team and Enterprise plans can only share chats with other members of the same organization, not publicly. Read more here: **[Project visibility and sharing](https://support.claude.com/en/articles/9519189-project-visibility-and-sharing)**.

### Share chats with files or MCP integrations

When sharing chats that include uploaded files or MCP (Model Context Protocol) integrations, it's important to understand what information is included in the shared snapshot.

**Attached files:** If you share a chat that contains an attached file, the file itself is not included in the shared snapshot and remains private. Only the conversation and Claude's responses will be visible to anyone with the link.

**MCP tool calls:** When sharing chats that use MCP integrations, the raw data retrieved from MCP tool calls remains hidden in the shared snapshot. Only the final chat output and conversation will be visible to viewers. The underlying tool call data stays private.

This ensures that sensitive information from your files and connected tools is protected, even when you share a chat snapshot.

## Unshare chats

To unshare a chat:

1. Navigate to the "Share" menu.
2. Click the visibility dropdown.
3. Change the chat from "Public" to "Private" to disable the direct link.

## Manage shared chats

Users on free, Pro, or Max plans can review a log of shared chats by navigating to **[Settings > Privacy](https://claude.ai/settings/data-privacy-controls)**. Find the **Privacy settings** section and click “Manage” next to **Shared chats:**

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1790833500&signature=a4c17e42e701df3978f3cb86e923da4dcdd08a893fa05a7b0b1f39724771985a&req=dSklF894lIheWvMW1HO4zWn5HjMVYUZuc9cNIYuX0GF2304jDhYIs917CuWo%0AszfZ6cQ%2FrBVlOZWP2hg%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1790833500&signature=a4c17e42e701df3978f3cb86e923da4dcdd08a893fa05a7b0b1f39724771985a&req=dSklF894lIheWvMW1HO4zWn5HjMVYUZuc9cNIYuX0GF2304jDhYIs917CuWo%0AszfZ6cQ%2FrBVlOZWP2hg%3D%0A)

This will open a **Shared chats** modal listing the title, date shared, and link to each chat, allowing you to easily review and access all your previously-shared content. From here, you also have the option to click “Unshare” next to each listed chat to revoke access to the last snapshot you shared:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1790833500&signature=cede6aa3b088ad926e3bc3a7ed97846db27bfc36c6d9466ded6f2a098bc8e433&req=dSYlEst6noleWfMW1HO4ze44eSdplxE7guvTv9woD7aJr2heYXaE9cUWhe%2Fe%0AlbhKFk2IHUXk0uOt5pg%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1790833500&signature=cede6aa3b088ad926e3bc3a7ed97846db27bfc36c6d9466ded6f2a098bc8e433&req=dSYlEst6noleWfMW1HO4ze44eSdplxE7guvTv9woD7aJr2heYXaE9cUWhe%2Fe%0AlbhKFk2IHUXk0uOt5pg%3D%0A)

If you don’t have any shared chat snapshots, the **Shared chats** modal will show “No shared content found”:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1790833500&signature=0b47c9842a93976b595f2ad185b77dbf1e88f7d47e264794925d1e3cf6ab80f0&req=dSYlEst6nolfUfMW1HO4zdaFnMV8goq0DeZsm0Gz1HtUpoYHW8tKRgkN2bXi%0AXpuvWIM%2FaIMV%2BAoB%2FH8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1790833500&signature=0b47c9842a93976b595f2ad185b77dbf1e88f7d47e264794925d1e3cf6ab80f0&req=dSYlEst6nolfUfMW1HO4zdaFnMV8goq0DeZsm0Gz1HtUpoYHW8tKRgkN2bXi%0AXpuvWIM%2FaIMV%2BAoB%2FH8%3D%0A)

* [Manage project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)
* [Share artifacts](https://support.claude.com/en/articles/9547008-share-artifacts)
* [Custom visuals in chat and Cowork](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork)
* [Public links for shared chats](https://support.claude.com/en/articles/16762437-public-links-for-shared-chats)
* [Share a chat with specific people](https://support.claude.com/en/articles/16762496-share-a-chat-with-specific-people)
