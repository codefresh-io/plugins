# Codefresh Plugins

Use this repository to submit official Plugins for Codefresh. Plugins are curated automated step definitions for Codefresh. For more information about using Codefresh, see its
[documentation](https://docs.codefresh.io). 

## How do I install these plugins?

Codefresh Plugins are available as plain Docker images. As long as Plugin Docker image is accessible, Codefresh can use it for its pipelines.

## How do I use plugins from the Incubator repository?

*TBD*

## Codefresh Plugin Format

Take a look at the [example plugin](#) for reference when you're writing your first few plugins.

The Plugin folder must contain `plugin.yaml` and `README.md` files.

Before contributing a Plugin, become familiar with the format. Note that the project is still under active development and the format may still evolve a bit.

## Repository Structure

This GitHub repository contains the source for the packaged and versioned plugins released in the [`gs://codefresh-plugins` Google Storage bucket](https://console.cloud.google.com/storage/browser/codefresh-plugins/) (the Plugins Repository).

The Plugins in the `stable/` directory in the master branch of this repository match the latest packaged Plugins in the Plugin Repository, though there may be previous versions of a Plugin available in that Plugin Repository.

The purpose of this repository is to provide a place for maintaining and contributing official Plugins, with CI processes in place for managing the releasing of Plugins into the Plugin Repository.

The Plugins in this repository are organized into two folders:
* stable
* incubator

Stable Plugins meet the criteria in the [technical requirements](CONTRIBUTING.md#technical-requirements).

Incubator Plugins are those that do not meet these criteria. Having the incubator folder allows plugins to be shared and improved on until they are ready to be moved into the stable folder. The plugins in the `incubator/` directory can be found in the [`gs://codefresh-plugins-incubator` Google Storage Bucket](https://console.cloud.google.com/storage/browser/codefresh-plugins-incubator).

In order to get a Plugin from incubator to stable, Plugin maintainers should open a pull request that moves the plugin folder.

## Contributing a Plugin

We'd love for you to contribute a Plugin that provides a useful automated step for Codefresh. Please read our [Contribution Guide](CONTRIBUTING.md) for more information on how you can contribute Plugins.

## Review Process

The following outlines the review procedure used by the Plugin repository maintainers. Github labels are used to indicate state change during the review process. 

* ***AWAITING REVIEW*** - Initial triage which indicates that the PR is ready for review by the maintainers team. All e2e tests must pass in-order to move to this state
* ***CHANGES NEEDED*** - Review completed by at least one maintainer and changes needed by contributor (explicit even when using the review feature of Github)
* ***CODE REVIEWED*** - The plugin structure has been reviewed and found to be satisfactory given the [technical requirements](CONTRIBUTING.md#technical-requirements) (may happen in parallel to UX REVIEWED)
* ***UX REVIEWED*** - The plugin installation UX has been reviewed and found to be satisfactory. (may happen in parallel to CODE REVIEWED)
* ***LGTM*** - Added ONLY once both UX/CODE reviewed are both present. Merge must be handled by someone OTHER than the maintainer that added the LGTM label. This label indicates that given a quick pass of the comments this change is ready to merge

### Stale Pull Requests

After initial review feedback, if no updates have been made to the pull request for 1 week, the `stale` label will be added. If after another week there are still no updates it will be closed. Please re-open if/when you have made the proper adjustments.

## Status of the Project

This project is still under active development, so you might run into [issues](https://github.com/codefresh-io/plugins/issues). If you do, please don't be shy about letting us know, or better yet, contribute a fix or feature.