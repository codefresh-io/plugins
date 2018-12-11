# Docker build using Azure ACR


## Run locally
`docker run -it codefresh/cf-azure-builder`
```
NAME:
   cf-azure-builder

DESCRIPTION:
   Build 

## Mandatory Parameters:

    IMAGE     - Image name
    TAG    - Tag name
    ACR_NAME   - ACR registry name
    APP_ID     - Azure service principal application id
    PASSWORD   - Azure service principal password
    TENANT     - Azure ad tenant id
    DOCKERFILE_PATH - Dockerfile path (default - working_dir/Dockerfile)

## Usage Example:

version: '1.0'
steps:
  cf-az-build:
    image: codefresh/cf-azure-builder
    environment:
      - IMAGE=<image name>
      - TAG=<tag name>
      - ACR_NAME=<acr registry name>
      - APP_ID=<azure service principal application id>
      - PASSWORD=<azure service principal password>
      - TENANT=<azure ad tenant id>
      - DOCKERFILE_PATH=<dockerfile path>

