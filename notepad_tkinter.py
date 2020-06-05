from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os

def newfile():
    global file
    root.title("untitled - NOTEPAD")
    file=None
    Textarea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.text")])
    if file =="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents" , "*.text")])
        if file =="":
            file=None
        else:
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File saved")
    else:
        f=open(file,"w")
        f.write(Textarea.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    Textarea.event_generate("<<Cut>>")
def copy():
    Textarea.event_generate("<<Copy>>")
def paste():
    Textarea.event_generate("<<Paste>>")
def about():
    showinfo("Notepad","Notepad by kumar")


if __name__ =='__main__':
    root=Tk()
    root.title("untitled-Notepad")
    root.geometry("644x555")
    Textarea=Text(root,font="lucida 13")
    file=None
    Textarea.pack(expand=True,fill=BOTH)
    MenuBar=Menu(root)
    fileMenu=Menu(MenuBar,tearoff=0)
    fileMenu.add_command(label="New",command=newfile)
    fileMenu.add_command(label="Open",command=openfile)
    fileMenu.add_command(label="Save",command=savefile)
    MenuBar.add_cascade(label="File",menu=fileMenu)

    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    HelpMenu.add_command(label="Help",command=HelpMenu)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    EMenu=Menu(MenuBar,tearoff=0)
    EMenu.add_command(label="Quit",command=quitApp)
    MenuBar.add_cascade(label="Quit",menu=EMenu)

    root.config(menu=MenuBar)

    Scroll=Scrollbar(Textarea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)


    root.mainloop()