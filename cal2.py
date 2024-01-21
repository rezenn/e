from tkinter import *

win = Tk()
win.title("Calculator")
win.iconbitmap("calci.ico")

e = Entry(win, width=50, borderwidth=2)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math_operator
    math_operator = "+"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math_operator
    math_operator = "-"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math_operator
    math_operator = "*"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math_operator
    math_operator = "/"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math_operator == "+":
        e.insert(0, f_num + int(second_number))
    elif math_operator == "-":
        e.insert(0, f_num - int(second_number))
    elif math_operator == "*":
        e.insert(0, f_num * int(second_number))
    elif math_operator == "/":
        try:
            e.insert(0, f_num / int(second_number))
        except ZeroDivisionError:
            e.insert(0, "Error")

button_1 = Button(win, text="1",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(win, text="2",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(win, text="3",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(win, text="4",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(win, text="5",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(win, text="6",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(win, text="7",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(win, text="8",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(win, text="9",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(win, text="0",bg="dark gray",font=("The Times New Roman",12), padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(win, text="+",bg="gray",font=("The Times New Roman",12), padx=40, pady=20, command=button_add)
button_subtraction = Button(win, text="-",bg="gray",font=("The Times New Roman",12), padx=40, pady=20, command=button_subtract)
button_multiply = Button(win, text="*",bg="gray",font=("The Times New Roman",12), padx=40, pady=20, command=button_multiply)
button_divide = Button(win, text="/",bg="gray",font=("The Times New Roman",12), padx=40, pady=20, command=button_divide)
button_equal = Button(win, text="=",bg="orange",font=("The Times New Roman",12), padx=40, pady=20, command=button_equal)
button_clear = Button(win, text="C",bg="orange",font=("The Times New Roman",12), padx=40, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_addition.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtraction.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

win.mainloop()


