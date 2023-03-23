from kubernetes import client, config
from tabulate import tabulate

def get_kuberentes_data(ns : str) -> list:
  mined_data = list()

  # Load Kube config
  config.load_kube_config()

  # Create object
  appsV1 = client.AppsV1Api()

  deployments = appsV1.list_namespaced_deployment(ns).items

  # print(type(deployments))
  for deployment in deployments:
    deploy_data = dict()
    deploy_data['Deployment'] = deployment.metadata.name
    # print("Deployment Name: {}".format(deployment.metadata.name))
    deploy_data['Containers'] = list()

    containers = deployment.spec.template.spec.containers
    for container in containers:
      _temp_container = dict()
      _temp_container['Name'] = container.name
      # print("\tContainer Name: {}".format(container.name))
      _temp_container['Limits'] = container.resources.limits
      # print("\t\tLimits: {}".format(container.resources.limits))
      _temp_container['Requests'] = container.resources.requests
      # print("\t\tRequests: {}".format(container.resources.requests))
      if container.env != None:
        for e_var in container.env:
            if e_var.name == "WORKERS":
              _temp_container['Workers'] = e_var.value
              #print("\t\tWorkers: {}".format(e_var.value))
        # print("\t\tMemory Limits: {}".format(container.resources.limits.memory))
        # print("\t\tMemory Requests: {}".format(container.resources.requests.memory))
      deploy_data['Containers'].append(_temp_container)
    
    mined_data.append(deploy_data)
  
  return mined_data

def draw_table(in_data):
  out_f=tabulate(in_data,headers='keys',tablefmt='fancy_grid')

  with open('temp.txt', 'w') as out_file:
    out_file.write(out_f)


if __name__ == "__main__":
  deploy_data = get_kuberentes_data('aml-shuri-aws-uat')
  #print(deploy_data)
  draw_table(deploy_data)
