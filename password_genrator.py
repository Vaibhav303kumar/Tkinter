import random
from tkinter import*
import tkinter.messagebox
import ttkSimpleDialog


def passwordG():
    s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
   # passwordLength=int(input("enter the length of password you want-"))
    past= userentry.get()
    password = "".join(random.sample(s,int(past)))
    Label(root,text =password).grid()
    #print(password)

root=Tk()
root.geometry("400x350")
root.title("PassWord Generator")
pas=Label(root , text="Length of PassWord you Want-")
pas.grid()
uservalue=StringVar
userentry=Entry(root,textvariable=uservalue)
userentry.grid(row=0,column=1)

button = Button(text="sumit" , command=passwordG).grid()

root.mainloop()
