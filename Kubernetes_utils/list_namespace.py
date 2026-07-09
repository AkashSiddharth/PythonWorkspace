from kubernetes import client, config

# Specify the custom path to your kubeconfig file
kubeconfig_path = None

# Load configuration from the custom path
config.load_kube_config(config_file=kubeconfig_path)

# Initialize the Core V1 API client
v1 = client.CoreV1Api()

# Fetch and list all namespaces
print("Listing namespaces:")
namespaces = v1.list_namespace()
for ns in namespaces.items:
    print(f"- {ns.metadata.name}")