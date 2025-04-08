from tkinter import *

window = Tk()

for i in range(3):
    for j in range(3):
        frame=frame(master=window,relief=tk.raised,borderwidth=2)
        frame.grid(row=i,column=j,padx=5,pady=5)
        