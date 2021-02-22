#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : main.py
# Author            : taotao <taotao@myhexin.com>
# Date              : 2021.02.22
# Last Modified Date: 2021.02.22
# Last Modified By  : taotao <taotao@myhexin.com>

from tkinter import *
from functools import partial
from tkinter import messagebox

def check(name, password):
    name     = name.get()
    password = password.get()
    if name == "Steven" and password == "123":
        messagebox.showinfo("Login Success ", "The Test Start!")
    else:
        messagebox.showerror("Error","Your name or password is wrong")
    # by taotao:  退出 messagebox




def login_check():
    loginwindow=Tk()
    loginwindow.title('Login Window')
    loginwindow.geometry('400x400')
    loginwindow.configure(bg='pink')
     # Create a label
     # TO create alabel you can use this label class from tkinter
    name=Label(loginwindow,text='Name:')
    name.place(x=30,y=50)
    name.configure(bg='pink')
    # create another label to display password
    password = Label(loginwindow, text='Password:')
    password.place(x=30, y=90)
    password.configure(bg='pink')

    username_entry = Entry(loginwindow)
    username_entry.place(x=120, y=50)

    password_entry = Entry(loginwindow)
    password_entry.place(x=120, y=90)

    # create Button Object
    login_B = Button(loginwindow, text='Login', command=partial(check, username_entry, password_entry))
    login_B.place(x=110, y=140)
    Quit_B = Button(loginwindow, text='quit', command=exit)
    Quit_B.place(x=240, y=140)


mainwindow = Tk()  # This line will create an object of Tk class
mainwindow.title('Test Login')  # title() function will help to st some title
mainwindow.geometry('1000x1000')
mainwindow.configure(bg='light GREY')  # configure() function will help to set some basic setting
# Create an object of Button class

login = Button(mainwindow, bg='blue', text='login', fg='black', font='15',width=18,height=5,
               command=login_check)  # this will create an object of button class
login.pack()
mainwindow.mainloop()  # mianloop() function Will show the window
