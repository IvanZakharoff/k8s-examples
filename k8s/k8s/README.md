Этот пример показывает, как добавить запись для домена example.com, который указывает на IP-адрес 192.168.1.100, в файл конфигурации CoreDNS.

Создайте файл конфигурации CoreDNS: Создайте файл coredns-custom.yaml с следующим содержимым:
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns-custom
  namespace: kube-system
data:
  custom.server: |
    example.com:53 {
      forward . 192.168.1.100
    }
В этом примере мы добавляем новый блок сервера custom.server, который перенаправляет запросы для домена example.com на IP-адрес 192.168.1.100.

Примените изменения: Используйте команду kubectl apply -f coredns-custom.yaml для применения изменений к вашему кластеру Kubernetes.

Namespace

apiVersion: v1
kind: Namespace
metadata:
 name: development
 labels:
    name: development

Secret 

apiVersion: v1
kind: Secret
metadata:
 name: mysecret
type: Opaque
data:
 username: YWRtaW4= # base64 encoded 'admin'
 password: MWYyZDFlMmU2N2Rm # base64 encoded '1f2d1e2e67df'