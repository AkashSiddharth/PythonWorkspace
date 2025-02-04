from tkinter import *
from tkinter import ttk

class test:
  def __init__(self) -> None:
    self.draw_layout()
    
  def draw_layout(self) -> None:
    window = Tk()

    frame_a = ttk.Frame()
    frame_b = ttk.Frame()

    label_a = ttk.Label(master=frame_a, text="I'm in Frame A")
    label_a.pack()

    label_b = ttk.Label(master=frame_b, text="I'm in Frame B")
    label_b.pack()

    frame_a.pack()
    frame_b.pack()

    window.mainloop()

if __name__ == "__main__":
  testing = test()
