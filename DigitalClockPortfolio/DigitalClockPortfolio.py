from tkinter import Tk
from tkinter import Label
import time
import sys

screen = Tk()
screen.title("My Digital time keeper")

def what_time_it_is():
    Var = time.strftime("%I:%M:%S %p")
    clock.config(text=Var)
    clock.after(200, what_time_it_is)

clock = Label(screen, font=("Helvetica", 90), bg="blue", fg="white")
clock.pack()

what_time_it_is()




screen.mainloop()