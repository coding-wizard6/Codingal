from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("400x300")
root.title("main")

def topwin ():
    top=Toplevel(root)
    top.geometry("180x200")
    top.title("Password Generator")

    l2=Label(top,text="12345678$")

    l2.pack()
    top.mainloop

l=Label(root,text="Password Generator")
btn=Button(root,text="GENERATE PASSWORD",command=topwin)

l.pack()
btn.pack()

root.mainloop()

