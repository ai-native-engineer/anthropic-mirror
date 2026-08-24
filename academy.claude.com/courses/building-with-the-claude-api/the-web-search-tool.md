<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/the-web-search-tool -->

Lesson 31 of 67 · Building with the Claude APIThe web search tool

**Important note:** Your organization must enable the Web Search tool in the settings console before using it. You can find this setting here: [https://platform.claude.com/settings/privacy(opens in new tab)](https://platform.claude.com/settings/privacy)

Claude includes a built-in web search tool that lets it search the internet for current or specialized information to answer user questions. Unlike other tools where you need to provide the implementation, Claude handles the entire search process automatically - you just need to provide a simple schema to enable it.

![](https://academy.claude.com/assets/media/f1edc5de25d4a7012a5234100ec3f4c0b7e19dff55beb5188ab2fd847eecba51.png)

## Setting Up the Web Search Tool

To use the web search tool, you create a schema object with these required fields:

python

```
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 5
}
```

The `max_uses` field limits how many searches Claude can perform. Claude might do follow-up searches based on initial results, so this prevents excessive API calls. A single search returns multiple results, but Claude may decide additional searches are needed.

## How the Response Works

When Claude uses the web search tool, the response contains several types of blocks:

* **Text blocks** - Claude's explanation of what it's doing
* **ServerToolUseBlock** - Shows the exact search query Claude used
* **WebSearchToolResultBlock** - Contains the search results
* **WebSearchResultBlock** - Individual search results with titles and URLs
* **Citation blocks** - Text that supports Claude's statements

![](https://academy.claude.com/assets/media/a9c3f8db3229581f947e3413e39fb2dade885bdf4fcf5ee38cdc8877403d0bbf.png)

The response structure lets you see exactly what Claude searched for and which sources it found. Citations include the specific text Claude used to support its answers, along with the source URLs.

## Restricting Search Domains

You can limit searches to specific domains using the `allowed_domains` field. This is particularly useful when you want reliable, authoritative sources:

python

```
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 5,
    "allowed_domains": ["nih.gov"]
}
```

For example, when asking about medical or exercise advice, restricting to domains like PubMed (nih.gov) ensures you get evidence-based information rather than random blog content.

![](https://academy.claude.com/assets/media/e9e7159ab9e9897fde75dba1dd0c89e889aa76e43600922c6e132d4701e7e4ef.png)

## Rendering Search Results

The different block types in the response are designed for specific UI rendering:

* Render text blocks as regular content
* Display web search results as a list of sources at the top
* Show citations inline with the text, including the source domain, page title, URL, and quoted text

![](https://academy.claude.com/assets/media/cc9b802fe80ee655ec64e47e7fc881e8dc8078714bfcd536eeab5992ef94aea8.png)

This structure helps users understand how Claude arrived at its answers and provides transparency about the sources being used. The citation format makes it clear which specific information came from which sources, building trust in the AI's responses.

## Practical Usage

The web search tool works best for:

* Current events and recent developments
* Specialized information not in Claude's training data
* Fact-checking and finding authoritative sources
* Research tasks requiring up-to-date information

Simply include the schema in your tools array when making API calls, and Claude will automatically decide when a web search would help answer the user's question.
