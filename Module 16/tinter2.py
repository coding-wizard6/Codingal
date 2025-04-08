from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("400x300")
root.title("main")

def topwin ():
    top=Toplevel(root)
    top.geometry("180x200")
    top.title("toplevel")

    l2=Label(top,text="This is a toplevel window")

    l2.pack()
    top.mainloop

l=Label(root,text="This is a root window")
btn=Button(root,text="Click here to poen another window",command=topwin)

l.pack()
btn.pack()

root.mainloop()

