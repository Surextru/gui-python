from tkinter import *

#everythin is a widget

root = Tk()

#LABEL 
# #creating a label widget
# myLabel1 = Label(root, text="Hello world").grid(row=0, column=)
# myLabel2 = Label(root, text="My name is Jimmy")

# #shoving it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)

#BUTTON

# def myClick():
#     myLabel = Label(root, text="You clicked me you rude. I like it")
#     myLabel.pack()

# # myButton = Button(root, text="Hi babe :D", state=DISABLED)
# # myButton = Button(root, text="Hi babe :D", padx=50, pady=50)
# # myButton = Button(root, text="Dont click me", command=myClick)
# myButton = Button(root, text="Dont click me", command=myClick)
# myButton.pack()

#ENTRY

# e = Entry(root, width=50, bg="yellow", fg="green")
# e = Entry(root, width=50, borderwidth=5)
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def btn():
    name = e.get()
    myLabel = Label(root, text=name)
    myLabel.pack()

btn = Button(root, text="enter your name", command=btn).pack()

root.mainloop()
