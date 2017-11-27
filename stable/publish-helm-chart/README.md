# Codefresh Helm Plugin

Use Codefresh [Helm](https://helm.sh) plugin to publish a Helm chart to repository.

## Usage

Set required and optional environment variable and add the following step to your Codefresh pipeline:

```yaml
---
version: '1.0'

steps:

  ...

  publish_to_repo:
    image: codefresh/plugin-publish-helm-to-repo:0.1.2

  ...

```

## Environment Variables

- **required** `CHART_NAME` - Helm chart name
- **required** `CHART_REPO_URL` - Helm chart repository URL
- `CHART_VERSION` - application chart version to install
- `DEBUG` - print verbose output