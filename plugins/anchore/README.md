# Codefresh Anchore Plugin

Anchore is a service that analyzes Docker images and generates a detailed manifest of the image, a virtual ‘bill of materials’ that includes official operating system packages, unofficial packages, configuration files, and language modules and artifacts. Anchore policies can they be defined to govern security vulnerabilities, package whitelists and blacklists, configuration file contents, presence of credentials in image, manifest changes, exposed ports or any user defined checks. These policies can be deployed site wide or customized for specific images or categories of applications.

For more information view the github repo here: https://github.com/anchore/anchore-engine

## Prerequisites

- Codefresh subscription
- Running Anchore Engine service

### Reference

- Example `codefresh.yml`: https://raw.githubusercontent.com/valancej/plugins/master/plugins/anchore/codefresh.yml
- Github repo containing Dockerfile: https://github.com/valancej/node_critical_fail
- Anchore Documentation: https://anchore.freshdesk.com/support/home
- Anchore CLI Image: https://hub.docker.com/r/anchore/engine-cli/

## Example

In this example, we will scan an image built by Codefresh. Depending on the result of the Anchore policy evaluation, we will choose to push the image to Dockerhub or not. 

### Setup

The example setup is described below. 

### Environment Variables

These environment variables can be set within Codefresh pipeline configuration.

Name|Required|Description
---|---|---
ANCHORE_CLI_URL|Yes|The address of the Anchore server
ANCHORE_CLI_USER|Yes|Anchore account name
ANCHORE_CLI_PASS|Yes|Anchore account password
ANCHORE_FAIL_ON_POLICY|No|Fail build if policy evaluation fails
ANCHORE_CLI_IMAGE|Yes|Image built and scanned

### Codefresh.yml

```yaml
version: '1.0'
steps:
  MyDockerImage:
    title: Building Docker Image
    type: build
    image_name: ${{QA_IMAGE}}
  ScanMyImage:
    title: Scanning Docker Image
    image: anchore/engine-cli:latest
    env:
      - ANCHORE_CLI_IMAGE=${{QA_IMAGE}}
      - ANCHORE_CLI_USER=user
      - ANCHORE_CLI_PASS=password
      - ANCHORE_CLI_URL=http://anchore-engine::8228/v1
      - ANCHORE_CLI_FAIL_ON_POLICY=true
```