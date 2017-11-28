# Import Docker Images Codefresh Plugin

Run single or multiple jenkins job from codefresh pipeline

## Environment Variables

- `JENKINS_USER`: jenkins username
- `JENKINS_TOKEN`: token
- `JENKINS_URL`: jenkins machine url
- `JENKINS_JOB`: jenkins job to run

Usage Example:

version: '1.0'
steps:
  RunJenkins:
   	title: Triggering Jenkins Job
    image: codefresh/cf-run-jenkins-job
    environment:
    - JENKINS_URL=http://<jenkins host>:<jenkins port>
    - JENKINS_USER=<jenkins user name>
    - JENKINS_TOKEN=<jenkins token>
    - JENKINS_JOB=<jenkins job name>
