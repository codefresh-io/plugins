# Codefresh Clair Plugin

Clair is an open source Docker Image securitu scanning server. For more information see here: https://github.com/coreos/clair/

There's an open source CLI tool for clair, called 'klar' that you can use to integrate secrurity scan into your pipeline. More info on klar: https://github.com/optiopay/klar

## Usage

Set environment variables described below, and run the command with the given image to scan:

```yaml
scan:
    image: 'codefresh/klar:master'
    commands:
      - /klar codefresh/helm:2.8.1
``` 

(in this example we are scanning the helm image tagged 2.8.1 under codefresh organization in Docker Hub)

## Environment Variables

The minimal setup is described below. Please see Klar documentation for additional configuration.

Name|Required|Description
---|---|---
CLAIR_ADDR|Yes|The address of the clair server
DOCKER_USER|No|Docker registry account name
DOCKER_PASSWORD|No|Docker registry account password

