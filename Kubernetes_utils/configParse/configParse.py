from pathlib import Path
import yaml
from collections import defaultdict


class kubeConfigParse:
  def __init__(self) -> None:
    # Initialize variable
    self.kubeconfig_path = None
    self.kube_config_parsed = None
    self.status_message = None
    self.accounts = list()

  def load_kube_config_file(self) -> str:
    self.status_message = "Trying to load default kubeconfig ... !!!"
    USER_HOME = str(Path.home())
    DEFAULT_PATH = "{}/.kube/config".format(USER_HOME)

    kpath = Path(DEFAULT_PATH)
    if kpath.is_file():
      return DEFAULT_PATH
    else:
      self.status_message = "No K8S Config located at the default location !!!"
      ## Frame for feeding Kube Config
      return "error"

  def parse_kube_config_file(self) -> None:
    KUBECONFIG_PATH = self.load_kube_config_file()
    try:
      with open(KUBECONFIG_PATH, "r") as kconfig_in:
        kconfig_stream = kconfig_in.read()
        self.kube_config_parsed = yaml.load(kconfig_stream, yaml.BaseLoader)
    except yaml.YAMLError as exc:
      self.status_message = "Error while parsing YAML file"
      if hasattr(exc, 'problem_mark'):
        if exc.context != None:
          exc_message = 'parser says\n' + str(exc.problem_mark) + '\n  ' + str(exc.problem) + ' ' + str(exc.context) + '\nPlease correct data and retry.'
        else:
          exc_message = 'parser says\n' + str(exc.problem_mark) + '\n  ' + str(exc.problem) + '\nPlease correct data and retry.'
      else:
       exc_message =  "Something went wrong while parsing yaml file."
  
    clusterList = [cluster['name'] for cluster in self.kube_config_parsed['clusters']]
    self.accounts = list(set(i.split(':')[4] for i in clusterList if "aws:eks" in i))
    
    print(self.accounts)
    for account in self.accounts:
      for cluster in clusterList:
        if account in cluster:
          
    # for item in clusterList:
    #   if "aws:eks" in item:
    #     arr_item = item.split(':')[3:]
    #     print(arr_item)
    #     #cluster[arr_item[4]] = dict()
  

if __name__ == "__main__":
  testObj = kubeConfigParse()
  testObj.parse_kube_config_file()