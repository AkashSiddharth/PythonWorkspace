import boto3
import logging
import yaml
from pathlib import Path

def get_home() -> str:
  return Path.home()

def get_all_aws_profiles() -> list:
  aws_profiles = list()
  logging.info(f"Fetching AWS profile configurations @ {get_home()}/.aws/config")
  with open( f"{get_home()}/.aws/config", 'r') as aws_config:
    content = aws_config.readlines()
  
  for line in content:
    logging.debug(f"Read line: {line}")
    if line.startswith('[profile'):
      aws_profiles.append(line.split(' ')[-1][:-2])
  
  logging.info(f"All AWS profiles located: {aws_profiles}")

  return aws_profiles

def get_cluster_data() -> dict:
  profiles = get_all_aws_profiles()

  # Create a dictionary of all clusters
  dict_cluster = dict()

  try:
    for profile in profiles:
      logging.info(f"Establishing session for {profile}")
      # Establish a custom session
      temp_session = boto3.session.Session(profile_name = profile)

      # Create an EKS session
      eks_client = temp_session.client('eks')
      
      clusters = eks_client.list_clusters()

      if clusters['ResponseMetadata']['HTTPStatusCode'] == 200:
        logging.info(f"EKS clusters in {profile} : {clusters['clusters']}")
        
        # Get the cluster data
        for cluster in clusters['clusters']:
          # Append the cluster as key
          dict_cluster[cluster] = dict()
          cluster_info = eks_client.describe_cluster(name = cluster)
          logging.debug(cluster_info)
          dict_cluster[cluster]['profile'] = profile
          dict_cluster[cluster]['cert'] = cluster_info['cluster']['certificateAuthority']['data']
          dict_cluster[cluster]['endpoint'] = cluster_info['cluster']['endpoint']
          dict_cluster[cluster]['arn'] = cluster_info['cluster']['arn']
          dict_cluster[cluster]['region'] = cluster_info['cluster']['arn'].split(':')[3]
          logging.info(f"Key added {cluster} with values {dict_cluster[cluster]}")

    return dict_cluster
  except Exception as e:
    print(e)

def create_kubeconfig():
  cluster_data = get_cluster_data()

  dict_kubeconfig = {
    'apiVersion': 'v1',
    'kind': 'Config',
    'preferences': {},
    'clusters': [],
    'contexts': [],
    'current-context': None,
    'users': []
  }

  for cluster, data in cluster_data.items():
    cluster_dict = dict()
    context_dict = dict()
    user_dict = dict()
    user_temp = dict()

    cluster_dict['cluster'] = dict()
    context_dict['context'] = dict()
    user_dict['user'] = dict()
    user_dict['user']['exec'] =  dict()

    user_dict['user']['exec']['env'] = list()

    context_dict['name'] = cluster
    cluster_dict['name'] = context_dict['context']['cluster'] = context_dict['context']['user'] = user_dict['name'] = data['arn']

    cluster_dict['cluster']['certificate-authority-data'] = data['cert']
    cluster_dict['cluster']['server'] = data['endpoint']

    user_dict['user']['exec']['apiVersion'] = 'client.authentication.k8s.io/v1beta1'
    user_dict['user']['exec']['args'] = ['--region', 
                                         data['region'], 
                                         'eks', 
                                         'get-token',
                                         '--cluster-name',
                                         cluster,
                                         '--output',
                                         'json']
    user_dict['user']['exec']['command'] = 'aws'

    user_temp['name'] = 'AWS_PROFILE'
    user_temp['value'] = data['profile']

    user_dict['user']['exec']['env'].append(user_temp)

    logging.info(f"Current Cluster: {cluster_dict}")
    logging.info(f"Current Context: {context_dict}")
    logging.info(f"Current User: {user_dict}")

    dict_kubeconfig['clusters'].append(cluster_dict)
    dict_kubeconfig['contexts'].append(context_dict)
    dict_kubeconfig['users'].append(user_dict)
  
  logging.info(f"Created configuration: {dict_kubeconfig}")

  with open(f"{get_home()}/.kube/config", 'w') as kconfig:
    yaml.dump(dict_kubeconfig, kconfig)

if __name__ == "__main__":
  logging.basicConfig(level=logging.WARN, format="%(levelname)s:%(message)s")
  create_kubeconfig()