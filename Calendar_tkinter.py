from Tkinter import *
##from calendar import *
from tkcalendar import *
import tkMessageBox
root = Tk()
def cal_func():
    # makes a button that can be clicked to show current date
    def calval():
        tkMessageBox.showinfo("your date is", cal.get_date())
    top = Toplevel(root)
    # creates calendar with starting point
    cal = Calendar(top, font = "Arial 14", selectmode= "day", year= 2020, month= 5, day = 17)
    cal.pack(fill = "both", expand = True)
    btn3 = Button(top, text= "Click Me", command= calval)
    btn3.pack()
def date_func():
    top = Toplevel(root)
    Label(top, text= "Select Date").pack(padx = 10, pady = 10)
    ent = DateEntry(top, width = 15, backgroundcolor = "blue", foregroundcolor = "red", borderwidth = 3)
    ent.pack(padx = 10, pady = 10)
    
btn1 = Button(root, text = "Calendar", command = cal_func)
btn2 = Button(root, text = "DateEntry", command = date_func)
btn1.pack()
btn2.pack()
mainloop()
