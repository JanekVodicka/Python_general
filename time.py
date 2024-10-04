from tkinter import *
import time

def Tick():
    Time_str = time.strftime("%H:%M:%S")
    clock.config(text=Time_str)

counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter)) # str = string
        label.after(1000,count)         # 1000 - čim vyšší, tím pomalejší
    count()

Window = Tk()
Window.title("Hodiny a počítač")
Window.geometry('300x300')

clock = Label(Window, font=("Times", 16, "bold"))
clock.pack()
label = Label(Window, fg = "dark green")
label.pack()
counter_label(label)
button1 = Button(Window, text = "Close", command = Window.destroy)
button1.pack()

Tick()
Window.mainloop()
