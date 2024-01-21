from tkinter import *
win= Tk()
win.title("Calculator")
win.iconbitmap("calculator.ico")

display=Entry(win,bg="gray",font=("The Times New Roman",22,'bold'))
display.grid(row=0,column=0, columnspan=5, padx=10, pady=10)

def button_click(num):
   current=display.get()
   display.delete(0,END)
   display.insert(0,str(current)+str(num))

def button_clear():
   display.delete(0,END)

def button_add():
   f_num=display.get()
   global first_number
   global maths_operation
   maths_operation= "+"
   first_number=int(f_num)
   display.delete(0,END)

def button_sub():
   f_num=display.get()
   global first_number
   global maths_operation
   maths_operation= "-"
   first_number=int(f_num)
   display.delete(0,END)

def button_multiply():
   f_num=display.get()
   global first_number
   global maths_operation
   maths_operation= "*"
   first_number=int(f_num)
   display.delete(0,END)

def button_div():
   f_num=display.get()
   global first_number
   global maths_operation
   maths_operation= "/"
   first_number=int(f_num)
   display.delete(0,END)

def button_equal():
   second_number= display.get()
   display.delete(0,END)

   if maths_operation=="+":
       display.insert(0,first_number + int(second_number))
   elif maths_operation=="-":
      display.insert(0,first_number - int(second_number))
   elif maths_operation=="-":
      display.insert(0,first_number - int(second_number))
   elif maths_operation=="*":
      display.insert(0,first_number * int(second_number))
   elif  maths_operation=="/":
        try: 
            display.insert(0,first_number / int(second_number))
        except ZeroDivisionError:
            display.insert(0,"Error")

button_1 = Button(win, text="1",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(win, text="2",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(win, text="3",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(win, text="4",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(win, text="5",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(win, text="6",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(win, text="7",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(win, text="8",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(win, text="9",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(win, text="0",bg="dark gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(win, text="+",bg="gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=button_add)
button_sub = Button(win, text="-",bg="gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=button_sub)
button_multiply = Button(win, text="*",bg="gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=button_multiply)
button_div = Button(win, text="/",bg="gray",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=button_div)
button_equal = Button(win, text="=",bg="orange",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=button_equal)
button_clear = Button(win, text="C",bg="orange",font=("The Times New Roman",14,'bold'), padx=40, pady=20, command=button_clear)

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)
button_add.grid(row=3, column=4)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)
button_sub.grid(row=2, column=4)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)
button_multiply.grid(row=1, column=4)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_div.grid(row=4, column=4)
    


win.mainloop()