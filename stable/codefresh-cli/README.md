# Codefresh Cli Plugin

Use Codefresh Cli plugin to perform operations on your Codefresh resources

## Usage


```yaml
---
version: '1.0'

steps:

  ...

  annotate_image:
    image: codefresh/cli
    description: annotates image with metadata
    command: annotate image IMAGE_ID -a key1=value1 -a key2=value2

  run_pipeline:
    image: codefresh/cli
    description: run a pipeline
    command: run PIPELINE_ID -b master
  ...

```

## Environment Variables

- `CFCONFIG` - Path for cfconfig file path (default: ${HOME}/.cfconfig
