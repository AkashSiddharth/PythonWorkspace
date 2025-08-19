import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    filepath = filedialog.askopenfilename(
        title="Select a file",
        initialdir="/",  # Start browsing from the root directory
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filepath:
        print(f"Selected file: {filepath}")

def open_directory_dialog():
    dirpath = filedialog.askdirectory(
        title="Select a directory",
        initialdir="/"
    )
    if dirpath:
        print(f"Selected directory: {dirpath}")

root = tk.Tk()
root.title("File Browser Example")

open_file_button = tk.Button(root, text="Open File", command=open_file_dialog)
open_file_button.pack(pady=10)

open_dir_button = tk.Button(root, text="Open Directory", command=open_directory_dialog)
open_dir_button.pack(pady=10)

root.mainloop()
