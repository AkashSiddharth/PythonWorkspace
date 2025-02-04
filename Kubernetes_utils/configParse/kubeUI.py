# brew install python-tk
from tkinter import *
from tkinter import ttk, filedialog

# class kubeConfigDraw:
#     def __init__(self) -> None:
        

root = Tk()
root.title("Kubernetes Config Management")

rootFrame = ttk.Frame(root)

## Frame for feeding Kube Config
kubeConfigFilename = filedialog.askopenfilename()

print(kubeConfigFilename)

## Frame to load clusters


root.mainloop()