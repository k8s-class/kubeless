# Install CLI
```
wget https://github.com/kubeless/kubeless/releases/download/v1.0.0-alpha.8/kubeless_linux-amd64.zip
unzip kubeless_linux-amd64.zip
sudo mv bundles/kubeless_linux-amd64/kubeless /usr/local/bin
rm -r bundles/
```

# Deploy kubeless
```
kubectl create ns kubeless
kubectl create -f https://github.com/kubeless/kubeless/releases/download/v1.0.0-alpha.8/kubeless-v1.0.0-alpha.8.yaml 
```

# Example function

## python
```
kubeless function deploy hello --runtime python2.7 \
                               --from-file python-example/example.py \
                               --handler test.hello
```
## NodeJS
```
kubeless function deploy myfunction --runtime nodejs6 \
                                --dependencies node-example/package.json \
                                --handler test.myfunction \
                                --from-file node-example/example.js
```

# Commands

## List Function
```
kubeless function ls
```


## Expose function
```
* Only deploy the ingress controller if you do not have an ingress controller deployed. 
kubectl create -f nginx-ingress-controller-with-elb.yml

kubeless trigger http create myfunction --function-name myfunction --hostname myfunction.aheadlabs.io
kubeless trigger http create myfunction --function-name hello --hostname hello.aheadlabs.io
```


# PubSub
## Kafka Installation
```
export RELEASE=$(curl -s https://api.github.com/repos/kubeless/kafka-trigger/releases/latest | grep tag_name | cut -d '"' -f 4)
kubectl create -f https://github.com/kubeless/kafka-trigger/releases/download/$RELEASE/kafka-zookeeper-$RELEASE.yaml
```

### Trigger and publish

```
kubeless trigger kafka create test --function-selector created-by=kubeless,function=hello --trigger-topic hello
kubeless topic publish --topic hello --data "this message will sent to output"

```

## Call Function
```
kubeless function call myfunction --data 'This is some data'
kubeless function call hello --data 'This is some test data'
```
