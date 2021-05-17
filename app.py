# import tkinter

from tkinter import *

m = Tk()

m.title("Sample code")

m.geometry("500x300")


redbutton = Button(m, text = "red", fg = 'red')
redbutton.pack( side = LEFT)
greenbutton = Button(m, text = "blue", fg = 'Black')
greenbutton.pack( side = RIGHT)
bluebutton = Button(m, text = "black", fg = 'blue')
bluebutton.pack( side = TOP)
blackbutton = Button(m, text = "green", fg = 'red')
blackbutton.pack( side = BOTTOM)




m.mainloop()