from tkinter import *
from tkinter import messagebox

win=Tk()
win.withdraw()
result=messagebox.askyesno("Confirmation", "Are you sure")
if result:
    print("Yes")
else:
    print("No")
 
win.mainloop()