#Login Form
from tkinter import *
import tkinter as tk
from tkinter import messagebox
def open_pas():
   import cms7
def login():
    username = t1.get()
    password = t2.get()
    if username == "vrushali"and password == "5555":
        open_pas()
    else:
        if username != "vrushali":
            messagebox.showinfo('Login Failed', "Invalid username")
        else:
            messagebox.showinfo('Login Failed', "Invalid password")

win= Toplevel()


win.configure(bg="#ffe4e1")


win.title("cafe system")

f1=('arial',15,'bold',)
frame1 = tk.Frame(win, bg="#B48395", width=460, height=460, relief="raised", bd=5,)
frame1.pack(pady=100)

l1=Label(win,text='*Login*',font=("Georgia",30,'bold'),bg='#B48395',fg='white')
l1.place(x=350,y=140)

l2=Label(win,text='User name',font=f1,width=10,bg="#B48395",fg='white')
l2.place(x=240,y=260)
t1=Entry(win,bd=4,font=f1,width=18, bg="black",fg='white')
t1.place(x=420,y=260)

l4=Label(win,text='Password',font=f1,width=10, bg="#B48395",fg='white')
l4.place(x=240,y=330)
t2=Entry(win,bd=4,font=f1,width=18, bg="black",fg='white',show='*')
t2.place(x=420,y=330)

b1=Button(win,text='Login',font=f1,width=7,bg='grey', command=login)
b1.place(x=310,y=410)
b2=Button(win,text='Cancel',font=f1,width=7,bg='grey', command=quit)
b2.place(x=440,y=410)

win.geometry("900x800")
mainloop()
