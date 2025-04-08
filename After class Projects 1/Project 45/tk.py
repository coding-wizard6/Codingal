from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("400x300")
root.title("main")

def topwin ():
    top=Toplevel(root)
    top.geometry("180x200")
    top.title("ROCK PAPER SCISSORS")
    
    l2=Label(top,text="PAPER")

    l2.pack()
    top.mainloop

l=Label(root,text="Rock Paper Scissor Game")
btn=Button(root,text="ROCK",command=topwin)
btn1=Button(root,text="PAPER",command=topwin)
btn2=Button(root,text="SCISSOR",command=topwin)

l.pack()
btn.pack()

root.mainloop()
