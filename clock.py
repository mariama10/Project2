from tkinter import *
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title("My Clock")

def time():
    hours = strftime("%I")
    mins = strftime("%M")
    secs = strftime("%S")
    am_pm = strftime("%p")
    string=hours+ ":"+mins+":"+secs+" "+am_pm
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font = "ds-digital 150", background = "black", foreground = "white")
label.pack(anchor = "center")

time()
mainloop()