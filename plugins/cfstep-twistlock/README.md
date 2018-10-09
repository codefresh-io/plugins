# Codefresh Twistlock Plugin

Dockerhub repo: https://hub.docker.com/r/codefresh/cfstep-twistlock/tags/

The Docker image uses the Twistlock API v2.3: https://twistlock.desk.com/customer/en/portal/articles/2912404-twistlock-api-2-3

Plugin that allow users to perform Twistlock Security Scans on images.

This plugin **does not** require access to Docker Daemon.


## Prerequisites:

- Codefresh Subscription - https://codefresh.io/
- Twistlock Subscription - https://www.twistlock.com/

## Options
These options are set as Environment Variables at your pipeline (either at Pipeline configuraion, and/or Step definition)
To use an ENVIRONMENT VARIABLE you need to add the variables to your Codefresh Pipeline and also to your codefresh.yaml.

| ENVIRONMENT VARIABLE | DEFAULT | TYPE | REQUIRED | DESCRIPTION |
|--|--|--|--|--|
| TL_CONSOLE_HOSTNAME | null | string | Yes | hostname/ip |
| TL_CONSOLE_PORT | null | string | Yes | port |
| TL_CONSOLE_USERNAME | null | string | Yes | username |
| TL_CONSOLE_PASSWORD | null | string | Yes | password |
| TL_COMPLIANCE_THRESHOLD | null | string | Yes | [ low, medium, high, critical ] sets the the minimal severity compliance issue that returns a fail exit code |
| TL_VULNERABILITY_THRESHOLD | null | string | Yes | [ low, medium, high, critical ] sets the minimal severity vulnerability that returns a fail exit code |
| TL_REGISTRY | null | string | Yes | Registry URL. (e.g.: docker.io, cfcr.io). This should match the Registry URL set at Twistlock Console |
| TL_IMAGE_NAME | null | string | Yes | The full image name (excluding the registry URL) (e.g.: myrepo/myimage) |
| TL_IMAGE_TAG | null | string | Yes | The tag of the image to scan. |

>  **Threshold description**
>
> - low: the most **restrictive**. When thresholds are set to this level, the scanning process will fail with any issue or vulnearability found.
> - critical: the most **permissive**. When thresholds are set to this level, the scanning process will fail only if a critical issue or vulnearability is found (or a combination of lower level vulnerabilities that summed up result in a risk score higher than 1000).



## How to use it (examples)

Summary: in this example, we're going to scan an image built by Codefresh.

The image's Dockerfile is defined in this sample repo: https://github.com/francisco-codefresh/twistlock_demo

In order for this to work, the registry to scan must be previously added to Twistlock Console.

Once the security scan finishes, we annote the image based on the Security Report created by Twistlock.

In our example pipeline, if the compliance and vulnerability thresholds are not exceeded (which means the scan doesn't fail), then, we push the resulting image to our final, curated, registry.

### Preparation step: Set up a pipeline with the following configuration
Now, create a pipeline associated to your repo, in this case, our demo repo is "twistlock_demo" (mentioned above)

#### Environment Variables (configured at Pipeline Configuration):

```
TL_CONSOLE_HOSTNAME=169.254.169.254
TL_CONSOLE_PORT=8083
TL_CONSOLE_USERNAME=myuser
TL_CONSOLE_PASSWORD=mypassword
TL_COMPLIANCE_THRESHOLD=critical
TL_VULNERABILITY_THRESHOLD=critical
```

For this example, we're being permissive (critical for both thresholds). Of course those values can be set to any of the other options.

### Example 1 - Scanning an image from Codefresh Docker registry
This is a great way to take advantage of the built-in registry provided by Codefresh (for free).
Since evey image built in Codefresh is automatically pushed to this registry, you don't need to worry for explicitly pushising the image to scan.


#### Configure the Codefresh registry in Twistlock
In your Twistlock dashboard go to `#!/defend/vulnerabilities/registry` . And add a new "registry settings" record.

These are the settings used for Codefresh Private Registry:

- Version: Docker Registry v2
- Registry: https://r.cf-cd.com *(notice this is not the common r.cfcr.io domain)*
- Repository name: <your_cf_account_name>/<image_repo> (e.g.: francisco-codefresh/myimage)
- Tag: <empty>
- Username: <your_codefresh_user_name>
- Password: <your_registry_token> (you can generate one at https://g.codefresh.io/user/settings)

#### Set up a pipeline with the following configuration

**Environment Variables (configured at Pipeline Configuration):**

```
TL_CONSOLE_HOSTNAME=169.254.169.254
TL_CONSOLE_PORT=8083
TL_CONSOLE_USERNAME=my_tl_user
TL_CONSOLE_PASSWORD=my_tl_password
TL_COMPLIANCE_THRESHOLD=critical
TL_VULNERABILITY_THRESHOLD=critical
```

For this example, we're being permissive (`critical` for both thresholds). Of course those values can be set to any of the other options.

**Pipeline YAML (codefresh.yml)**

```yaml
version: '1.0'
steps:
  BuildingDockerImage:
    title: Building Docker Image
    type: build
    image_name: franciscocodefresh/twistlockdemo
    tag: '${{CF_SHORT_REVISION}}'
    dockerfile: Dockerfile
      
  TLScan:
    title: Twistlock Scan
    image: codefresh/cfstep-twistlock
    environment:
      - TL_REGISTRY=https://r.cf-cd.com
      - TL_IMAGE_NAME=francisco-codefresh/franciscocodefresh/twistlockdemo
      - TL_IMAGE_TAG=${{CF_SHORT_REVISION}}
    on_success:
      metadata:
        set:
          - ${{BuildingDockerImage.imageId}}:
            - SECURITY_SCAN: true
    on_fail: 
      metadata: 
        set: 
          - ${{BuildingDockerImage.imageId}}: 
            - SECURITY_SCAN: false     
  # If image scan (previous step) fails, the build will fail, thus the image won't be pushed to the curated registry
  # If image scan succeeds, the image will be pushed to the curated registry 
  PushingDockerRegistry:
    title: Pushing to FINAL Docker Registry (curated registry of scanned images)
    type: push
    candidate: '${{BuildingDockerImage}}'
    image_name: franciscocodefresh/twistlockdemo
    tags: 
      - '${{CF_SHORT_REVISION}}'
```

### Example 2 - Scanning an image from a temporary external registry
In this example, we are going to use Docker Hub as our temporary registry, which can be considered as a "*Registry of unscanned images*" (to be scanned). Once there, we can initiate the scan in Twistlock console.

#### Configure the registry to scan in Twistlock

In your Twistlock dashboard go to `#!/defend/vulnerabilities/registry` . And add a new "registry settings" record.

These are the settings used:

- Version: Docker Registry v2
- Registry: docker.io
- Repository name: franciscocodefresh/twistlockdemo-temp
- Tag: <empty>
- Username: <your_user_name>
- Password: <your_password>

#### Set up a pipeline with the following configuration

**Environment Variables (configured at Pipeline Configuration):**

```
TL_CONSOLE_HOSTNAME=169.254.169.254
TL_CONSOLE_PORT=8083
TL_CONSOLE_USERNAME=myuser
TL_CONSOLE_PASSWORD=mypassword
TL_COMPLIANCE_THRESHOLD=critical
TL_VULNERABILITY_THRESHOLD=critical
```

For this example, we're being permissive (`critical` for both thresholds). Of course those values can be set to any of the other options.

**Pipeline YAML (codefresh.yml)**

```yaml
version: '1.0'
steps:
  BuildingDockerImage:
    title: Building Docker Image
    type: build
    image_name: franciscocodefresh/twistlockdemo
    tag: '${{CF_SHORT_REVISION}}'
    dockerfile: Dockerfile

  PushingToTempDockerRegistry:
    title: Pushing to Temporal Docker Registry (for unscanned images -> to be scanned)
    type: push
    candidate: '${{BuildingDockerImage}}'
    image_name: franciscocodefresh/twistlockdemo-temp
    tags: 
      - '${{CF_SHORT_REVISION}}'
      
  TLScan:
    title: Twistlock Scan
    image: codefresh/cfstep-twistlock
    environment:
      - TL_REGISTRY=docker.io
      - TL_IMAGE_NAME=franciscocodefresh/twistlockdemo-temp
      - TL_IMAGE_TAG=${{CF_SHORT_REVISION}}
    on_success:
      metadata:
        set:
          - ${{BuildingDockerImage.imageId}}:
            - SECURITY_SCAN: true
    on_fail: 
      metadata: 
        set: 
          - ${{BuildingDockerImage.imageId}}: 
            - SECURITY_SCAN: false     

  PushingDockerRegistry:
    title: Pushing to FINAL Docker Registry (curated registry of scanned images)
    type: push
    candidate: '${{BuildingDockerImage}}'
    image_name: franciscocodefresh/twistlockdemo
    tags: 
      - '${{CF_SHORT_REVISION}}'
```
