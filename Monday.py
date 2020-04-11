from Tkinter import *
"""Presets"""
WIDTH = 400
HEIGHT = 600
""""""
"""Initial Setup"""
root = Tk()
root.title("Work App")
BACKGROUND = Label()
BACKGROUND.configure(color = "green", bd = 0)
BACKGROUND.grid(row=1, column=0)
root.configure(width = WIDTH, height = HEIGHT, bg = "#7083AE")
HEAD_BACKGROUND = Label(bg = "#7083AE")
HEAD_BACKGROUND.grid(row=1, column = 0, columnspan = 2)
HEAD_TITLE = Label(text="Work App", bg = "#7083AE", fg = "#f8f8ff", font=("Arial", 22))
HEAD_TITLE.grid(row = 0, column = 1)
ICON_SETTINGS = PhotoImage(file="images/ICON_SETTINGS.gif")
HEAD_SETTINGS = Button(image=ICON_SETTINGS, bg = "#7083AE", bd = 0)
HEAD_SETTINGS.grid(row=0, column=4)
"""Buttons"""
SIDE_BUTTON_1 = Button(text = "A",\
 bg = "#2C3445", fg = "#f8f8ff", width = 10, height = 4)
SIDE_BUTTON_1.grid(row = 0, column = 0)

SIDE_BUTTON_2 = Button(text = "B",\
 bg = "#2C3445", fg = "#f8f8ff", width = 10, height = 4)
SIDE_BUTTON_2.grid(row = 1, column = 0)

SIDE_BUTTON_3 = Button(text = "C",\
 bg = "#2C3445", fg = "#f8f8ff", width = 10, height = 4)
SIDE_BUTTON_3.grid(row = 2, column = 0)

SIDE_BUTTON_4 = Button(text = "D",\
 bg = "#2C3445", fg = "#f8f8ff", width = 10, height = 4)
SIDE_BUTTON_4.grid(row = 3, column = 0)

SIDE_BUTTON_5 = Button(text = "E",\
 bg = "#2C3445", fg = "#f8f8ff", width = 10, height = 4)
SIDE_BUTTON_5.grid(row = 4, column = 0)
""""""
#7083AE
root.mainloop()
