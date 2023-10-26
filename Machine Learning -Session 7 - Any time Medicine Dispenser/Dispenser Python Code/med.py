import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *
import random
import sqlite3 
import time


txt =""
def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Medicine Dispenser Login')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#B64D4D")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="orange")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Medicine Dispenser Login",fg="white",bg="orange")
    heading.config(font=('calibri 25'))
    heading.place(relx=0.2,rely=0.1)

    #UID 
    ulabel = Label(login_frame,text="    UID        ",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='white',fg='black',textvariable = password,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                #print(logdata)
                
                menu(a)
                break
        else:
            error = Label(login_frame,text="Wrong UID or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,fg="white",bg="black")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Medicine Dispenser App')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#FFBC25")
    img = PhotoImage(file="bac.png")
    sup_canvas.create_image(12,10,image=img,anchor=NW)
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#BADA55")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Medicine Dispenser SignUp",fg="#FFA500",bg="#BADA55")
    heading.config(font=('calibri 25'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='white',bg='black')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #UID
    ulabel = Label(sup_frame,text="    UID      ",fg='white',bg='black')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='white',bg='black')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='white',fg='black',textvariable = passW,show="*")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='white',bg='black')
    clabel.place(relx=0.217,rely=0.7)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        UID = user.get()
        password = pas.get()
        country = c.get()
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(c.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(c.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="UID and password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="UID can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('medd.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, UID text,PASSWORD text,COUNTRY text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,UID,password,country)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            #print(z)
            #L2.config(text="UID is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('medd.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="#BADA55", fg="black")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Medicine Dispenser Menu')
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="orange")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#7FFFD4")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(menu_canvas,text=' M E D I C I N E   D I S P E N S E R ',fg="white",bg="orange") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    abcdefgh='Hello '+ abcdefgh
    level34 = Label(menu_frame,text=abcdefgh,bg="black",font="calibri 18",fg="white")
    level34.place(relx=0.17,rely=0.15)
    
    level = Label(menu_frame,text='Please answer the following questions !!',bg="orange",font="calibri 18")
    level.place(relx=0.17,rely=0.3)
    
    
    var = IntVar()
    
    def navigate():
            menu.destroy()
            meddi()
        

    letsgo = Button(menu_frame,text="Let's Go",bg="black",fg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.45,rely=0.8)
    menu.mainloop()




    
def meddi():
    
    global e, txt
    e = Tk()
    e.title('Medicine Dispenser BOT')
    
    easy_canvas = Canvas(e,width=720,height=440,bg="orange")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="#BADA55")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
        
    def messageWindow():
        win = Toplevel()
        win.title('Condition')
        message = "How is your health Condition?"
        Label(win, text=message).pack()
        def closeall():
            global txt
            if(txt=="End"):
                win.destroy()
                e.destroy()
                serialout()
            else:
                win.destroy()
                

        Button(win, text='Mild', command=closeall).pack()
        Button(win, text='Severe', command=closeall).pack()

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0

    
    easyQ = [
                 [
                     "Do you have cold?",
                     "Yes",
                     "No"
                    
 
                 ] ,
                 [
                     "Do you have cough?" ,
                     "Yes",
                     "No"

                     
                 ],
                [
                    "Do you have throat pain?" ,
                    "Yes",
                    "No"
                  
                ],
                [
                    "Do you have headache?" ,
                    "Yes",
                    "No"
              
                ],
                [
                    "Do you have fever?" ,
                    "Yes",
                    "No"
                  
                ]
            ]

    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="orange")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="#BADA55")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="#BADA55")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)


    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    def calc():
        global score
        if (var.get() =="Yes"):
            messageWindow()

            
            

    def display():
        global txt
        
        if len(li) == 1 and txt=="End":
                e.destroy()
                serialout()
        if len(li) == 2:
            
            txt="End"
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            calc()
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])

            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

    
    nextQuestion = Button(easy_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()

def serialout():
    import numpy as np
    import serial
    MCData = serial.Serial(port = "COM15", baudrate=115200,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
   
    sh = Tk()
    sh.title('Your Result')
 
    
    def callsignUpPage():
        sh.destroy()
        start()
    

    canvas = Canvas(sh,width = 720,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="bac.png")
    canvas.create_image(12,10,image=img,anchor=NW)
    heading = Label(sh,text="Please Take your Tablet",fg="#FFA500",bg="#BADA55")
    heading.config(font=('calibri 25'))
    heading.place(relx=0.28,rely=0.45)
    button = Button(sh, text='Quit',command = callsignUpPage,bg="red",fg="yellow") 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)

    
    time.sleep(2)

    MCData.write(("1").encode('utf-8'))
    sh.mainloop()
    
def start():
    global root 
    root = Tk()
    root.title('Medicine Dispenser')
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="bac.png")
    canvas.create_image(12,10,image=img,anchor=NW)
    
    heading = Label(root,text="Medicine Dispenser",fg="#FFA500",bg="#BADA55")
    heading.config(font=('calibri 25'))
    heading.place(relx=0.32,rely=0.45)
    button = Button(root, text='Start',command = signUpPage,bg="red",fg="yellow") 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()
    

