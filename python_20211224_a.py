from tkinter import *
import serial

def changed(value = None):
    global temp
    lbl.configure(text = value)
    ser.write(bytes(value, "utf-8"))
    ser.write(b"a")
    #temp = 1 - temp
    #if (temp == 0):
    #    ser.write(b"45")
    #    ser.write(b"a")
    #else:
    #    ser.write(b"135")
    #    ser.write(b"a")

ser = serial.Serial('COM4', 9600)
temp = 0;

window = Tk()
window.geometry('350x100')
window.title("Điều khiển động cơ servo")

lbl = Label(window)
lbl.pack(fill = X)

scl = Scale(window, from_ = 0, to = 180, orient = HORIZONTAL, command = changed)
scl.set(0)
scl.pack(fill = X)

mainloop()
