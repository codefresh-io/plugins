# Codefresh Twistlock Plugin

Dockerhub repo: https://hub.docker.com/r/codefresh/cfstep-twistlock/tags/

The Docker image uses the Twistlock API v2.3: https://twistlock.desk.com/customer/en/portal/articles/2912404-twistlock-api-2-3

Plugin that allow users to perform Twistlocl Security Scans on their images.

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



## How to use it (example)

Summary: in this example, we're going to scan an image built by Codefresh.

The image's Dockerfile is defined in this sample repo: https://github.com/francisco-codefresh/twistlock_demo

For scanning purposes, the image will be pushed to a temporary registry, which can be considered as a "Registry of unscanned images". Once there, we can initiate the scan in Twistlock console.

In order for this to work, the registry to scan must be previously added to TwistlocK Console.

Once the security scan finishes, we annote the image based on the Security Report created by Twistlock.

In our example pipeline, if the compliance and vulnerability thresholds are not exceeded, then, we push the resulting image to our final, curated, registry.

### Configure the registry to scan in Twistlock

In your Twistlock dashboard go to `#!/defend/vulnerabilities/registry` . And add a new "registry settings" record.

In this case, we are going to use Docker Hub as our temporary registry. And these are the settings used:

- Version: Docker Registry v2
- Registry: docker.io
- Repository name: franciscocodefresh/twistlockdemo-temp
- Tag: <empty>
- Username: <your_user_name>
- Password: <your_password>

### Set up a pipeline with the following configuration

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

#### Pipeline YAML (Codefresh.yml)

```yaml
version: '1.0'
steps:
  BuildingDockerImage:
    title: Building Docker Image
    type: build
    image_name: franciscocodefresh/twistlockdemo
    working_directory: ./
    tag: '${{CF_SHORT_REVISION}}'
    dockerfile: Dockerfile

  PushingToTEMPDockerRegistry:
    title: Pushing to Temporal Docker Registry (for unscanned images -> to be scanned)
    type: push
    candidate: '${{BuildingDockerImage}}'
    image_name: franciscocodefresh/twistlockdemo-temp
    tags: 
      - '${{CF_SHORT_REVISION}}'
      
  TL_Scan:
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



