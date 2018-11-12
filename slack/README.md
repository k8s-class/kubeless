# SLACK example

Trigger the function and it send a message to your SLACK channel.

You need a SLACK_API_TOKEN

## Store token

Store your SLACK API TOKEN in a Kubernetes secret

```
kubectl create secret generic slack --from-literal=token=<your_token>
```

## Launch the function

Edit `bot.py` to specify the proper channel.

```
make slack
```

## Send a slack message

With a local proxy running:

```
kubeless function call slack --data '{"msg":"This is a message to SLACK"}'
```
```
kubeless function call slack --data '{"msg":"This is a message to SLACK"}'
{"headers": {"Content-Length": "170", "X-XSS-Protection": "0", "Access-Control-Allow-Origin": "*", "X-Via": "haproxy-www-g0p9", "Expires": "Mon, 26 Jul 1997 05:00:00 GMT", "Pragma": "no-cache", "Date": "Mon, 12 Nov 2018 15:15:04 GMT", "X-Cache": "Miss from cloudfront", "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload", "Server": "Apache", "X-Slack-Exp": "1", "Connection": "keep-alive", "X-Amz-Cf-Id": "zAv7h0wNbWbSUyv_XgRJlpqKLPykglIkzKtGYnxMKEFfAFcWY3K1cg==", "X-OAuth-Scopes": "identify,bot:basic", "X-Slack-Req-Id": "bc203c95-ac82-44ab-a5e3-f1c9cf2f357c", "Via": "1.1 430c98a561662ce110d7e2e105bbcbed.cloudfront.net (CloudFront)", "X-Content-Type-Options": "nosniff", "Content-Encoding": "gzip", "Vary": "Accept-Encoding", "x-slack-router": "p", "X-Slack-Backend": "h", "Cache-Control": "private, no-cache, no-store, must-revalidate", "Referrer-Policy": "no-referrer", "Content-Type": "application/json; charset=utf-8", "X-Accepted-OAuth-Scopes": "chat:write:bot,post"}, "message": {"username": "ghettobot", "text": "This is a message to SLACK", "ts": "1542035704.000100", "subtype": "bot_message", "type": "message", "bot_id": "B9SQGMA6N"}, "ok": true, "ts": "1542035704.000100", "channel": "C9M6RBG0M"}
```

## Listen to Kubernetes events in SLACK

Launch the Kafka event sync:

```
kubeless topic create k8s
kubectl run events --image=skippbox/k8s-events:0.10.12
```

Deploy the function to get triggered on k8s events and send message to SLACK

```
make events
```
