# Codefresh plugins

Codefresh Plugins are Docker images made especially for use in a Codefresh freestyle step. Each plugin facilitates a common task that would otherwise by difficult to achieve.
See each plugin readme for more info and usage instructions.

## Plugins

| Plugin| Author| Description| Tags|
| --- | --- | --- | --- |
| [Codefresh Cli](codefresh-cli/README.md) | Operate on Codefresh resources | `cli` `codefresh`|
| [Deploy Helm](helm-legacy/README.md)| [Deprecated - see Incubator/helm instead] Deploy a Helm chart| `kubernetes` `helm`|
| [Slack](slack/README.md)| Send message to slack| `slack` `notify`|
| [Deploy to ECS](ecs-deploy/README.md)| Deploy docker image to ECS| `ecs` `deploy` `containers` `aws`                         |
| [Deploy Kompose](kompose/README.md)| Deploy Docker Compose to Kubernetes cluster with Kubernetes [Kompose](http://kompose.io) | `docker` `docker-compose` `kompose` `deploy` `kubernetes` |
| [GitHub PR](github-pr/README.MD)| Creates pull request to GitHub | `github`  |
| [Run Jenkins Jobs](https://github.com/codefresh-io/plugins/tree/master/stable/run-jenkins-job/README.md)| Run jenkins job from codefresh pipeline| `jenkins` `job`|
| [Deploy to DCOS](dcos-app-deploy/README.md) | Deploy application image to DC/OS cluster | `dcos` `deploy` `containers` |
| [Interact with Jira](https://github.com/codefresh-io/plugins/tree/master/stable/jira/README.md)|@antweiss | Interact with Jira from codefresh pipelines| `jira` `workflow`|
| [release to npm](release-to-NPM/README.md) | Release npm modules from a pipeline | `npm` |
| [Twistlock](twistlock-scan) | Security scanning of docker images using Twistlock | `security` |
| [Helm](helm/README.md) | Deploy Helm charts | `kubernetes` `helm`|
| [Clair](clair/README.md) |  Security scanning of Docker images using Clair | `security` |
| [Import Docker Images](import-docker-images/README.md) | Import Docker images metadata into Codefresh| `docker` `codefresh`|
| [Deploy Kompose](kompose/README.md)| Deploy Docker Compose to Kubernetes cluster with Kubernetes Kompose | `docker` `docker-compose` `kompose` `deploy` `kubernetes` |
