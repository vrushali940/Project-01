#Desktop Form
from tkinter import *

win=Toplevel()

def open_custreg():
    import custreg

def open_custmast():
    import cms1


def open_tabreg():
    import tabreg


def open_tablemast():
    import cms2

def open_itemreg():
    import itemreg


def open_itemmast():
    import cms3

def open_transreg():
    import Transreg


def open_transmast():
    import cms4

def open_ordreg():
    import ordreg

def open_orderdetail():
    import cms5
def on_button_click():
    print("Button Clicked")
f1=('arial',15,'bold')
l1=Label(win,text="Cafe  Management  System",font=('Gabriola',36,'bold'))
l1.place(x=140,y=20)

l2=Label(win,text='Developed By',font=('cambria',22,'bold'))
l2.place(x=90,y=640)
l3=Label(win,text='Vrushali Mahajan',font=('cambria',18,'bold'))
l3.place(x=115,y=690)

l2=Label(win,text='Guidance By',font=('cambria',20,'bold'))
l2.place(x=550,y=640)
l3=Label(win,text='Prof. Pankaj Adawadkar',font=('cambria',18,'bold'))
l3.place(x=550,y=690)

b1=Button(win,text='customer Entry Form',font=f1,bg='#ECFFDC',width=20,command=open_custmast)
b1.place(x=80,y=150)

b2=Button(win,text='Table Entry From',font=f1,bg='#ECFFDC',width=20,command=open_tablemast)
b2.place(x=180,y=230)

b3=Button(win,text='Item Entry Form',font=f1,bg='#ECFFDC',width=20,command=open_itemmast)
b3.place(x=280,y=310)


b5=Button(win,text='Results',font=f1,bg='#ECFFDC',width=20,command=open_transmast)
b5.place(x=350,y=390)

b6=Button(win,text='Exit',font=f1,bg='#ECFFDC',width=20,command=quit)
b6.place(x=500,y=550)

win.title("Cafe System")
win.configure(bg='#6082B6')
win.geometry("800x800")
mb=Menu(win)
ReportMenu=Menu(mb)
ReportMenu.add_command(label="Customer Register " ,command=open_custreg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Table Register ",command=open_tabreg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Item Register ",command=open_itemreg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Transaction Register ",command=open_transreg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Orderdetail Register ",command=open_ordreg)
ReportMenu.add_separator()
ReportMenu.add_command(label="Exit")
mb.add_cascade(label="Report",menu=ReportMenu)
win.config(menu=mb)
win.mainloop()
