from tkinter import *

window = Tk()
window.title("Welcome to tkinter")
window.geometry("300x300")

greeting = Label(text="Hi , WELCOME TO TKINTER",fg="red",bg="yellow")
button = Button(text="Click here",bg="black",fg="white")
entry = Entry(fg="blue",bg="pink",width = 50)
frame=Frame(master=window,relief=RAISED,borderwidth=4)
text = Text(bg="lightgreen",fg="black")

greeting.pack()
button.pack()
entry.pack()
frame.pack()
text.pack()

window.mainloop()