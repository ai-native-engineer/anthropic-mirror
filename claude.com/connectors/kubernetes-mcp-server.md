<!-- source: https://claude.com/connectors/kubernetes-mcp-server -->

[Skip to main content](#main-content)

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

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://drive.google.com&size=64)

### [Google Drive](https://claude.com/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://mail.google.com&size=64)

### [Gmail](https://claude.com/connectors/gmail)

Draft replies, summarize threads, & search your inbox

[Add Gmail in Claude (opens in new tab)](https://claude.ai/directory/2701e52f-b826-4aaf-8b25-11f2a97c98b0 "Add in Claude")

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://calendar.google.com&size=64)

### [Google Calendar](https://claude.com/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=canva.com&sz=96)

### [Canva](https://claude.com/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")

![](https://support.healthdataavatar.com/HDA-square.svg)

### [Health Data Avatar (HDA)](https://claude.com/connectors/health-data-avatar-hda)

Trending

Your complete health history structured for Claude

[Add Health Data Avatar (HDA) in Claude (opens in new tab)](https://claude.ai/directory/ebacb52d-dedb-424a-981c-3f6a14495676 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=microsoft.com&sz=96)

### [Microsoft 365](https://claude.com/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")
