#Transmast
from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter .ttk import Combobox
from tkinter .ttk import Combobox,Treeview
from tkcalendar import DateEntry
from PIL import Image,ImageTk
win=Toplevel()
f1=("Book Antiqua",16,'bold')
picode=[]
pqty=[]
prate=[]
pamt=[]

path=Image.open(r"D:\Photo Editor\bg16.jpg")
render=ImageTk.PhotoImage(path)
img=Label(win,image=render)
img.place(x=1,y=1)

def calculate(event=None):
    try:
        q=int(t8.get()) if t8.get().strip() else 0 #Default to 0 input is empty
        r=int(t9.get()) if t9.get().strip() else 0 #Default to 0 input is empty
        t=q*r
        t10.delete(0,END)
        t10.insert(0,str(t))
    except ValueError:
        messagebox.showerror("Error","please entr valid no")


def calculate1(event):
    amt=int(t5.get())  if t5.get().strip() else 0 #Default to 0 input is empty
    dis=int(t6.get())  if t6.get().strip() else 0 #Default to 0 input is empty
    netamt=amt-dis
    t7.delete(0,END)
    t7.insert(0,str(netamt))
def show():
    icode=ch2.get()
    iname=L16.cget("text")
    qty=t8.get()
    rate=t9.get()
    amt=t10.get()

    if (icode==""):
        messagebox.showinfo('Warn...','Please enter the ino & iname')
        return
    if (iname==""):
        messagebox.showinfo('Warn....','Please enter the iname ' )
        return
    if (int(qty)<=0):
        messagebox.showinfo('Warn....','Please enter the qty')
        return
    if (int(rate)<=0):
        messagebox.showinfo('Warn....','Please enter the rate')
        return
    if (amt==""):
        messagebox.showinfo('Warn.....','Please enter the amt')
        return
    t1.insert('',index='end',values=(icode,iname,qty,rate,amt))
    picode.append(icode)
    pqty.append(qty)
    prate.append(rate)
    pamt.append(amt)
    t=int(t5.get())
    pt = int(t10.get())
    pt = pt + t
    t5.delete(0, END)
    t5.insert(0, str(pt))
    t8.delete(0, END)
    t9.delete(0, END)
    t10.delete(0, END)
    t8.insert(0, 0)
    t9.insert(0, 0)


def clfield():
     cal.delete(0,END)
     ch.delete(0,END)
     ch1.delete(0,END)
     t5.delete(0,END)
     t6.delete(0,END)
     t7.delete(0, END)
     ch2.delete(0,END)
     t9.delete(0,END)
     t10.delete(0,END)
     t8.insert(0,0)
     t9.insert(0,0)
     t5.insert(0,0)
     t6.insert(0,0)

def fetchrec():
     mydb = mysql.connector.connect(
             user="root",
             password="",
             host="localhost",
             database="cms"
     )
     cursor=mydb.cursor()
     cursor.execute("select cno from custmast")
     data=cursor.fetchall()
     return data
def fetchrec1(event):
    s1=ch.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    cursor=mydb.cursor()
    cursor.execute("select * from Custmast where cno="+s1)
    data1=cursor.fetchone()
    L14.config(text=""+str(data1[1]))


def fetchtabledata():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    cursor = mydb.cursor()
    cursor.execute("select tbno from tablemast")
    data = cursor.fetchall()
    return data


def fetchrectabrec(event):
    s1 = ch1.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )

def fetchicodata():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    cursor = mydb.cursor()
    cursor.execute("select icode from Itemmast")
    data = cursor.fetchall()
    return data


def fetchrecicrec(event):
    s1 = ch2.get()
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    cursor = mydb.cursor()
    cursor.execute("select * from itemmast where icode=" + s1)
    data1 = cursor.fetchone()
    L16.config(text="" + str(data1[1]))

def maxrec():
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur = mydb.cursor()
    mycur.execute("select * from transmast")
    mydata=mycur.fetchall()
    mx=0
    for i in mydata:
        mx=i[0]
    mx= mx+1
    t12.delete(0,END)
    t12.insert(0,mx)
    clfield()
    t1.delete(*t1.get_children())

def saverec():
    s1=t12.get()
    s2=cal.get()
    s3=ch.get()
    s4=ch1.get()
    s5 = t5.get()
    s6 = t6.get()
    s7 = t7.get()
    if s2.strip()=="":
        messagebox.showinfo('Warn...','please enter Trdate')
        return
    if s3.strip()=="":
        messagebox.showinfo('Warn...','please enter cno ')
        return
    if s4.strip()=="":
        messagebox.showinfo('Warn..','please enter Tbno ')
        return

    if s5.strip()=="":
        messagebox.showinfo('Warn...','please enter Amount')
        return
    if s6.strip()=="":
       messagebox.showinfo('Warn...','please enter Discount')
       return
    if s7.strip()=="":
       messagebox.showinfo('Warn...','please enter Net amount')
       return

    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("insert into transmast values("+s1+",'"+s2+"',"+s3+","+s4+","+s5+","+s6+","+s7+")")
    mydb.commit()
    i=0
    while i<len(pqty):
       mycur.execute("insert into orderdetail values("+s1+","+picode[i]+","+pqty[i]+","+prate[i]+","+pamt[i]+")")
       mydb.commit()
       i=i+1

    messagebox.showinfo('Confirm',"Record is save")
    maxrec()
def serrec():
    s1=t12.get()
    clfield()
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("select * from transmast where trno="+s1)
    mydata=mycur.fetchone()
    if mydata is not None:
        cal.insert(0,mydata[1])
        ch.insert(0,mydata[2])
        ch1.insert(0,mydata[3])
        ch2.insert(0, mydata[4])
        t5.insert(0, mydata[5])
        t6.insert(0,mydata[6])
        t7.insert(0, mydata[7])
    else:
        messagebox.showinfo('Confirm',"Rec is found")
def uprec():
    s1=t12.get()
    s2=cal.get()
    s3=ch.get()
    s4=ch1.get()
   # s5 = t5.get()
    s5 = t5.get()
    s6 = t6.get()
    s7 =  t7.get()
    if s2.strip()=="":
        messagebox.showinfo('Warn...','pls enter Trdate ')
        return
    if s3.strip()=="":
        messagebox.showinfo('Warn...','pls enter cno')
        return
    if s4.strip()=="":
        messagebox.showinfo('Warn...','pls enter Tbno ')
        return

    if s5.strip() == "":
        messagebox.showinfo('Warn...', 'pls enter amount ')
        return

    if s6.strip() == "":
        messagebox.showinfo('Warn...', 'pls enter discount ')
        return
    if s7.strip() == "":
        messagebox.showinfo('Warn...', 'pls enter Net Amt ')
        return
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("update transmast set trdate="+s2+",cno="+s3+",tbno="+s4+",Amount="+s5+",Discount="+s6+",Net Amount="+s7+"where trno="+s1)
    mydb.commit()
    messagebox.showinfo('Confirm',"rec is updated")
    maxrec()
def  delrec():
    s1=t12.get()
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    ans=messagebox.askyesnocancel('Confirm','Are U Sure Delete Rec?')
    if ans==True:
        mycur.execute("delete from transmast where trno="+s1)
        mydb.commit()
        messagebox.showinfo('Confirm',"Rec is delete")
        maxrec()
def delrec1():
    selected_item=t1.selection()
    if not selected_item:
        messagebox.showinfo('Warn...','Please select a row to delete')
        return
    ans=messagebox.askyesnocancel('Confirm','Are You Sure You Want To Delete The Record?')
    for item in selected_item:
               t1.delete(item)

win.title("Transaction Entry Form")
win.geometry("600x600")
f1=("Book Antiqua",16,'bold')
L1=Label(win,text="Transaction Details",font=("Book Antiqua",20,'bold'))
L1.place (x=310,y=20)

L2=Label(win,text="Trno",font=f1)
L2.place(x=40,y=80)

t12=Entry(win,bd=2,font=f1)
t12.place(x=160,y=80)

#entry = Entry(win, bd=2, font=f1)
#t1_entry.place(x=160, y=80)

L3=Label(win,text="Trdate",font=f1)
L3.place(x=460,y=80)

cal=DateEntry(win,selectmode='day',font=f1,width=18,date_pattern="yyy-mm-dd")
cal.grid(row=15,column=15,padx=15)
cal.place(x=570,y=80)
L4=Label(win,text="cno",font=f1)
L4.place(x=40,y=130)
data=fetchrec()
ch=Combobox(win,font=f1,width=18,values=data)
ch.place(x=160,y=130)
ch.bind("<<ComboboxSelected>>",fetchrec1)



L5=Label(win,text="Tbno",font=f1)
L5.place(x=40,y=180)
data=fetchtabledata()
ch1=Combobox(win,font=f1,width=18,values=data)
ch1.place(x=160,y=180)
ch1.bind("<<ComboboxSelected>>",fetchrectabrec)

L6=Label(win,text="Icode",font=f1,width=5)
L6.place(x=70,y=230)
data=fetchicodata()
ch2=Combobox(win,font=f1,width=8,values=data,)
ch2.place(x=40,y=280)
ch2.bind("<<ComboboxSelected>>",fetchrecicrec)


L8=Label(win,text="Qty",font=f1,width=5)
L8.place(x=390,y=230)
t8=Entry(win,bd=2,font=f1,width=10)
t8.place(x=370,y=280)
t8.bind("<KeyRelease>",calculate)

L9=Label(win,text="Rate",font=f1,width=5)
L9.place(x=540,y=230)
t9=Entry(win,bd=1,font=f1,width=10)
t9.place(x=510,y=280)
t9.bind("<KeyRelease>",calculate)


L10=Label(win,text="Amt",font=f1,width=5)
L10.place(x=690,y=230)
t10=Entry(win,bd=1,font=f1,width=10)
t10.place(x=670,y=280)


L11=Label(win,text="Amount",font=f1)
L11.place(x=530,y=570)
t5=Entry(win,bd=2,font=f1)
t5.place(x=660,y=570)

L12=Label(win,text="Discount%",font=f1)
L12.place(x=530,y=620)
t6=Entry(win,bd=2,font=f1)
t6.place(x=660,y=620)
t6.bind("<KeyRelease>",calculate1)

L13=Label(win,text="Net amt",font=f1)
L13.place(x=530,y=670)
t7=Entry(win,bd=2,font=f1)
t7.place(x=660,y=670)

L14=Label(win,text="--------------------",font=f1,width=15)
L14.place(x=590,y=130)

L15=Label(win,text="cust name",font=f1)
L15.place(x=460,y=130)

L16=Label(win,text="----------",font=f1,width=10)
L16.place(x=190,y=280)
L7=Label(win,text="Iname",font=f1,width=5)
L7.place(x=220,y=230)

b7=Button(win,text="Add",font=f1,command=show)
b7.place(x=790,y=180)

t1=Treeview(win,columns=("Icode","Iname","Qty","Rate","Amt"),show="headings",height=8)
t1.heading("Icode",text='Icode')
t1.heading("Iname",text='Iname')
t1.heading("Qty",text='Qty')
t1.heading("Rate",text='Rate')
t1.heading("Amt",text='Amt')

t1.column("Icode",width=115,anchor="center")
t1.column("Iname",width=155,anchor="center")
t1.column("Qty",width=115,anchor="center")
t1.column("Rate",width=115,anchor="center")
t1.column("Amt",width=115,anchor="center")
t1.place(x=80,y=340)


b1=Button(win,text="Add",font=f1,width=7,command=maxrec)
b1.place(x=200,y=730)

b2=Button(win,text="Save",font=f1,width=7,command=saverec)
b2.place(x=350,y=730)


b3=Button(win,text="Exit",font=f1,width=7,command=quit)
b3.place(x=500,y=730)

win.geometry("900x800")
win.mainloop()



























