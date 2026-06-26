<!-- source: https://claude.com/docs/claude-tag/admins/connections/salesforce -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Salesforce lets Claude read accounts, contacts, opportunities, and cases (and write, if you grant it) from any channel under the bundle’s scope. Add it as a custom credential with **Connect another app**, using the OAuth 2.0 JWT bearer flow; Salesforce has no preset button in the picker.

##  Create the credential in Salesforce

Create a Connected App configured for the JWT bearer flow, with a dedicated integration user assigned to it. Salesforce’s guide is at [help.salesforce.com](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_jwt_flow.htm).
You’ll need from Salesforce:

* The Connected App’s **Consumer Key** (client ID)
* The **private key** from the certificate you uploaded to the Connected App
* The integration user’s **username** (the JWT subject)
* Your org’s login URL (`https://login.salesforce.com` for production, `https://test.salesforce.com` for sandboxes, or your My Domain)

Assign the integration user a Permission Set scoped to the objects and fields Claude should reach. Read-only is the recommended starting point.

##  Add the connection to a bundle

In the bundle, click **Connect another app** at the bottom of the Credentials tab and choose the credential type below.

| Field | Value |
| Credential type | **OAuth 2.0 JWT bearer** |
| Issuer (iss) | The Connected App’s Consumer Key |
| Subject (sub, optional) | The integration user’s username |
| Private key (PEM) | The private key (PEM) from your certificate |
| Token URL | `https://login.salesforce.com/services/oauth2/token` (or your My Domain `/services/oauth2/token`) |
| Allowed websites | Your Salesforce instance host (for example `yourorg.my.salesforce.com`) |

The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

@Claude list the five most recently modified Opportunities in Salesforce.

Check the integration user’s login history in Salesforce Setup to confirm the call landed under that user.

* [Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state): what this connection adds

[PagerDuty](/docs/claude-tag/admins/connections/pagerduty)[Sentry](/docs/claude-tag/admins/connections/sentry)
