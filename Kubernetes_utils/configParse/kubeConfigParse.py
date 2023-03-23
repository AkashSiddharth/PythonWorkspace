import yaml

## TO-DO: To be provided or loaded automatically
KUBECONFIG_PATH = "/Users/akashsiddharth/.kube/config"

with open(KUBECONFIG_PATH, "r") as kconfig_in:
    kconfig_stream = kconfig_in.read()

    print(yaml.load(kconfig_in))