import tkinter as tk
from tkinter import *
import mysql.connector
win = Tk()  # parent window
win.title("Transaction Register")
win.geometry("650x650")  # width and height of window
#https://www.plus2net.com/python/tkinter-mysql.php0
####### end of connection ####

mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
mycur=mydb.cursor()

mycur.execute("SELECT * FROM transmast")
r_set=mycur.fetchall()
f1=("arial",15,'bold')
l1=Label(win,text="Transaction Register ",font=("Arial",20,'bold'),bg='white')


e=Label(win,width=10,text='TrNo',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red' ,font=f1)
e.grid(row=0,column=0)
e=Label(win,width=10,text='Trdate',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=1)
e=Label(win,width=10,text='cno',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=2)
e=Label(win,width=10,text='Tbno',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=3)
e=Label(win,width=10,text='Amount',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=4)
e=Label(win,width=10,text='Discount',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=5)
e=Label(win,width=10,text='Net Amt',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=6)



i=1
for student in r_set:
    for j in range(len(student)):
        e = Entry(win, width=10, fg='blue',font=("arial",15,'bold'))
        e.grid(row=i+1, column=j)
        e.insert(END, student[j])
        e.configure(state='disabled')
    i = i + 1
win.config(bg='white')
win.mainloop()

