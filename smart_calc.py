from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break

        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod,}

win = Tk()
win.geometry('500x400')
win.title('Smart Pugger')
win.configure(bg='blue')

l1 = Label(win , text='I AM A SMART CALCULATOR',width=30,height=2 ,padx=3,pady=3,bg="blue",fg="black",font="italics 18")
l1.place(x=100,y=10)
l1.pack(fill=X)
l2 = Label(win , text='My NAME IS VAIBHAV' ,width=20,height=2 ,padx=3,bg="blue",fg="black",font="italics 19")
l2.place(x=130,y=40)
l2.pack(fill=X)
l3 = Label(win , text='What CAN I DO FOR YOU?' ,width=20,height=1, padx=3,bg="blue",fg="black",font="arial 22")
l3.place(x=150,y=130)
l3.pack(fill=X)

textin = StringVar()
e1 = Entry(win , width=30 ,textvariable = textin)
e1.place(x=140,y=170)

b1 = Button(win , text='CALCULATE',fg="black",bg="grey",height=1,font="arial " ,command=calculate)
b1.place(x=190,y=200)

list = Listbox(win,width=40,height=3)
list.place(x=130,y=250)

win.mainloop()