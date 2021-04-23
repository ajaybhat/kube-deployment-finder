from kubernetes import client
from kubernetes.config import new_client_from_config

class KubeClient:
    def __init__(self, kube_config_file):
        self.api_client = new_client_from_config(config_file=kube_config_file)
        self.apps_v1_api = client.AppsV1Api(api_client=self.api_client)
