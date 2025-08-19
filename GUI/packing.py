import tkinter as tk

root = tk.Tk()
root.title("Widgets in the Same Row")

# Create and pack the first label
label1 = tk.Label(root, text="Label 1", bg="lightblue")
label1.pack(side=tk.LEFT, padx=5, pady=5) # padx and pady add spacing

# Create and pack the second label
label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label2.pack(side=tk.LEFT, padx=5, pady=5)

# Create and pack a button
button1 = tk.Button(root, text="Click Me!")
button1.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()