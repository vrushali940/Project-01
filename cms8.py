#Billform
from tkinter import *
import mysql.connector
from PIL import Image,ImageTk
def showall():
    mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
    mycur=mydb.cursor()
    mycur.execute("select t.trno,t.trdate,t.cno,c.cname,t.tbno,t.amount,t.discount,t.netamt,t1.ordno, t1.icode,i.iname,t1.qty,t1.rate,t1.amt from transmast t,orderdetail t1,itemmast i,custmast c where t.trno=t1.ordno and t.cno=c.cno and t1.icode=i.icode and t.trno=(select max(trno) from transmast)")
    mydata=mycur.fetchone()
    return mydata

ans=showall()


win=Tk()
win.title("bill form")
f1=("arial",15,"bold")
win.configure(bg="#FFFFFF")

path=Image.open(r"D:\Photo Editor\bg10.jpg")

render=ImageTk.PhotoImage(path)
img=Label(win,image=render)
img.place(x=70,y=550)

l1=Label(win,text="CHAITANYA CAFE",font=("Gabriola",36,"bold"),)
l1.place(x=330,y=15)

l3=Label(win,text="Trno",font=f1,)
l3.place(x=70,y=200)
l4=Label(win,text=ans[0],font=f1)
l4.place(x=180,y=200)
l5=Label(win,text="Trdate",font=f1,)
l5.place(x=450,y=200)
l6=Label(win,text=ans[1],font=f1)
l6.place(x=570,y=200)
l5=Label(win,text="Cno",font=f1,)
l5.place(x=70,y=260)
l4=Label(win,text=ans[0],font=f1)
l4.place(x=180,y=260)

l7=Label(win,text="Cust Name",font=f1,)
l7.place(x=450,y=260)
l8=Label(win,text=ans[3],font=f1)
l8.place(x=570,y=260)
l9=Label(win,text="Tbno",font=f1,)
l9.place(x=70,y=320)
l10=Label(win,text=ans[4],font=f1)
l10.place(x=180,y=320)
l11=Label(win,text="Icode",font=f1,width=6)
l11.place(x=50,y=380)
l12=Label(win,text=ans[8],font=f1)
l12.place(x=60,y=430)
l13=Label(win,text="Iname",font=f1,width=6)
l13.place(x=200,y=380)
l14=Label(win,text=ans[10],font=f1)
l14.place(x=200,y=430)
l15=Label(win,text=" Qty ",font=f1,width=6)
l15.place(x=340,y=380)
l16=Label(win,text=ans[11],font=f1)
l16.place(x=370,y=430)
l17=Label(win,text="Rate",font=f1,width=6)
l17.place(x=500,y=380)
l18=Label(win,text=ans[12],font=f1)
l18.place(x=510,y=430)
l19=Label(win,text="Amt",font=f1,width=6)
l19.place(x=640,y=380)
l20=Label(win,text=ans[13],font=f1)
l20.place(x=650,y=430)
l21=Label(win,text="Amount",font=f1,)
l21.place(x=580,y=550)
l22=Label(win,text=ans[5],font=f1)
l22.place(x=680,y=550)
l23=Label(win,text="Discount",font=f1,)
l23.place(x=580,y=630)
l24=Label(win,text=ans[6],font=f1)
l24.place(x=680,y=630)
l25=Label(win,text="NetAmt",font=f1,)
l25.place(x=580,y=710)
l26=Label(win,text=ans[7],font=f1)
l26.place(x=680,y=710)
win.geometry("900x600")
mainloop()