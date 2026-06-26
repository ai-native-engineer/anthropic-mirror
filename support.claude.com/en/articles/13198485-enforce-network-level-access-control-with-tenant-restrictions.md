<!-- source: https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions -->

# Enforce network-level access control with Tenant Restrictions

Tenant Restrictions are available for members of Enterprise plans and Console organizations.

Tenant Restrictions enable IT administrators on Enterprise plans to enforce network-level access control for Claude. This feature ensures that users on corporate networks can only access approved organizational accounts, preventing unauthorized use of personal accounts.

## How it works

When enabled, your network proxy injects an HTTP header into requests to Claude. Anthropic validates this header and blocks access from any organization not in the allowed list.

**Supported authentication methods:**

* Web access ([claude.ai](http://claude.ai))
* Desktop / App Access
* API key authentication
* OAuth token authentication

## Header format

```
anthropic-allowed-org-ids: <org-uuid-1>,<org-uuid-2>,...
```

* Comma-delimited list of organization UUIDs
* No spaces between values

**Example:**

```
anthropic-allowed-org-ids: 550e8400-e29b-41d4-a716-446655440000,6ba7b810-  
9dad-11d1-80b4-00c04fd430c8
```

## Configuration steps

### 1. Find your organization UUID

Members of Enterprise plans can find this in two different places:

1. Navigate to **[Settings > Account](https://claude.ai/settings/account)** and find **Organization ID**.
2. Navigate to **[Organization settings > Organization](https://claude.ai/admin-settings/organization)** and scroll down to the bottom of the page to locate **Organization ID**.

Members of Console organizations can find this in **[Settings > Organization](https://platform.claude.com/settings/organization)**.

### 2. Configure your network proxy

Configure your proxy to inject the header for Claude traffic:

```
Rule: Claude Tenant Restriction  
Application: claude.ai, api.anthropic.com, claude.com, anthropic.com  
Action: Inject Header  
Header Name: anthropic-allowed-org-ids  
Header Value:   
TLS Inspection: Required
```

### 3. Test your configuration

From restricted network, test with your org's API key:

```
curl https://api.anthropic.com/v1/messages \  
  -H "x-api-key: $CLAUDE_API_KEY" \  
  -H "anthropic-version: 2023-06-01" \  
  -H "content-type: application/json" \  
  -d '{"model":"claude-sonnet-4-6","max_tokens":1024,"messages":  
 [{"role":"user","content":"Hello"}]}'
```

## Error response

When access is blocked, users receive the following error:

```
{  
  "type": "error",  
  "error": {  
    "type": "permission_error",  
    "message": "Access restricted by network policy. Contact IT Administrator.",  
    "error_code": "tenant_restriction_violation"  
  }  
}
```

## Supported proxy platforms

* Zscaler ZIA (Cloud App Control policies)
* Palo Alto Prisma Access (SaaS App Management)
* Cato Networks (Tenant Restriction policy)
* Netskope (Header Insertion rules)
* Generic HTTPS proxies with header injection capability

## Use cases

|  |  |
| --- | --- |
| **Scenario** | **Header Value** |
| Single Organization | `<your-org-uuid>` |
| Multiple Organizations (Partners) | `<org-uuid-1>,<org-uuid-2>` |

## Security benefits

* **Data Loss Prevention:** Block personal account usage from corporate networks.
* **Compliance:** Enforce data residency and access policies.
* **Shadow IT Control:** Prevent unauthorized Claude usage.
* **Audit Trail:** Complete visibility into access attempts.

## Backward compatibility

* No impact to networks without tenant restrictions configured.
* Standard authentication continues for unmanaged networks.
* Existing API key authentication remains unchanged.

[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)[Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
