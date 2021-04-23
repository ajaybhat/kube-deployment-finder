import getopt
import sys

from tabulate import tabulate

from kube_client import KubeClient


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hf:", ["kubeconfig="])
    except getopt.GetoptError:
        print('Usage: find_kube_deployments.py -f <kube_config_file>')
        sys.exit(2)
    kube_client = KubeClient(opts[0][1])
    deployments = kube_client.apps_v1_api.list_deployment_for_all_namespaces()

    rows = []
    for deployment in deployments.items:
        # Find name, namespace, image, last update time
        row = [deployment.metadata.name,
               deployment.metadata.namespace,
               [container.image for container in deployment.spec.template.spec.containers],
               deployment.status.conditions[-1].last_update_time]
        rows.append(row)
    print(tabulate(rows, headers=['Deployment Name', 'Namespace', 'Image', 'Last Updated']))


if __name__ == "__main__":
    main(sys.argv[1:])
