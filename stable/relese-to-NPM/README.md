# Codefresh release-to-npm Plugin

The release-to-npm can be used to publish images to npm. 

## Usage

Set required and optional environment variable and add the following step to your Codefresh pipeline:

```yaml
---
version: '1.0'

steps:

  ...

     deploy_to_npm:  
      title: Publishing To Npm 
      image: codefresh/release-to-npm
      commands:
      - NPM_TOKEN=${{NPM_TOKEN}} npm run ci-publish 
  ...

```

## Environment Variables

- **required** `NPM_TOKEN` - token of npm account

for accessing the NPM_TOKEN please see https://docs.npmjs.com/private-modules/ci-server-config#getting-an-authentication-token


