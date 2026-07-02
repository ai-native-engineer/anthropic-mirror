<!-- source: https://claude.com/docs/connectors/verification -->

The [Connectors Directory](/docs/connectors/directory) includes connectors built by Anthropic and by third-party developers. Each connector shows how much Anthropic has reviewed it, so you can decide what to connect to.

##  Verified

Anthropic has reviewed this connector for quality and security. Verified connectors show a checkmark next to their name.

##  Community

A third-party developer built this connector. It passed Anthropic’s automated checks, but Anthropic has not reviewed it in depth.
Community connectors show a “Community” label in the directory and in [Settings > Connectors](https://claude.ai/settings/connectors). Before you connect one, Claude shows a reminder that it has not been reviewed in depth.

##  Custom

You added this connector yourself. Anthropic has not reviewed it.
See [custom connectors](/docs/connectors/custom/remote-mcp) to learn how to add one.

##  The directory is optional

The directory is a catalog, not a separate kind of connector. Connectors in the directory and custom connectors you add yourself use the same technology and work the same way.
If you have a connector’s URL, it can be added as a custom connector. A connector does not need to be in the directory for you to use it.
Listing a connector in the directory makes it discoverable by other people and gives it a review label (a checkmark if Anthropic has verified it, or “Community” if it passed Anthropic’s automated checks). It does not change what the connector can do. See [directory vs custom](/docs/connectors/building/directory-vs-custom) for a detailed comparison.

##  Advice for all third-party connectors

Whatever the label, this advice applies to any connector built by someone other than Anthropic:

* Only connect to servers from developers and organizations you trust.
* A connector’s developer controls which tools it exposes and can change them at any time.
* Anthropic does not run a third-party connector’s servers and does not control how it handles your data.
* Carefully review requested permission scopes during authentication.
* Be aware of prompt injection risks; Claude has built-in protections.
* Monitor for unexpected changes in tool behavior.

For more, see [security and privacy](/docs/connectors/custom/remote-mcp#security-and-privacy).

##  List your own connector

If you build connectors and want yours in the directory, start with the [review criteria](/docs/connectors/building/review-criteria) and the [submission guidelines](/docs/connectors/building/submission).

[Connectors directory](/docs/connectors/directory)[Remote MCP](/docs/connectors/custom/remote-mcp)
