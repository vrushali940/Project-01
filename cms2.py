#Tablemast
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk
win=Toplevel()


path=Image.open(r"D:\Photo Editor\bg6.jpg")

render=ImageTk.PhotoImage(path)
img=Label(win,image=render)
img.place(x=1,y=1)


def clfield():
     t2.delete(0,END)
     t3.delete(0,END)
     t4.delete(0,END)

def maxrec():
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("select * from tablemast ")
    mydata=mycur.fetchall()
    mx=0
    for i in mydata:
        mx=i[0]
    mx=mx+1
    t1.delete(0,END)
    t1.insert(0,mx)
    clfield()
def saverec():
    s1=t1.get()
    s2=t2.get()
    s3=t3.get()
    s4=t4.get()
    if s2.strip()=="":
        messagebox.showinfo('Warn...','please enter tb capacity')
        return
    if s3.strip()=="":
        messagebox.showinfo('Warn...','please enter tb type')
        return
    if s4.strip()=="":
        messagebox.showinfo('Warn..','please enter tb rate')
        return

    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("insert into tablemast values("+s1+",'"+s2+"','"+s3+"','"+s4+"')")
    mydb.commit()
    messagebox.showinfo('Confirm',"Rec is save")
    maxrec()
def serrec():
    s1=t1.get()
    clfield()
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("select * from tablemast where tbno="+s1)
    mydata=mycur.fetchone()
    if mydata is not None:
        t2.insert(0,mydata[1])
        t3.insert(0,mydata[2])
        t4.insert(0,mydata[3])

    else:
        messagebox.showinfo('Confirm',"Rec is found")
def uprec():
    s1=t1.get()
    s2=t2.get()
    s3=t3.get()
    s4=t4.get()
    if s2.strip()=="":
        messagebox.showinfo('Warn...','pls enter tb capacity  ')
        return
    if s3.strip()=="":
        messagebox.showinfo('Warn...','pls enter tb type')
        return
    if s4.strip()=="":
        messagebox.showinfo('Warn...','pls enter tb rate')
        return

    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("update tablemast set tbcapacity="+s2+",tbtype='"+s3+"',tbrate="+s4+" where tbno="+s1)
    mydb.commit()
    messagebox.showinfo('Confirm',"rec is updated")
    maxrec()
def  delrec():
    s1=t1.get()
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    ans=messagebox.askyesnocancel('Confirm','Are U Sure Delete Rec?')
    if ans==True:
        mycur.execute("delete from tablemast  where tbno="+s1)
        mydb.commit()
        messagebox.showinfo('Confirm',"Rec is delete")
        maxrec()
win.title("Table Entry Form")
win.geometry("600x600")
f1=("Bahnschrift SemiCondensed",18,'bold',)

L1=Label(win,text="Table Entry Form",font=("Bookman Old Style",26,'bold',))
L1.place (x=350,y=30)

L2=Label(win,text="Tb no",font=f1,height=1)
L2.place(x=290,y=140)

t1=Entry(win,bd=2,font=f1)
t1.place(x=420,y=140)

L3=Label(win,text="Tb capacity",font=f1,height=1)
L3.place(x=290,y=210)

t2=Entry(win,bd=2,font=f1)
t2.place(x=420,y=210)

L4=Label(win,text="Tb type",font=f1,height=1)
L4.place(x=290,y=280)

t3=Entry(win,bd=2,font=f1)
t3.place(x=420,y=280)

L5=Label(win,text="Tb rate",font=f1,height=1)
L5.place (x=290,y=350)

t4=Entry(win,bd=2,font=f1)
t4.place(x=420,y=350)


b1=Button(win,text="Add",font=f1,width=7,height=1,command=maxrec)
b1.place(x=150,y=450)

b2=Button(win,text="Save",font=f1,width=7,height=1,command=saverec)
b2.place(x=260,y=450)

b3=Button(win,text="Ser",font=f1,width=7,height=1,command=serrec)
b3.place(x=370,y=450)

b4=Button(win,text="Update",font=f1,width=7,height=1,command=uprec)
b4.place(x=480,y=450)

b5=Button(win,text="Del",font=f1,width=7,height=1,command=delrec)
b5.place(x=590,y=450)

b6=Button(win,text="Exit",font=f1,width=7,height=1,command=quit)
b6.place(x=700,y=450)

win.geometry("900x600")
win.mainloop()
























