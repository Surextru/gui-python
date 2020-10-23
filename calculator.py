from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

f_number = 0
math=""
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    result = e.get()
    global f_number
    global math
    math = "addition"
    f_number = int(result)
    e.delete(0, END)


def button_subs():
    result = e.get()
    global f_number
    global math
    math = "substraction"
    f_number = int(result)
    e.delete(0, END)

def button_mult():
    result = e.get()
    global f_number
    global math
    math = "multiplication"
    f_number = int(result)
    e.delete(0, END)

def button_div():
    result = e.get()
    e.delete(0, END)
    global f_number
    global math
    math = "division"
    f_number = int(result)

def button_clear():
    e.delete(0, END)

def button_eq():
    current = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, int(f_number) + int(current))
    if math == "substraction":
        e.insert(0, int(f_number) - int(current))
    if math == "multiplication":
        e.insert(0, int(f_number) * int(current))
    if math == "division":
        try:
            e.insert(0, int(f_number) // int(current))
        except ZeroDivisionError:
            e.insert(0, str("undefined"))



#definde buttons
btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

btn_add = Button(root, text="+", padx=39, pady=20, bg="#939393", command=button_add)
btn_subs = Button(root, text="-", padx=40, pady=20, bg="#939393", command=button_subs)
btn_mult = Button(root, text="x", padx=39.35, pady=20, bg="#939393", command=button_mult)
btn_div = Button(root, text="/", padx=40, pady=20, bg="#939393", command=button_div)

btn_eq = Button(root, text="=", padx=86, pady=20, command=button_eq)

btn_clear = Button(root, text="clear", padx=172, pady=15, bg="#939393", command=button_clear)


#put btns on the screen

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)

btn_0.grid(row=5, column=0)

btn_add.grid(row=5, column=3)
btn_subs.grid(row=4, column=3)
btn_mult.grid(row=3, column=3)
btn_div.grid(row=2, column=3)

btn_eq.grid(row=5, column=1, columnspan=2)
btn_clear.grid(row=1, column=0, columnspan=4)

root.mainloop()
