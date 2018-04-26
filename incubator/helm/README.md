# Codefresh Helm Plugin

You can always use the `helm` command line in a freestyle step, like any other command line tool, but for Helm, You might want to check out out helm deployment step.

## Usage

Set required and optional environment variable and add the following step to your Codefresh pipeline like so:

```yaml
Helm Upgrade:
    image: 'codefresh/cfstep-helm:2.8.0'
``` 

## Environment Variables

Name|Required|Description
---|---|---
KUBE_CONTEXT|required|Kubernetes context to use (the name of the cluster as configured in Codefresh)
CHART_NAME|required|Helm chart name to release (path to chart folder, or name of packaged chart)
RELEASE_NAME|required|Helm release name
NAMESPACE|required|target Kubernetes namespace
TILLER_NAMESPACE|required|Kubernetes namespace where tiller is at
CHART_VERSION|required|application chart version to install
CHART_REPO_URL|required|Helm chart repository URL (overriden by injected Helm repository context)
CUSTOMFILE_|optional|Values file to provide to Helm (as --file). see usage information below.
CUSTOM_|optional|Value to provide to Helm (as --set). see usage information below.
CMD_PS|optional|Command Postscript - this will be appended to the command string. Can be used to set additional parameters supported by the command but not exposed as variables.

## Helm Values

To supply value file, add an environment variable with the name prefix of `CUSTOMFILE_` (case *in*sensitive), and the value should point to an existing values file.
To override specific values, add an environment variable with the name prefix of `CUSTOM_` (case *in*sensitive), and replace any `.` characters in the name with `_`. The value should be the value for the variable.

Examples:
```text
CUSTOM_myimage_pullPolicy=Always
# Codefresh Helm plugin will add option below to the 'helm update --install' command
--set myimage.pullPolicy=Always

CUSTOMFILE_prod='values-prod.yaml'
# Codefresh Helm plugin will add option below to the 'helm update --install' command
--values values-prod.yaml
```

If a variable contains a `_`, replace the `_` character with `__`.

```text
custom_env_open_SOME__VAR__REF=myvalue
# translates to ...
--set env.open.SOME_VAR_REF=myvalue
```

## Kubernetes Configuration

Add Kubernetes integration to Codefresh: `> Account Settings > Integration > Kubernetes`. From now on, you can use added Kubernetes cluster in Codefresh pipeline, addressing its context by the name you see in `Clusters` menu.

## Helm Reposiroty Configuration

To install a chart from a private repository, add your repository in Codefresh, and inject it into the pipeline by selecting it under "Environment Variables" -> "Import from shared configuration".
Then you can simple select the chart with the `CHART_NAME` variable. No additional configuration needed.
