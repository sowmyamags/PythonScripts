#!/usr/bin/env python3

#import tkinter as tk
#from tkinter import *

#window = Tk()

#window.title("Welcome to LikeGeeks app")

#window.mainloop()
import tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


#create main window
master = tkinter.Tk()
master.title("tester")
master.geometry("300x100")


#make a label for the window
label1 = tkinter.Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# Run forever!
master.mainloop()
