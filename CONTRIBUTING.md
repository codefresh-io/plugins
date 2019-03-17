# Contributing Guidelines

The Codefresh Plugins project accepts contributions via GitHub pull requests. This document outlines the process to help get your contribution accepted.

### How to Contribute a Plugin

1. Develop and test your plugin
2. Create a github repository for your plugin containing the following:
  - all the source files needed to create the plugin
  - a Dockerfile that describes how to package your plugin in a Docker image
  - a plugin.yaml file (see further for the schema)
  - an example.yaml file that show how to use your plugin in a Codefresh pipeline
3. Ensure your Plugin follows the [technical](#technical-requirements) and [documentation](#documentation-requirements) guidelines, described below
4. Fork this repository (codefresh-io/plugins)
4. Update [plugin submission file](submit.json) with your plugin properties
5. Submit a pull request

***NOTE***: In order to make testing and merging of PRs easier, please submit changes to multiple plugins in separate PRs.

#### Technical requirements

* The Plugin with all its dependencies should be packaged into a single Docker container
* The Plugin code must be available as public GitHub repository
* It should be possible to build the Plugin using single `Dockerfile` (use *multi-stage* build if needed)
* The Plugin Docker Image should not have any major security vulnerabilities
* It should be possible to run the Plugin with simple `docker run` command, providing all required environment variables and volumes

#### Documentation requirements

* Must include an in-depth `README.md`, including:
    * Short description of the Plugin
    * Customization: explaining all required variables and their defaults

### Merge approval and release process

A Codefresh Plugins maintainer will review the Plugin submission, and start a validation job in the CI to verify the technical requirements of the Plugin. A maintainer may add "LGTM" (Looks Good To Me) or an equivalent comment to indicate that a PR is acceptable. Any change requires at least one LGTM. No pull requests can be merged until at least one maintainer signs off with an LGTM.

Once the Plugin has been merged, the release job will automatically run in the CI to package and release the Plugin in the [`gs://codefresh-plugins` Google Storage bucket](https://console.cloud.google.com/storage/browser/codefresh-plugins/).

### Support Channels

Whether you are a user or contributor, official support channels include:

- GitHub issues: https://github.com/codefresh-io/plugins/issues
- Slack: *TBD*

Before opening a new issue or submitting a new pull request, it's helpful to search the project - it's likely that another user has already reported the issue you're facing, or it's a known issue that we're already aware of.
