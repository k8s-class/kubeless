import json
import base64
import tempfile

#pip install slackclient
from slackclient import SlackClient

#pip install kubernetes
from kubernetes import client, config

config.load_incluster_config()

v1=client.CoreV1Api()

#Get minio and slack secrets
for secrets in v1.list_secret_for_all_namespaces().items:
    if secrets.metadata.name == 'slack':
        token = base64.b64decode(secrets.data['token'])

sc = SlackClient(token)

def handler(event, context):
    msg = "k8s event: %s" % event['data']

    r = sc.api_call(
                "chat.postMessage",
                channel="#bot",
                text=msg
               )
    if r.get('ok'):
        return "Notification successfully sent to Slack"
    else:
        return "Error while sending notification to Slack: " + r.get('error')
