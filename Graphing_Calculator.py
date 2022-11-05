# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:20:44 2022

@author: agraw
"""

from tkinter import *
import sympy
from sympy import symbols
from sympy.plotting import *

class Graphing_Calculator():
    def __init__(self):
        window = Tk()
        window.title("Graphing Calculator")
        frame = Frame(window)
        frame.pack()
        l = Label(frame, text = "Enter the function")
        self.msg = StringVar()
        ent = Entry(frame, textvariable= self.msg)
        b = Button(frame, text = "plot", command = self.plot)
        f = Frame(window)
        f.pack()
        self.la = Label(f)
        self.la.pack()
        l.grid(row = 1, column = 1)
        ent.grid(row = 1, column = 2)
        b.grid(row = 2, column = 1)
        window.mainloop()
        
    def plot(self):
        x = symbols("x")
        e = self.msg.get()
        p1 = plot(e, show = True)

