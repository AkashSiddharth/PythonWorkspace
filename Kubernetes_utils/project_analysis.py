from pathlib import Path
import yaml
import os

class Node:
    def __init__(self, name: str, path: str, is_dir: bool):
        self._name = name
        self._path = path
        self._is_dir = is_dir
        self._parent = None
        self._child = list()

    @property
    def name(self):
        return self._name
    
    @property
    def path(self):
        return self._path
    
    @property
    def type(self):
        if self._is_dir:
            return "Folder"
        else:
            _, _extn = os.path.splitext(self.path)
            return _extn.lower().lstrip('.')

    @property
    def children(self):
        return self.children

class Project:
    def __init__(self, projectpath: str):
        try:
            if os.path.exists(projectpath) and os.path.isdir(projectpath):
                self.projectpath = projectpath
            else:
                raise FileNotFoundError
        except FileNotFoundError as exc:
            print(f"Path does not exist or not a folder. {exc}")
        except Exception as exc:
            print(f"{exc}")
        
        self._project = None

    @property
    def project(self):
        return self._project
    
    @project.setter
    def project(self):
        pass
    
    def walk(self):
        for dirpath, dirnames, filenames in os.walk(self.projectpath):
            # Get the current name
            basename = os.path.basename(dirpath)
            print(f"Name: {basename}")
            print(f"Current Directory: {dirpath}")
            print(f"Subdirectories: {dirnames}")
            print(f"Files: {filenames}\n") 
    
if __name__ == "__main__":
    project = Project("/Users/akashsiddharth/WorkSpaces/CorpSysEngg/fas-k8s/xFunctional/NDACentral")
    project.walk()

