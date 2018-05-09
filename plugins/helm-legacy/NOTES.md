## Kubernetes Configuration

Currently, you need to pass a Kubernetes configuration file as a single line string, using `KUBE_CONFIG` environment variable. Please, make sure to use a valid [Kubernetes configuration file](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) with at least one context and `current-context` set to one you want to use.

Use following command to generate single line, base 64 encoded string:

```sh
$ KUBE_CONFIG=$(cat ~/.kube/my_cluster_config | base64 -e | tr -d '\r\n')
```