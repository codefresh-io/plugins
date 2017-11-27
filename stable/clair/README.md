# Codefresh Clair Plugin

Use Codefresh [Clair](https://github.com/coreos/clair) plugin to scan your docker image and find security vulnerabilities.

## Usage

Set required and optional environment variable and add the following step to your Codefresh pipeline:

```yaml
---
version: '1.0'

steps:

  ...

  release_to_env:
    image: codefresh/plugin-clair:1.0.0

  ...

```

## Environment Variables

- **required** `CHART_NAME` - Helm chart name
- `TIMEOUT` - wait timeout (5min by default)
