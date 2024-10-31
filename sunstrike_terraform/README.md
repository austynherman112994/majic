

Set the Following:

``` bash
export KUBE_CONFIG_PATH=~/.kube/config
```


This works for some reason even though tf times out

``` bash
helm upgrade     --values /home/aherman/Desktop/majic/sunstrike_terraform/helm/pulsar/values-minikube.yaml     --namespace sunstrike     pulsar apache/pulsar
```


```bash
kubectl get secret --namespace sunstrike grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

```


http://loki-gateway.sunstrike.svc.cluster.local
