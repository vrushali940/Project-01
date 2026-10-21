import tkinter as tk
from tkinter import *
import mysql.connector
win = Tk()  # parent window
win.title("Customer Register")
win.geometry("650x500")  # width and height of window
#https://www.plus

mydb=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="cms"
    )
mycur=mydb.cursor()

mycur.execute("SELECT * FROM custmast")
r_set=mycur.fetchall()
f1=("arial",15,'bold')
l1=Label(win,text="Customer Register ",font=("Arial",20,'bold'),bg='white')


e=Label(win,width=10,text='Cust No',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red' ,font=f1)
e.grid(row=0,column=0)
e=Label(win,width=10,text='Cust Name',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=1)
e=Label(win,width=10,text='Address',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=2)
e=Label(win,width=10,text='City',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=3)
e=Label(win,width=10,text='Contact',borderwidth=2, relief='ridge',anchor='w',bg='white',fg='red',font=f1)
e.grid(row=0,column=4)
#i=1



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
