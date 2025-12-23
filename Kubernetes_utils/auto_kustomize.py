from kubernetes import client, config
from pathlib import Path
import yaml
import os

class AutoKustomize:
    """
    Input:
        An Application folder
    scan the subdirectories to determine the env
    create a base folder with kustomize
    create env folders with kustomize
    """
    def __init__(self):
        pass

class ParseK8SYAML:
    """
        This class will take in a yaml and tokenize it
        Arrange the keys in Alphabetical order
        Determine server manifest fields and drop them
        multiline commnads are joined back to single line
        Outs a validated dictionary or a yaml dpepending on argument
    """
    def __init__(self):
        pass

    def 


class KustomizeApp:
    def __init__(self, application: str):
        self.app_details = dict()
        try:
            if os.path.exists(application) and os.path.isdir(application):
                self.app_folder = application
            else:
                raise FileNotFoundError
        except FileNotFoundError as exc:
            print(f"Path does not exist or not a folder. {exc}")
        except Exception as exc:
            print(f"{exc}")
    
    def app_walk(self) -> dict:
        

def do_nothing():
    pass

def create_local_workspace(fpath: str) -> str:
    workspace = f"local_{os.path.normpath(fpath)}_workspace"
    
    os.mkdir(os.path.join(fpath, f"{workspace}"))
    return workspace

def get_all_files(fpath: str) -> list: return list(map(lambda x: os.path.join(fpath, x) ,os.listdir(fpath)))

def get_manifests(fpath: str) -> list:
    k8s_manifests = list()
    for file in get_all_files(fpath):
        if file.endswith('yaml') or file.endswith('.yml'):
            print(f"{file}")

            # Check if Kubernetes Manifest
            k8s_manifests.append(file) if validate_k8s_manifest(file) else do_nothing
    
    return k8s_manifests

def validate_k8s_manifest(file: str) -> bool:
    required_fields = ['apiVersion', 'kind', 'metadata', 'spec']

    with open(file, 'r') as in_f:
        # Check if it has single yaml or multiple
        documents = list(yaml.safe_load_all(file))
        if len(documents) > 1 :

        manifest = yaml.safe_load(in_f)
        print(f"{manifest}")
        # It has to be dictionary
        if not isinstance(manifest, dict):
            print(f"{file} is not a dictionary.")
            return False
        
        # Checking for required fields in the file
        for field in required_fields:
            if field not in manifest:
                print(f"No {field} field in the YAML file: {file}.")
                return False
    
    return True

def kustomize_files(fpath: str):
    workspace = create_local_workspace(fpath)

if __name__ == "__main__":
    test_path = Path("/Users/akashsiddharth/WorkSpaces/CorpSysEngg/fas-k8s/xFunctional/AICM/cs-fast/IT/workdayoutbound-svc")
    # files = get_all_files(test_path)
    files = get_manifests(test_path)
    print(f"{files}")