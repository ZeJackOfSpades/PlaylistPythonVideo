#!/usr/bin/env python3
#coding:utf-8
"""
Created on Tue Nov 27 14:41:57 2018

@author: philou666
"""

from math import sqrt
from cmath import *
#from tkinter import *
from tkinter import Button , Label, Tk, Entry, DoubleVar, StringVar, Checkbutton , messagebox

# My nice Color : to be put in a module
# red = (255 , 0 , 0)


# information 
def info () :
    messagebox.showinfo ("Read me", "This program has been developped by PowerWolves team \n"
                         "(PapsWolf & JackWolf)\n"
                         "It solves complex polynom,\n"
                         "Plot the curve\nand can save report")

#  checker
def valueCheck (GetnChecked) : 
    val_Checked = "?"
    try :
        val_Checked = GetnChecked.get()            
    except:
        answer = False
        val_Checked = "?"
        return (val_Checked , answer)
    else :
        answer = True
        return (val_Checked , answer)

# compute Delta and gender of roots
def delta_Compute (a,b,c) :
    delta = b**2 - 4*a*c 
    if delta > 0    : genre = "real"
    elif delta == 0 : genre = "double"   
    else            : genre = "complex"
    return (delta,genre)

# compute roots
def roots_compute (a,b,c,delta,gender) :
    if a == 0 :
        if b != 0: 
            msg2 = "Polynome order1 is P(x) = Bx + C\n with only one root x={}"
            msg_Solutions.set (msg2.format(-c/b))
        else :
            msg1 = "\nNo roots : P(x) = C"
            msg_Solutions.set (msg1)
    else :
        if gender == "real" :
            x1 = (-b + sqrt(delta)) / (2*a)
            x2 = (-b - sqrt(delta)) / (2*a)
            msg2 = "\n{} roots are x1={} and x2={}"
            msg_Solutions.set (msg2.format(gender,x1,x2))
                   
        elif gender == "double" :
            x0 = -b / (2*a)
            msg2 = "\n{} root is x0={}"
            msg_Solutions.set (msg2.format(gender,x0))
            
        else  : 
            reZ = -b/(2*a)
            imZ = sqrt(-delta/(2*a)) 
            z1 = complex(reZ,imZ)
            z2 = complex(reZ,-imZ)
            msg2 = "\n{} roots are z1={} and z2={} "
            msg_Solutions.set (msg2.format(gender,z1,z2))

# update command
def update (*args) :  
    (A , A_answer) = valueCheck(var_A_entry)   
    (B , B_answer) = valueCheck(var_B_entry)
    (C , C_answer) = valueCheck(var_C_entry)
     
    #print ("updating...") debug only

    if A_answer and B_answer and C_answer : # executed when Coeff are Ok
        (delta,gender) = delta_Compute (A,B,C)
        print (A, B, C, delta, gender) #for debug only
        roots_compute (A,B,C,delta,gender)
    else :
        messagebox.showerror ("Error", "One or more coefficient are erroneous")

    # handle color of input in case of error
    if A_answer == False :
        input_CoeffA.config(fg = "red") # error
    else :
        input_CoeffA.config(fg = "black") # ok
    if B_answer == False :
        input_CoeffB.config(fg = "red")
    else :
        input_CoeffB.config(fg = "black")
    if C_answer == False :
        input_CoeffC.config(fg = "red")
    else :
        input_CoeffC.config(fg = "black")

# saving data in a file
#def fileSave ():


# MAIN PROGRAM

#Wigdet creation and management
mainWindow = Tk()
mainWindow.title("Complex Polynom Resolution") # title
mainWindow.geometry("600x240") #size
#MainWindow.resize(True,False)

# Label 

msg_Welcome      ="\nThis widget solve complex polynom Ax² + Bx + C\nA B and C could be complex\n"
msg_Solutions    = StringVar()

label_Title      = Label(mainWindow, text=msg_Welcome)
label_Conclusion = Label(mainWindow, textvariable=msg_Solutions)

# Coefficient entry definition
var_A_entry      = DoubleVar()
var_B_entry      = DoubleVar()
var_C_entry      = DoubleVar()
input_CoeffA     = Entry(mainWindow, textvariable=var_A_entry)
input_CoeffB     = Entry(mainWindow, textvariable=var_B_entry)
input_CoeffC     = Entry(mainWindow, textvariable=var_C_entry)


# Buttons, checkbox with command
button_Info      = Button(mainWindow,text= "info", command=info)
check_SaveInAFile= Checkbutton(mainWindow, text= "save in a file")
button_Update    = Button(mainWindow, text="update", command=update)
button_Quit      = Button(mainWindow, text="Exit", command=mainWindow.destroy) # tkinder window closure Button


# labels, check box, input et Button instantiation
button_Info.pack()
label_Title.pack()
check_SaveInAFile.pack()
input_CoeffA.pack()
input_CoeffB.pack()
input_CoeffC.pack()
button_Update.pack()
label_Conclusion.pack()
button_Quit.pack()

# Display infinite loop by tkinter
mainWindow.mainloop()
