# Codefresh Helm Plugin

Use Codefresh [Helm](https://helm.sh) plugin to deploy a Helm chart into specified (by context) Kubernetes cluster. 

## Usage

Set required and optional environment variable and add the following step to your Codefresh pipeline:

```yaml
---
version: '1.0'

steps:

  ...

  release_to_env:
    image: codefresh/plugin-helm

  ...

```

## Environment Variables

- **required** `CHART_NAME` - Helm chart name
- **required** `RELEASE_NAME` - Helm release name
- **required** `KUBE_CONFIG` - Kubernetes configuration file (single line base64 encoded string)
- `NAMESPACE` - target Kubernetes namespace
- `CHART_VERSION` - application chart version to install
- `CHART_REPO_URL` - Helm chart repository URL
- `DRY_RUN` - do a "dry run" installation (do not install anything, useful for Debug)
- `DEBUG` - print verbose install output
- `WAIT` - block step execution till installation completed and all Kubernetes resources are ready
- `TIMEOUT` - wait timeout (5min by default)

