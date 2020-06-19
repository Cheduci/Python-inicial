from tkinter import *
from tkcalendar import *

root = Tk()

cal = Calendar(root, selectmode="day", year=2020, month=5)
cal.pack(pady=20)

def grab_date():
    myLabel.config(text=cal.get_date())

myButton = Button(root, text = "Get date", command = grab_date)
myButton.pack(pady = 20)

myLabel = Label(root, text = "")
myLabel.pack(pady = 20)

root.mainloop()