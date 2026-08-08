<!-- source: https://support.claude.com/en/articles/8243635-our-approach-to-rate-limits-for-the-claude-api -->

Your rate limit depends on your usage tier, and is currently measured in three key metrics:

1. Requests per minute (RPM)
2. Input tokens per minute (ITPM)
3. Output tokens per minute (OTPM)

If you exceed any of these rate limits, you will get a 429 error describing which rate limit was exceeded, along with a `retry-after` header indicating how long to wait.

Rate limits are set at the organization level and depend on your usage tier. There are three usage tiers: Start, Build, and Scale. Accounts whose limits are managed with their account team are on a separate Custom tier. Higher tiers have higher rate limits.

You can view your organization's current tier and limits in the **[Claude Console](https://platform.claude.com)**. If you need higher limits, you can request them there once you're using at least 50% of your current limits.

For more about usage tiers and rate limits, see the **[Rate limits page in our Claude Platform Docs](https://docs.claude.com/en/api/rate-limits)**.

* [I’m encountering 429 errors, and I’m worried my rate limit is too low. What should I do?](https://support.claude.com/en/articles/8114527-i-m-encountering-429-errors-and-i-m-worried-my-rate-limit-is-too-low-what-should-i-do)
* [Cost and Usage Reporting in the Claude Console](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console)
* [How can I get higher rate limits on the Claude API?](https://support.claude.com/en/articles/10366389-how-can-i-get-higher-rate-limits-on-the-claude-api)
* [Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)
* [Claude Enterprise Admin API reference guide](https://support.claude.com/en/articles/15330651-claude-enterprise-admin-api-reference-guide)
