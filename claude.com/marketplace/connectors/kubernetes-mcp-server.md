<!-- source: https://claude.com/marketplace/connectors/kubernetes-mcp-server -->

More[Support (opens in new tab)](https://github.com/Flux159/mcp-server-kubernetes)[Privacy policy (opens in new tab)](https://www.linuxfoundation.org/legal/privacy-policy)

MCP Server that can connect to a Kubernetes cluster and manage it.

By default, the server loads kubeconfig from `~/.kube/config`.

The server will automatically connect to your current kubectl context. Make sure you have:

1. kubectl installed and in your PATH

2. A valid kubeconfig file with contexts configured

3. Access to a Kubernetes cluster configured for kubectl (e.g. minikube, Rancher Desktop, GKE, etc.)

4. Optional: Helm v3 installed and in your PATH.

You can verify your connection by asking Claude to list your pods or create a test deployment.

If you have errors open up a standard terminal and run `kubectl get pods` to see if you can connect to your cluster without credentials issues.

## Features

- [x] Connect to a Kubernetes cluster

- [x] Unified kubectl API for managing resources

- Get or list resources with `kubectl\_get`

- Describe resources with `kubectl\_describe`

- List resources with `kubectl\_get`

- Create resources with `kubectl\_create`

- Apply YAML manifests with `kubectl\_apply`

- Delete resources with `kubectl\_delete`

- Get logs with `kubectl\_logs`

- and more.

## Tools

* ping
* cleanup
* kubectl\_get
* kubectl\_describe
* kubectl\_apply
* kubectl\_delete
* kubectl\_create
* kubectl\_logs
* kubectl\_patch
* kubectl\_rollout
* kubectl\_scale
* kubectl\_context
* kubectl\_generic
* install\_helm\_chart
* upgrade\_helm\_chart
* uninstall\_helm\_chart
* explain\_resource
* list\_api\_resources
* node\_management
* exec\_in\_pod
* port\_forward
* stop\_port\_forward

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/8aa6ad728cfe811f74a7b65b92b44fe774b1fe17.jpg?w=128&fit=max&auto=format)

### [Atlassian MCP](https://claude.com/marketplace/connectors/atlassian)

Search, read and update Jira, Confluence, Bitbucket, Loom and other Atlassian apps with your existing Atlassian permissions.

[Add Atlassian MCP in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/53ca8822f4c024f9b358b1e44148a1dc3c616dbe.svg?w=128&fit=max&auto=format)

### [Gmail](https://claude.com/marketplace/connectors/gmail)

Draft replies, summarize threads, & search your inbox

[Add Gmail in Claude (opens in new tab)](https://claude.ai/directory/2701e52f-b826-4aaf-8b25-11f2a97c98b0 "Add in Claude")

![](https://assets.claude.com/646945a1897f9146e5221ee6ace82001a2e52f4d.svg?w=128&fit=max&auto=format)

### [Google Calendar](https://claude.com/marketplace/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://assets.claude.com/e476a6c2c2f961f5f2120482f37b1daafc1506d9.jpg?w=128&fit=max&auto=format)

### [Canva](https://claude.com/marketplace/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")

![](https://assets.claude.com/20c8443aa72ae4e4d77f923e6c33314713f965e8.svg?w=128&fit=max&auto=format)

### [Microsoft 365](https://claude.com/marketplace/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")
