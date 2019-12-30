#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on December 2019
# This program displays the time and date


from tkinter import * 
from tkinter.ttk import *
from time import strftime
import datetime
  
# creating tkinter window 
root = Tk() 
root.title('Clock') 
  

def main():
    # This function displays time and date

    string = strftime('%H:%M:%S \n%d-%m-%Y')
    lbl.config(text = string)
    lbl.after(1000, main) 
  
# Styling the label widget

lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'white') 
  
# Placing clock at the centre 

lbl.pack(anchor = 'center') 

 
if __name__ == "__main__":
    main()

mainloop()

