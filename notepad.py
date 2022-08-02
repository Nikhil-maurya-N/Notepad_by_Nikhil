
# importing required modules
import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as tmsg

# delclaring root variable as Tk() and formating it
root=Tk()
root.geometry("1366x768")

name="Untitled"
root.title(f"{name} - Notepad By Nikhil")

# decalring soem variables for  view ->customized menu'function
h=StringVar()
w=StringVar()

# this funtion for 'Apply' button in customized function
def update():
    root.geometry(f"{h.get()}x{w.get()}")
    
# thisfunction for view ->  customized function
def customized():
    new=Frame(root,height=140,width=200,bg="light blue")
    new.place(x=50,y=50)
    
    Label(new,text="Height",bg="light blue").place(x=10,y=30)
    Label(new,text="Width",bg="light blue").place(x=10,y=60)
    Entry(new,textvariable=h).place(x=70,y=30)
    Entry(new,textvariable=w).place(x=70,y=60)
    Button(new,text="Apply",command=update).place(x=80,y=100)
    Button(new,text="X",command=new.destroy,width=2,).place(x=170,y=5)

# this function is for view -> vertical menu 
def Vertical():
    root.geometry("683x768")

# this function is for view -> horizontal menu 
def Horizontal():
    root.geometry("1366x384")
 
# this function is for file -> new file menu   
def newFile():
    print("created new file")
    output=tmsg.askyesnocancel("Notepad By Nikhil","Do want to save this file?")
    if(output==YES):
        saveFile()
        tx.delete(1.0,END)
    else:
        root.title(f"{name} - Notepad by Nikhil")
        tx.delete(1.0,END)

# this function is for file -> savefile menu   
def saveFile():
    global file
    file=asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py"),("C files","*.c"),("C++ files","*.cpp")],initialfile="Untitled.txt")
    if file=="":
        file=None
    else:
        f=open(file,"w")
        f.write(tx.get(1.0,END))
        f.close()
    root.title(f"{os.path.basename(file)} - Notepad by Nikhil")

# this function is for file -> open file menu   
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt"),("Python files","*.py")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad by Nikhil")
        tx.delete(1.0,END)
        f=open(file,"r")
        tx.insert(1.0,f.read())
        f.close()

# this function is for file -> saveas file menu   
def saveasFile():
    saveFile()

# this function is for edit -> cut menu   
def cut():
    tx.event_generate(("<<Cut>>"))

# this function is for edit -> copy menu   
def copy():
    tx.event_generate(("<<Copy>>"))

# this function is for edit -> paste menu   
def paste():
    tx.event_generate(("<<Paste>>"))
    
# this function is for file-> find menu   
def find():
    global findVar
    global fr
    fr=Frame(height=60,width=220,bg="light Gray")
    fr.place(x=800,y=100)
    findVar=StringVar()
    Button(fr,text="FIND",bg="light gray",relief=GROOVE,command=getin).place(x=10,y=3)
    Entry(fr,textvariable=findVar,bg="light Gray").place(x=60,y=5)
    Button(fr,text="X",command=fr.destroy).place(x=200,y=3)

# this fumctom is for button  in 102 th line for searching ccorsponding string to entire text
def getin():
    strr=tx.get(1.0,END)
    cha=strr.find(findVar.get())
    dis=Label(fr,text=f"{findVar.get()} is found at {cha}th character",bg="pink")
    dis.place(x=10,y=35)
    dis.after_cancel(400)
    
    


# this function is for help -> about us menu
def help():
   a= tmsg.showinfo("About Notepad","Hi There I am Nikhil Maurya I am currently purssuing BCA from Dr. Virendra Swarup institute of computer studies this project is made at the time of June start Date = 6/5/2022.The finishing date is 9/6/2022. This is a simulation progrram of Microsoft't Windows Buit in Basic text editor called \"Notepad\".I got a little help and inspiration from online mentor Named as \'Code With Harry.\'\n\n\n\tThank you for using it. \n\nfor detailed information open this pdf")

# this funtion is for file -> exit menu
def exit1():
    exit()


# here is  the declartion of text widget for entile text area
tx=Text(root ,undo=True,font=("Helvetica",20))
tx.pack(expand=True,fill=BOTH)

# declartion of mainmenu of the program
mainmenu=Menu(root)

# declartion of first menu named as m1(file)
m1=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="File",font=("BOLD",15),menu=m1)
m1.add_command(label="New File",font=("BOLD",15),command=newFile)
m1.add_command(label="Open",font=("BOLD",15),command=openFile)
m1.add_command(label="Save",font=("BOLD",15),command=saveFile)
m1.add_command(label="Save as",font=("BOLD",15),command=saveasFile)
m1.add_command(label="find",font=("BOLD",15),command=find)
m1.add_command(label="Exit",font=("BOLD",15),command=exit1)

# declartion of first menu named as m2(edit)

m2=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="Edit",font=("BOLD",15),menu=m2)
m2.add_command(label="Undo",font=("BOLD",15),command=tx.edit_undo)
m2.add_command(label="Redu",font=("BOLD",15),command=tx.edit_redo)
m2.add_separator()
m2.add_command(label="Cut",font=("BOLD",15),command=cut)
m2.add_command(label="Copy",font=("BOLD",15),command=copy)
m2.add_command(label="Paste",font=("BOLD",15),command=paste)

# declartion of third menu named as m3 (view)
m3=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="View",font=("BOLD",15),menu=m3)
m3.add_command(label= "Vertical",font=("BOLD",15),command=Vertical)
m3.add_command(label= "Horizontal",font=("BOLD",15),command=Horizontal)
m3.add_command(label= "customized",font=("BOLD",15),command=customized)

# declartion of first menu named as m4(help)
m4=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="Help",font=("BOLD",15),menu=m4)
m4.add_command(label= "About Notepad",font=("BOLD",15),command=help)

# configering the mainmenu
root.config(menu=mainmenu)

# scrollbar for text area if there is a lot of text in there
scy=Scrollbar(tx,relief=RAISED,width=25,)
scy.pack(side=RIGHT,fill=Y)
scy.config(command=tx.yview)
tx.config(yscrollcommand=scy.set)

# mainloop for infinite screeen entries
root.mainloop()