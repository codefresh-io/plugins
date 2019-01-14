# Plugins

Plugins are created as files laid out in a particular directory tree,
then they can be packaged into versioned archives to be deployed.

This document explains the plugin format, and provides basic guidance for
building plugins.

## Plugin File Structure

A plugin is organized as a collection of files inside of a directory. The
directory name is the name of the plugin (without versioning information). Thus,
a plugin describing "Kubernetes Deployment" would be stored in the `kube-deploy/` directory.

Inside of this directory, Codefresh will expect a structure that matches this:

```
kube-deploy/
  plugin.yaml         # A YAML file containing information about the plugin
  LICENSE             # OPTIONAL: A plain text file containing the license for the plugin
  README.md           # OPTIONAL: A human-readable README file
  NOTES.md            # OPTIONAL: A plain text file containing short usage notes
```


## The plugin.yaml File

The `plugin.yaml` file is required for a plugin. It contains the following fields:

```yaml
image: The fully qualified name of the plugin Docker image (required)
tag: The plugin image tag (optional, default "latest")
version: SevVer 2 version for the plugin (required)
description: A single-sentence description of this plugin (optional)
keywords:
  - A list of keywords about this plugin (optional)
home: The URL of this plugin's home page (optional)
sources:
  - A list of URLs to source code for this plugin (optional)
maintainers: # (optional)
  - name: The maintainer's name (required for each maintainer)
    email: The maintainer's email (optional for each maintainer)
icon: A URL to an SVG or PNG image to be used as an icon (optional)
envs:
  - name: The variable name (required)
    type: required | optional | runtime (default to "optional")
    alias: alternative name, used inside the plugin container (optional)
    description: A short description for the variable (optional)
volumes:
  - name: The volume name
    required: true | false (default "false")
    description: A short description for attached volume
context:
  - kind: Codefresh context kind to inject automatically to the plugin
```


### Plugins and Versioning

Every plugin must have a version number. A version must follow the
[SemVer 2](http://semver.org/) standard. Codefresh Plugins uses version numbers as release markers. Plugins in repositories are identified by name plus version.

For example, an `kube-deploy` plugin whose version field is set to `version:
1.2.3` will be named:

```
kube-deploy-1.2.3.tgz
```

More complex SemVer 2 names are also supported, such as
`version: 1.2.3-alpha.1+ef365`. But non-SemVer names are explicitly
disallowed by the system.

### Predefined Variables

The following environment variables are pre-defined, are available to every plugin, and
cannot be overridden. 

- `CF_BUILD_TIMESTAMP`: Codefresh pipeline start execution timestamp
- `CF_SHORT_REVISION`: short Git commit SHA
- `CF_REVISION`: full Git commit SHA
- `CF_REPO_NAME`: Git repository name
- `CF_BRANCH_TAG_NORMALIZED`: default image tag for Codefresh CI pipeline 
- `CF_BRANCH`: Git branch name
- `CF_BUILD_URL`: URL to Codefresh pipeline log
- `CF_COMMIT_AUTHOR`: Git commit author
- `CF_VOLUME_PATH`: Codefresh shared context volume (default to `/codefresh/volume`)
- `CF_COMMIT_URL`: Git commit URL
- `CF_BRANCH_VERSION_NORMALIZED`: 
- `CF_COMMIT_MESSAGE`: Git commit message
- `CF_BUILD_ID`: Codefresh pipeline ID
- `CF_REPO_OWNER`: Codefresh pipeline owner
- `CF_BUILD_TRIGGER`: Codefresh pipeline trigger

### Predefined Volumes and Files

- `/codefresh/volume` - same volume mounted to all steps running in Codefresh pipeline
- `/codefresh/volume/env_vars_to_export` - a placeholder file to be filled with **exported** environment variables; any exported variable can be used in subsequent pipeline steps