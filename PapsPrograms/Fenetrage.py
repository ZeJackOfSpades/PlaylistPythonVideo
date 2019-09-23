#!/usr/bin/env python3
#coding:utf-8
"""
Created on Tue Nov 27 14:41:57 2018

@author: philou666
"""

from math import sqrt
from cmath import *
#from tkinter import *
from tkinter import Button , Label, Tk, Entry, DoubleVar, StringVar, Checkbutton

def valueCheck () : 
    answer = False
    while answer == False :
        try:
            var_entry = DoubleVar()   
        except:
            print("Erronous value !")
            answer = False
        else:
            answer = True
   #         return var_entry

   
def delta_Compute (a,b,c) :
    delta = b**2 - 4*a*c 
    if delta > 0    : genre = "real"
    elif delta == 0 : genre = "double"   
    else            : genre = "complex"
    return (delta,genre)

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
            print (msg_Solutions)       
        elif gender == "double" :
            x0 = -b / (2*a)
            msg2 = "\n{} root is x0={}"
            msg_Solutions.set (msg2.format(gender,x0))
            print(msg_Solutions)
        else  : 
            reZ = -b/(2*a)
            imZ = sqrt(-delta/(2*a)) 
            z1 = complex(reZ,imZ)
            z2 = complex(reZ,-imZ)
            msg2 = "\n{} roots are z1={} and z2={} "
            msg_Solutions.set (msg2.format(gender,z1,z2))
            print(msg_Solutions)

def update (*args) :
    A=var_A_entry.get()
    B=var_B_entry.get()
    C=var_C_entry.get()
    
    print ("updating...")
    
    (delta,gender) = delta_Compute (A,B,C)
   # print (A, B, C, delta, gender) #for debug only
    
    roots_compute (A,B,C,delta,gender)

#Wigdet creation and management
mainWindow = Tk()
mainWindow.title("Complex Polynom Resolution")
mainWindow.geometry("600x240")

#MainWindow.resize(True,False)

msg_Welcome      ="This widget solve complex polynom Ax² + Bx + C\nA B and C could be complex"
#msg_Solutions    = "Solutions are Z1 =  and  Z2="
msg_Solutions    = StringVar()
label_Title      = Label(mainWindow, text=msg_Welcome)
label_Conclusion = Label(mainWindow, textvariable=msg_Solutions)

var_A_entry = DoubleVar()
var_B_entry = DoubleVar()
var_C_entry = DoubleVar()

#input_CoeffA     = Entry(mainWindow, textvariable=var_A_entry , command=valueCheck)
input_CoeffA     = Entry(mainWindow, textvariable=var_A_entry)

input_CoeffB     = Entry(mainWindow, textvariable=var_B_entry)
input_CoeffC     = Entry(mainWindow, textvariable=var_C_entry)

check_SaveInAFile= Checkbutton(mainWindow, text= "save in a file")
button_Update    = Button(mainWindow, text="update", command=update)
button_Quit      = Button(mainWindow, text="Exit", command=mainWindow.destroy)

label_Title.pack()
check_SaveInAFile.pack()
input_CoeffA.pack()
input_CoeffB.pack()
input_CoeffC.pack()
button_Update.pack()

label_Conclusion.pack()

button_Quit.pack()

mainWindow.mainloop()
