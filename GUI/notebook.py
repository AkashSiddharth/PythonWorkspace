from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tabbed Frames Example")
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both') # Pack the notebook into the root window
tab1_frame = ttk.Frame(notebook)
tab2_frame = ttk.Frame(notebook)
notebook.add(tab1_frame, text="Tab 1")
notebook.add(tab2_frame, text="Tab 2")
Label(tab1_frame, text="Content for Tab 1").pack(pady=20)
Button(tab2_frame, text="Click Me in Tab 2").pack(pady=20)
root.mainloop()
