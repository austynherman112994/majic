

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



Services
```aiignore

minikube service redis-master -n sunstrike --url
minikube service pulsar-proxy -n sunstrike --url
```

For pulsar proxy run tunnel [https://minikube.sigs.k8s.io/docs/handbook/accessing/](https://minikube.sigs.k8s.io/docs/handbook/accessing/)
```
minikube tunnel
kubeclt get svc -n sunstrike
```
Then use the external ip of the proxy as the ip to connect
