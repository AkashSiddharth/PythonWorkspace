from tkinter import *
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import yaml

class kubeConfigParse:
  def __init__(self) -> None:
    # Initialize variable
    self.kubeconfig_path = None
    self.kube_config_parsed = dict()
    self.status_message = str()

    # Initialize UI elements
    ## Root Window
    self.root = Tk()
    self.root.title("Kubernetes Configuration Management")

    #setting window size
    width=900
    height=1000
    screenwidth = self.root.winfo_screenwidth()
    screenheight = self.root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    self.root.geometry(alignstr)
    self.root.resizable(width=False, height=False)

    # Initialize UI Variables
    self.var_accounts, self.var_regions, self.var_clusters = list(), list(), list()

    # Load the Base UI
    self.draw_UI()
  
  def draw_UI(self):
    ## Top Frame
    self.frame_top = ttk.Frame()
    #self.frame_top.
    self.frame_top.pack(side='top', fill=X)

    # Accounts
    label_accounts =  ttk.Label(master=self.frame_top, text="Accounts: ")
    label_accounts.pack(side='left')
    self.cmbobx_accounts = ttk.Combobox( master = self.frame_top, state = 'disabled')
    self.cmbobx_accounts.pack(side='left', padx = 5, pady = 5)

    # Region
    label_region =  ttk.Label(master=self.frame_top, text="Region: ")
    label_region.pack(side='left')
    self.cmbobx_region = ttk.Combobox(master = self.frame_top, state = 'disabled')
    self.cmbobx_region.pack(side='left', padx = 5, pady = 5)

    # Clusters
    label_clusterList = ttk.Label(master=self.frame_top, text="Clusters: ")
    label_clusterList.pack(side='left')
    self.cmbobx_clusterList = ttk.Combobox(master = self.frame_top, state = 'disabled')
    self.cmbobx_clusterList.pack(side='left', padx = 5, pady = 5)

    ## Status Frame
    self.frame_status = ttk.Frame()
    self.frame_status.pack(side='bottom')
    self.label_status = ttk.Label(master=self.frame_status, textvariable=self.status_message)
    self.label_status.pack(side='left', fill=X)

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
      return filedialog.askopenfilename(filetypes = (("Config File" , "*.yaml"),("All Files","*.*")))

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
      
      messagebox.showerror("self.status_message", exc_message )

  def load_data_to_UI(self) -> None:
    self.parse_kube_config_file()

    clusterList = [cluster['name'] for cluster in self.kube_config_parsed['clusters']]

    ## Extract Data
    self.var_accounts = list(set(item.split(':')[4] for item in clusterList if "aws:eks" in item))
    cmbobx_accounts_val = StringVar()
    self.cmbobx_accounts['values'] = self.var_accounts
    self.cmbobx_accounts['state'] = 'readonly'
    self.cmbobx_accounts['textvariable'] = cmbobx_accounts_val

    


  def runner(self):
    self.load_data_to_UI()
    self.root.mainloop() # Start the event loop 


if __name__ == "__main__":
  kconf = kubeConfigParse()
  kconf.runner()