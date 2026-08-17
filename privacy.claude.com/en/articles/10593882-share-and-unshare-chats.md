<!-- source: https://privacy.claude.com/en/articles/10593882-share-and-unshare-chats -->

# Share and unshare chats

June 15, 2026

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

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1786926600&signature=e7ce1d17f22cb9cc2b767ee5cd5b0720e9460529c6837ba7c3a7fe930a56815b&req=dSklF894lIheWvMW1HO4zWn5HzUUYENtc9cNIYuX0GF3Q3NlgpHY%2FAsbm3Rd%0A%2F%2BJzbg3UNU4GSIIKpQ0%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1786926600&signature=e7ce1d17f22cb9cc2b767ee5cd5b0720e9460529c6837ba7c3a7fe930a56815b&req=dSklF894lIheWvMW1HO4zWn5HzUUYENtc9cNIYuX0GF3Q3NlgpHY%2FAsbm3Rd%0A%2F%2BJzbg3UNU4GSIIKpQ0%3D%0A)

This will open a **Shared chats** modal listing the title, date shared, and link to each chat, allowing you to easily review and access all your previously-shared content. From here, you also have the option to click “Unshare” next to each listed chat to revoke access to the last snapshot you shared:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1786926600&signature=42dcfbbbff32e6dec1d49b60279363dc1ce1c08e3258910002fc2e36f2c1137f&req=dSYlEst6noleWfMW1HO4ze44eCFolhQ4guvTv9woD7aamMEXIB2ywIt4SAHU%0AQXG7T9IPB1yRZqdls%2BM%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1786926600&signature=42dcfbbbff32e6dec1d49b60279363dc1ce1c08e3258910002fc2e36f2c1137f&req=dSYlEst6noleWfMW1HO4ze44eCFolhQ4guvTv9woD7aamMEXIB2ywIt4SAHU%0AQXG7T9IPB1yRZqdls%2BM%3D%0A)

If you don’t have any shared chat snapshots, the **Shared chats** modal will show “No shared content found”:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1786926600&signature=22c6ce94a40d079f3b43fa6b2cd853991f917b97c0aab3c8e8caa6e4c89a75c8&req=dSYlEst6nolfUfMW1HO4zdaFncN9g4%2B3DeZsm0Gz1HuyEfjMs5%2F9ztjy8ZjI%0APSP2ui2U%2BBxBHlJr3NI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1786926600&signature=22c6ce94a40d079f3b43fa6b2cd853991f917b97c0aab3c8e8caa6e4c89a75c8&req=dSYlEst6nolfUfMW1HO4zdaFncN9g4%2B3DeZsm0Gz1HuyEfjMs5%2F9ztjy8ZjI%0APSP2ui2U%2BBxBHlJr3NI%3D%0A)

* [Deleting commercial Anthropic accounts](https://privacy.claude.com/en/articles/7996865-deleting-commercial-anthropic-accounts)
* [Is my data used for model training?](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)
* [Business Associate Agreements (BAA) for Commercial Customers](https://privacy.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)
* [How Do You Use Personal Data in Model Training?](https://privacy.claude.com/en/articles/10023555-how-do-you-use-personal-data-in-model-training)
* [Is my data used for model training?](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)
