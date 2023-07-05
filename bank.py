from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import *
from tkinter import ttk
from datetime import datetime

MAINLIST = []
# mysql.connector
import mysql.connector as mcon
mydb = mcon.connect(host='localhost', user='root', passwd='1234')
print(mydb.is_connected())
mycursor = mydb.cursor()
mycursor.execute('SHOW DATABASES')
for i in mycursor:
    MAINLIST.append(i[0])
ADMINCHECK=0
if 'admin' not in MAINLIST:
    ADMINCHECK = 1
    ADMINUSER = input('Enter your admin username      :      ')
    ADMINPASSWD = input('Enter your admin password       :     ')

for i in ['ADMIN', 'ACCOUNT_NUMBER', 'SAVINGS', 'CURRENT']:
    try:
        mycursor.execute("CREATE DATABASE " + i)
    except:
        continue

mydb.close()
_mydb = mcon.connect(host='localhost', user='root', passwd='1234', database='ADMIN')
_mycursor = _mydb.cursor()
if ADMINCHECK == 1:
    try:
        _mycursor.execute("CREATE TABLE ADMIN( USERNAME varchar(20),PASSWORD varchar(20))")
        _mycursor.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES('{}','{}')".format(ADMINUSER, ADMINPASSWD))
        _mydb.commit()
    except:
        pass
_mydb.close()
# Basic window is created
root = Tk()
root.geometry("1360x680")
root.title('BANK')
root.configure(background='white')
fs1 = 12;
fs2 = 10;
fs3 = 16;
fs4 = 18;
fs5 = 25
i = None
length = None
g = 0
BD = 0
balance = None
balance1 = None
balance2 = None
check = 0;
check1 = 1;
check2 = 0;
check3 = 0;
check4 = 0;
check5 = 0;
check6 = 0;
check7 = 0
chdepdraw = 0
LDICT = {1: None, 2: None, 3: None, 4: None, 5: None,
         6: None, 7: None, 8: None, 9: None, 10: None,
         11: None, 12: None, 13: None, 14: None, 15: None,
         16: None, 17: None, 18: None, 19: None, 20: None,
         21: None, 22: None, 23: None, 24: None, 25: None,
         26: None, 27: None, 28: None, 29: None, 30: None,
         31: None, 32: None, 33: None, 34: None, 35: None,
         36: None, 37: None, 38: None, 39: None, 40: None,
         41: None, 42: None, 43: None, 44: None, 45: None,
         46: None, 47: None, 48: None, 49: None, 50: None,
         51: None, 52: None, 53: None, 54: None, 55: None,
         56: None, 57: None, 58: None, 59: None, 60: None}
LLIST = []
LDvar = 1
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
text = text2 = None
givenusr = givenpass = None
dict = {}
E_E1 = StringVar();
E_E2 = StringVar();
E_E3 = StringVar();

E_E4 = StringVar();
E_E5 = StringVar();
E_E6 = StringVar();
E_E7 = StringVar();
E_E8 = StringVar();
E_E9 = StringVar();
E_E10 = StringVar();
E_E11 = StringVar();
E_E12 = StringVar();
E_E13 = StringVar();
E_E14 = StringVar();
E_E15 = StringVar();
E_E16 = StringVar()

E_E17 = IntVar();
E_E18 = IntVar();
E_E19 = IntVar();
E_E20 = IntVar();
E_E21 = StringVar();
E_E22 = IntVar();
E_E23 = StringVar();
E_E24 = StringVar();

mydbvar1 = None
mydbvar2 = None
mydbvar3 = None
mydbvar4 = None
mydbvar5 = None

st = st1 = None
radio1 = IntVar()
radio2 = IntVar()

def f():
    list = root.pack_slaves()
    for l in list:
        l.destroy()

def f1():
    global f1_, check2
    Tops = Frame(root, width=1360, height=60, bd=1, bg='#D8BFD8', relief=RIDGE)
    Tops.pack(side=TOP)
    Title = Label(Tops, font=('arial', 40, 'bold'), text="\t\t  BANK \t\t\t ", bg='#D8BFD8').grid(row=0, column=0,
                                                                                                  padx=100)

    f1_ = Frame(root, width=1360, height=40, bd=1, bg='#FFFFFF', relief=FLAT)
    f1_.pack(side=TOP, anchor=W)
    if check2 == 0:
        Home = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=8, relief=RIDGE, text="Home",
                      command=fHome).grid(row=0, column=0)
        Pbank = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=17, relief=RIDGE, text="Personal Banking",
                       command=fLogpb).grid(row=0, column=1)
        NEWacc = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=17, relief=RIDGE, text="New Account",
                        command=ACCOUNT, state=NORMAL).grid(row=0, column=2)
        Log = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=8, relief=RIDGE, text="Login", command=fLogpb,
                     state=NORMAL).grid(row=0, column=3)
        Logout = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=13, relief=RIDGE, text="Log Out",
                        command=logout, state=DISABLED).grid(row=0, column=5)


    else:
        Home = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=8, relief=RIDGE, text="Home",
                      command=loggedin).grid(row=0, column=0)
        Pbank = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=17, relief=RIDGE, text="Personal Banking",
                       command=loggedin).grid(row=0, column=1)
        NEWacc = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=17, relief=RIDGE, text="New Account",
                        command=ACCOUNT, state=DISABLED).grid(row=0, column=2)
        Log = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=8, relief=RIDGE, text="Login", command=fLogpb,
                     state=DISABLED).grid(row=0, column=3)
        Logout = Button(f1_, bd=1, fg="#000000", font=('arial', fs2), width=13, relief=RIDGE, text="Log Out",
                        command=logout, state=NORMAL).grid(row=0, column=5)
    Blank = Label(f1_, bd=2, bg="#FFFF00", width=95, padx=0, pady=0).grid(row=0, column=4)

def fHome():
    global i, g, f5_, img1, img2, img3, img4, img5, img6, img7, img8
    f()
    f1()
    g += 1
    f2_ = Frame(root, width=1360, height=40, bd=1, bg='#FF0050', relief=RIDGE)
    f2_.pack(side=TOP)
    info = Label(f2_, font=('arial', fs2), text="The Bank never asks for confidential information such as PIN and OTP from customers.\
                Any such call can be made by a fraudster.Please do not share personal info.", bg='#FF0050')
    info.grid(row=0, column=0, padx=170)
    f3_ = Frame(root, width=680, height=300, bd=1, bg='#EEFFFF', relief=RIDGE)
    f3_.pack(side=LEFT, anchor=N)
    f4_ = Frame(root, width=680, height=300, bd=1, bg='#FAFD7B', relief=RIDGE)
    f4_.pack(side=RIGHT, anchor=N)

    img1 = PhotoImage(file='personal banking.png')
    pbimg = Label(f3_, image=img1).place(x=237.5, y=40)
    img2 = PhotoImage(file='log.png')
    pblog = Button(f3_, image=img2, relief=FLAT, command=fLogpb).place(x=280, y=140)

    img3 = PhotoImage(file='pbinfo.png')
    pbinfo = Label(f3_, image=img3, fg='#EEFFFF').place(x=3, y=250)

    f5_ = Frame(root, width=1360, height=280, bd=1, relief=RIDGE, bg='#EEFFFF');
    f5_.place(x=0, y=425)
    i = g % 5
    choices = ['banner1.png', 'banner2.png', 'banner3.png', 'banner4.png', 'banner5.png']
    img4 = PhotoImage(file=choices[i])
    baninfo = Label(f5_, image=img4, fg='#EEFFFF').place(x=4, y=0)
    root.mainloop()

def fLogpb():
    global text, check, check1
    global dict
    dict_form()
    f()
    f1()
    f5_.place_forget()
    f6_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f6_.pack(side=LEFT, anchor=N)
    f7_ = Frame(f6_, width=680, height=600, bd=1, bg='#F5F5F5', relief=FLAT)
    f7_.pack(side=LEFT, anchor=N)
    f8_ = Frame(f6_, width=680, height=600, bd=1, bg='#F5F5F5', relief=FLAT)
    f8_.pack(side=RIGHT, anchor=N)
    info1 = Label(f8_, font=('arial', fs1), text="WELCOME TO PERSONAL INTERNET BANKING", bg='#F5F5F5')
    info1.place(x=170, y=20)
    img5 = PhotoImage(file='login.png')
    pbimg = Label(f8_, image=img5).place(x=60, y=80)
    img6 = PhotoImage(file='info1.png')
    pbimg = Label(f7_, image=img6).place(x=155, y=300)
    img7 = PhotoImage(file='info2.png')
    pbimg = Label(f8_, image=img7).place(x=155, y=400)
    info2 = Label(f7_, font=('arial', fs2), text="Username and Password are case sensitive ", bg='#F5F5F5')
    info2.place(x=170, y=10)
    f9_ = Frame(f7_, width=680, height=250, bd=1, bg='#F5F5F5', relief=FLAT)
    f9_.place(x=0, y=50)
    usrnm1 = Label(f9_, font=('arial', fs3), text="Username", bg='#F5F5F5').place(x=80, y=25)
    E1 = Entry(f9_, font=('arial', fs3), bg='#F5F5F5', textvariable=E_E1).place(x=220, y=25)
    E_E1.set('ENTER')
    psswd1 = Label(f9_, font=('arial', fs3), text="Password", bg='#F5F5F5').place(x=80, y=65)
    E2 = Entry(f9_, font=('arial', fs3), bg='#F5F5F5', textvariable=E_E2, show='*').place(x=220, y=65)
    E_E2.set('ENTER')
    if check1 == 0:
        wrong = Label(f9_, font=('arial', fs2), text="Invalid Username,Password or captcha", bg='#F5F5F5',
                      fg='#0000FF').place(x=80, y=0)

    text = str(randint(100000, 999999))
    f10_ = Frame(f9_, width=118, height=48, bd=1, bg='#F5F5F5', relief=RIDGE)
    f10_.place(x=80, y=105)
    img8 = PhotoImage(file='captcha.png')
    img9 = PhotoImage(file='refresh.png')
    capimg1 = Label(f10_, text=text, font=('arial', 25), bg='#F5F5F5').place(x=1, y=1)
    cap2img = Label(f10_, image=img8).place(x=1, y=24)
    cap1 = Label(f9_, font=('arial', fs3), text="Captcha", bg='#F5F5F5').place(x=80, y=155)
    E3 = Entry(f9_, font=('arial', fs3), bg='#F5F5F5', textvariable=E_E3).place(x=220, y=155)
    E_E3.set(0)
    refresh1 = Button(f9_, image=img9, command=fLogpb).place(x=220, y=105)
    Login1 = Button(f9_, font=('arial', fs2, 'bold'), text="LOGIN", command=l).place(x=80, y=205)
    root.mainloop()

def l():
    global text, check, check1, dict
    if E_E3.get() == text:
        list1.append(E_E1.get())
        list1.append(E_E2.get())
        check = logchk(E_E1.get(), E_E2.get())
        if check == 1:
            check1 = 1
            loggedin()
        else:
            check1 = 0
            fLogpb()

    else:

        check1 = 0
        fLogpb()

def dict_form():
    global dict
    mydb1 = mcon.connect(host='localhost', user='root', database='ADMIN', passwd='1234')
    cursor1 = mydb1.cursor()
    cursor1.execute("Select USERNAME,PASSWORD from ADMIN")
    for i in cursor1:
        dict[i[0]] = i[1]
    mydb1.close()

def logchk(a, b):
    global dict
    givenusr = a
    givenpass = b
    try:
        if dict[a] == b:
            return 1
        else:
            return 0
    except:
        return 0

def loggedin():
    global check2, f5_, givenusr, givenpass
    check2 = 1
    f()
    f1()
    f5_.place_forget()

    f11_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f11_.pack(side=LEFT, anchor=N)

    Dep_Draw = Button(f11_, font=('arial', fs3, 'bold'), width=20, bg='#FFD6C1', relief=FLAT, bd=1,
                      text="Deposit/Withdraw", command=depdraw).place(x=80, y=100)
    Transfer = Button(f11_, font=('arial', fs3, 'bold'), width=20, bg='#FFDEAD', relief=FLAT, bd=1, text="Transfer",
                      command=trans).place(x=680, y=100)
    Minstate = Button(f11_, font=('arial', fs3, 'bold'), width=20, bg='#DDA0DD', relief=FLAT, bd=1,
                      text="Mini Statement", command=state).place(x=80, y=200)
    root.mainloop()

def ACCOUNT():
    global check4

    f()
    f1()
    f5_.place_forget()
    f12_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f12_.pack(side=LEFT, anchor=N)
    lbl1 = Label(f12_, font=('arial', fs5), text="New Account", bg='#F5F5F5')
    lbl1.place(x=100, y=5)

    X1 = 80;
    X2 = X1 + 160;
    X3 = X1 + 520;
    X4 = X1 + 720
    Y1 = 60;
    Y2 = 40;

    name = Label(f12_, font=('arial', fs4), text="Name", bg='#F5F5F5').place(x=X1, y=Y1)
    E4 = Entry(f12_, font=('arial', fs4), bg='#F5F5F5', textvariable=E_E4).place(x=X2, y=Y1)
    E_E4.set('ENTER')
    dob = Label(f12_, font=('arial', fs4), text="Date of Birth", bg='#F5F5F5').place(x=X3, y=Y1)
    E5 = Entry(f12_, font=('arial', fs4), width=10, bg='#F5F5F5', textvariable=E_E5).place(x=X4, y=Y1)
    info3 = Label(f12_, font=('arial', fs1), text="Format : DD-MM-YYYY", bg='#F5F5F5')
    info3.place(x=X4 + 150, y=Y1)
    E_E5.set('DD-MM-YYYY')

    gender = Label(f12_, font=('arial', fs4), text="Gender", bg='#F5F5F5').place(x=X1, y=Y1 + Y2)
    E6 = ttk.Combobox(f12_, font=('arial', fs4), state='readonly', textvariable=E_E6)
    E6['value'] = ('-SELECT-', 'MALE', 'FEMALE', 'OTHERS')
    E6.current(0)
    E6.place(x=X2, y=Y1 + Y2)

    fname = Label(f12_, font=('arial', fs4), text="Father's Name", bg='#F5F5F5').place(x=X3, y=Y1 + Y2)
    E7 = Entry(f12_, font=('arial', fs4), bg='#F5F5F5', textvariable=E_E7).place(x=X4, y=Y1 + Y2)
    E_E7.set('ENTER')

    address = Label(f12_, font=('arial', fs4), text="Address", bg='#F5F5F5').place(x=X1, y=Y1 + Y2 * 2 + 20)
    E8 = Entry(f12_, font=('arial', fs4), width=63, bg='#F5F5F5', textvariable=E_E8).place(x=X2, y=Y1 + Y2 * 2 + 20)
    E_E8.set('ENTER')

    idtype = Label(f12_, font=('arial', fs4), text="Id Proof type", bg='#F5F5F5').place(x=X1, y=Y1 + Y2 * 3 + 20)
    E9 = ttk.Combobox(f12_, font=('arial', fs4), state='readonly', textvariable=E_E9)
    E9['value'] = ('-SELECT-', 'Aadhar Card', 'Voter\'s Card', 'Passport', 'Driving License')
    E9.current(0)
    E9.place(x=X2, y=Y1 + Y2 * 3 + 20)

    idnum = Label(f12_, font=('arial', fs4), text="Id Proof No.", bg='#F5F5F5').place(x=X3, y=Y1 + Y2 * 3 + 20)
    E10 = Entry(f12_, font=('arial', fs4), bg='#F5F5F5', textvariable=E_E10).place(x=X4, y=Y1 + Y2 * 3 + 20)
    E_E10.set('ENTER')

    city = Label(f12_, font=('arial', fs4), text="City", bg='#F5F5F5').place(x=X1, y=Y1 + Y2 * 4 + 20)
    E11 = Entry(f12_, font=('arial', fs4), bg='#F5F5F5', textvariable=E_E11).place(x=X2, y=Y1 + Y2 * 4 + 20)
    E_E11.set('ENTER')

    pincode = Label(f12_, font=('arial', fs4), text="Pincode", bg='#F5F5F5').place(x=X3, y=Y1 + Y2 * 4 + 20)
    E12 = Entry(f12_, font=('arial', fs4), bg='#F5F5F5', textvariable=E_E12).place(x=X4, y=Y1 + Y2 * 4 + 20)
    E_E12.set('ENTER')

    state = Label(f12_, font=('arial', fs4), text="State", bg='#F5F5F5').place(x=X1, y=Y1 + Y2 * 5 + 20)
    E13 = Entry(f12_, font=('arial', fs4), bg='#F5F5F5', textvariable=E_E13).place(x=X2, y=Y1 + Y2 * 5 + 20)
    E_E13.set('ENTER')

    mobno = Label(f12_, font=('arial', fs4), text="Mobile No.", bg='#F5F5F5').place(x=X3, y=Y1 + Y2 * 5 + 20)
    E14 = Entry(f12_, font=('arial', fs4), bg='#F5F5F5', textvariable=E_E14).place(x=X4, y=Y1 + Y2 * 5 + 20)
    E_E14.set('ENTER')

    email = Label(f12_, font=('arial', fs4), text="Email", bg='#F5F5F5').place(x=X1, y=Y1 + Y2 * 6 + 20)
    E15 = Entry(f12_, font=('arial', fs4), width=40, bg='#F5F5F5', textvariable=E_E15).place(x=X2, y=Y1 + Y2 * 6 + 20)
    E_E15.set('ENTER')

    acctype = Label(f12_, font=('arial', fs4), text="Account Type", bg='#F5F5F5').place(x=X1, y=Y1 + Y2 * 7 + 20)
    E16 = ttk.Combobox(f12_, font=('arial', fs4), state='readonly', textvariable=E_E16)
    E16['value'] = ('-SELECT-', 'SAVINGS ACCOUNT', 'CURRENT ACCOUNT')
    E16.current(0)
    E16.place(x=X2, y=Y1 + Y2 * 7 + 20)

    info6 = Label(f12_, font=('arial', fs3),
                  text="Please check twice your details before submission. Any wrong will result not opening of the bank account.",
                  bg='#F5F5F5')
    info6.place(x=170, y=Y1 + Y2 * 8 + 60)

    Submit = Button(f12_, font=('arial', fs4, 'bold'), text="SUBMIT", command=U_reg).place(x=X3 + 10, y=Y1 + Y2 * 11)
    root.mainloop()

def U_reg():
    global E_E4, E_E5, E_E6, E_E7, E_E8, E_E9, E_E10, E_E11, E_E12, E_E13, E_E14, E_E15, E_E16, check3, list2, list3, list4, check4, check5, mydbvar1
    f()
    f1()
    f5_.place_forget()

    mydb_ = mcon.connect(host='localhost', user='root', database='ACCOUNT_NUMBER', passwd='1234')
    _cursor = mydb_.cursor()

    Name = E_E4.get()
    DOB = E_E5.get()
    Gender = E_E6.get()
    Fname = E_E7.get()
    Adress = E_E8.get()
    IDtype = E_E9.get()

    IDnum = E_E10.get()
    City = E_E11.get()
    Pincode = E_E12.get()
    State = E_E13.get()
    Mobno = E_E14.get()
    Email = E_E15.get()
    Acctype = E_E16.get()

    try:
        _cursor.execute("CREATE TABLE ACCOUNT_NUMBER (Accno int, Name varchar(30),DOB char(10),Gender varchar(6),Fname varchar(30),\
                        Adress varchar(200), IDtype varchar(25),IDnum varchar (16),City varchar(20),Pincode char(6),State varchar(20),\
                        Mobno char(10),Email varchar(50),Acctype varchar(30))")
    except:
        pass
    _cursor.execute('SELECT * from ACCOUNT_NUMBER')

    for i in _cursor:
        try:
            list2.append(i[0])
        except:
            pass
    if len(list2) == 0:
        _cursor.execute("INSERT INTO ACCOUNT_NUMBER(Accno, Name, DOB, Gender, Fname, Adress, IDtype, IDnum, City, Pincode,\
    			State, Mobno, Email, Acctype) VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}','{}',\
    			'{}','{}','{}','{}')".format(0, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'))
        mydb_.commit()

    Accnobase = 100100000

    _cursor.execute("SELECT Accno from ACCOUNT_NUMBER")
    for i in _cursor:
        list3.append(i[0])
    if int(list3[-1]) == 0:
        Accno = Accnobase + 1
    else:
        Accno = int(list3[-1]) + 1

    try:
        _cursor.execute("INSERT INTO ACCOUNT_NUMBER(Accno, Name, DOB, Gender, Fname, Adress, IDtype, IDnum, City, Pincode,\
    			State, Mobno, Email, Acctype) VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}','{}',\
    			'{}','{}','{}','{}')".format(Accno, Name, DOB, Gender, Fname, Adress, IDtype, IDnum, City, Pincode,
                                             State, Mobno, Email, Acctype))
        mydb_.commit()
        check5 = 1
    except:
        ACCOUNT()
    mydb_.close()
    if Acctype == 'SAVINGS ACCOUNT':
        mydbvar1 = 'SAVINGS'
    elif Acctype == 'CURRENT ACCOUNT':
        mydbvar1 = 'CURRENT'
    mydb2 = mcon.connect(host='localhost', user='root', database=mydbvar1, passwd='1234')
    cursor2 = mydb2.cursor()
    st = '_' + str(Accno)
    print(Name, '...............', Accno)
    st1 = "CREATE TABLE " + st + "(Narration varchar(15), Date char(10) ,Debit int, Credit int, Balance int)"
    cursor2.execute(st1)
    mydb2.close()
    if check5 == 1:
        out()
        check5 = 0
    root.mainloop()

def out():
    f()
    f1()
    f5_.place_forget()
    out3 = Label(root, font=('arial', 25), text="YOU HAVE SUCCESFULLY CREATED YOUR ACCOUNT", bg='#F5F5F5').place(x=220,
                                                                                                                 y=200)
    out4 = Label(root, font=('arial', fs4), text="THANK YOU FOR USING OUR BANKING SERVICE", bg='#F5F5F5').place(x=345,
                                                                                                                y=300)
    root.mainloop()

def logout():
    global check2
    check2 = 0
    f()
    f1()
    f5_.place_forget()
    f13_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f13_.pack(side=LEFT, anchor=N)

    out1 = Label(f13_, font=('arial', 25), text="YOU HAVE SUCCESFULLY LOGGED OUT", bg='#F5F5F5').place(x=300, y=200)
    out2 = Label(f13_, font=('arial', fs4), text="THANK YOU FOR USING OUR BANKING SERVICE", bg='#F5F5F5').place(x=345,
                                                                                                                y=300)
    root.mainloop()

def depdraw():
    global chdepdraw, check6
    f()
    f1()
    f5_.place_forget()
    X5 = 100;
    X6 = X5 + 400;
    X7 = 10;
    X8 = 180
    Y3 = 100;
    Y4 = Y3 + 40;
    Y5 = 20;
    Y6 = Y5 + 60

    f14_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f14_.pack(side=LEFT, anchor=N)

    lbl2 = Label(f14_, font=('arial', fs5), text="WHAT DO YOU WANT TO DO", bg='#F5F5F5')
    lbl2.place(x=20, y=20)

    R1 = Radiobutton(f14_, font=('arial', fs5), text="DEPOSIT", variable=radio1, value=1, bg='#F5F5F5', command=depdraw)
    R1.place(x=X5, y=Y3)
    R2 = Radiobutton(f14_, font=('arial', fs5), text="WITHDRAW", variable=radio1, value=2, bg='#F5F5F5',
                     command=depdraw)
    R2.place(x=X6, y=Y3)

    f15_ = Frame(f14_, width=400, height=250, bd=1, bg='#F5F5F5', relief=RIDGE)
    f15_.place(x=X5, y=Y4 + 2)
    f16_ = Frame(f14_, width=400, height=250, bd=1, bg='#F5F5F5', relief=RIDGE)
    f16_.place(x=X6, y=Y4 + 2)

    label1 = Label(f15_, font=('arial', fs4), text="Account No.", bg='#F5F5F5').place(x=10, y=Y5)
    E17 = Entry(f15_, font=('arial', fs4), width=15, bg='#F5F5F5', textvariable=E_E17, state=DISABLED)
    E17.place(x=X8, y=Y5)
    E_E17.set(0)
    label2 = Label(f15_, font=('arial', fs4), text="Amount", bg='#F5F5F5').place(x=10, y=Y6)
    E18 = Entry(f15_, font=('arial', fs4), width=15, bg='#F5F5F5', textvariable=E_E18, state=DISABLED)
    E18.place(x=X8, y=Y6)
    E_E18.set(0)
    label3 = Label(f16_, font=('arial', fs4), text="Account No.", bg='#F5F5F5').place(x=10, y=Y5)
    E19 = Entry(f16_, font=('arial', fs4), width=15, bg='#F5F5F5', textvariable=E_E19, state=DISABLED)
    E19.place(x=X8, y=Y5)
    E_E19.set(0)
    label4 = Label(f16_, font=('arial', fs4), text="Amount", bg='#F5F5F5').place(x=10, y=Y6)
    E20 = Entry(f16_, font=('arial', fs4), width=15, bg='#F5F5F5', textvariable=E_E20, state=DISABLED)
    E20.place(x=X8, y=Y6)
    E_E20.set(0)
    if radio1.get() == 1:
        E17.configure(state=NORMAL)
        E18.configure(state=NORMAL)
        E19.configure(state=DISABLED)
        E20.configure(state=DISABLED)
        chdepdraw = 1
    elif radio1.get() == 2:
        E19.configure(state=NORMAL)
        E20.configure(state=NORMAL)
        E17.configure(state=DISABLED)
        E18.configure(state=DISABLED)
        chdepdraw = 2

    Submit = Button(f14_, font=('arial', fs4, 'bold'), text="SUBMIT", command=depdrawsub).place(x=450, y=400)
    root.mainloop()

def depdrawsub():
    global chdepdraw, E_E17, E_E18, E_E19, E_E20, balance, date, currentDay, currentMonth, currentYear, mydbvar2, list5
    f()
    f1()
    f5_.place_forget()
    f20_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f20_.pack(side=LEFT, anchor=N)

    if chdepdraw == 1:
        Accno = E_E17.get()
        Accno1 = '_' + str(Accno)
        Amount = E_E18.get()
        narration = 'Deposit'
    elif chdepdraw == 2:
        Accno = E_E19.get()
        Accno1 = '_' + str(Accno)
        Amount = E_E20.get()
        narration = 'Withdraw'

    mydb3 = mcon.connect(host='localhost', user='root', database='ACCOUNT_NUMBER', passwd='1234')
    cursor3 = mydb3.cursor()
    cursor3.execute("select Acctype from ACCOUNT_NUMBER where Accno={}".format(Accno))

    for i in cursor3:
        if i[0] == "SAVINGS ACCOUNT":
            mydbvar2 = 'SAVINGS'
        elif i[0] == "CURRENT ACCOUNT":
            mydbvar2 = 'CURRENT'
    mydb3.close()
    mydb4 = mcon.connect(host='localhost', user='root', database=mydbvar2, passwd='1234')
    cursor4 = mydb4.cursor()

    cursor4.execute("select Balance from " + Accno1)
    for i in cursor4:
        try:
            list5.append(i[0])
        except:
            pass
    date_()

    if len(list5) == 0:
        if narration == 'Withdraw':
            depdraw()
        elif narration == 'Deposit':
            cursor4.execute(
                "INSERT INTO " + Accno1 + "(Narration, Date,Debit, Credit, Balance) VALUES('{}','{}',{},{},{})".format(
                    narration, date, 0, Amount, Amount))
            mydb4.commit()
            check6 = 1
    else:
        if narration == 'Withdraw':
            balance = list5[-1]
            balance -= Amount
            if balance >= 0:
                cursor4.execute(
                    "INSERT INTO " + Accno1 + "(Narration, Date,Debit, Credit, Balance) VALUES('{}','{}',{},{},{})".format(
                        narration, date, Amount, 0, balance))
                mydb4.commit()
                check6 = 1
            else:
                depdraw()
        elif narration == 'Deposit':
            balance = list5[-1]
            balance += Amount
            cursor4.execute(
                "INSERT INTO " + Accno1 + "(Narration, Date,Debit, Credit, Balance) VALUES('{}','{}',{},{},{})".format(
                    narration, date, 0, Amount, balance))
            mydb4.commit()
            check6 = 1
    mydb4.close()
    try:
        if check6 == 1:
            out5 = Label(f20_, font=('arial', 25), text="YOU HAVE SUCCESFULLY DONE THE TRANSACTION",
                         bg='#F5F5F5').place(x=215, y=200)
            out6 = Label(f20_, font=('arial', fs4), text="THANK YOU FOR USING OUR BANKING SERVICE", bg='#F5F5F5').place(
                x=345, y=300)
    except:
        pass
    root.mainloop()

def trans():
    f()
    f1()
    f5_.place_forget()
    X9 = 10;
    X10 = 350;
    Y7 = 20;

    f17_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f17_.pack(side=LEFT, anchor=N)
    f17A_ = Frame(f17_, width=600, height=250, bd=1, bg='#F5F5F5', relief=RIDGE)
    f17A_.place(x=100, y=140)
    label5 = Label(f17_, font=('arial', fs5), text="TRANSFER", bg='#F5F5F5').place(x=100, y=20)

    label6 = Label(f17A_, font=('arial', fs4), text="Transfer from Account No.", bg='#F5F5F5').place(x=X9, y=Y7)
    E21 = Entry(f17A_, font=('arial', fs4), width=15, bg='#F5F5F5', textvariable=E_E21)
    E21.place(x=X10, y=Y7)
    E_E21.set('ENTER')

    label7 = Label(f17A_, font=('arial', fs4), text="Amount to be transfered", bg='#F5F5F5').place(x=X9, y=Y7 + 60)
    E22 = Entry(f17A_, font=('arial', fs4), width=15, bg='#F5F5F5', textvariable=E_E22)
    E22.place(x=X10, y=Y7 + 60)
    E_E22.set(0)

    label8 = Label(f17A_, font=('arial', fs4), text="Transfer to Account No.", bg='#F5F5F5').place(x=X9, y=Y7 + 60 * 2)
    E23 = Entry(f17A_, font=('arial', fs4), width=15, bg='#F5F5F5', textvariable=E_E23)
    E23.place(x=X10, y=Y7 + 60 * 2)
    E_E23.set('ENTER')
    Submit = Button(f17_, font=('arial', fs4, 'bold'), text="SUBMIT", command=transub).place(x=250, y=400)
    root.mainloop()

def transub():
    global E_E21, E_E22, E_E23, balance, date, currentDay, currentMonth, currentYear, list6, mydbvar3, mydbvar4, list7, balance1, balance2, check7
    f()
    f1()
    f5_.place_forget()
    f21_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f21_.pack(side=LEFT, anchor=N)

    Accno2 = E_E21.get()
    Accno2_ = '_' + str(Accno2)
    Amount1 = E_E22.get()
    Accno3 = E_E23.get()
    Accno3_ = '_' + str(Accno3)

    mydb5 = mcon.connect(host='localhost', user='root', database='ACCOUNT_NUMBER', passwd='1234')
    cursor5 = mydb5.cursor()
    cursor5.execute("select Acctype from ACCOUNT_NUMBER where Accno={}".format(Accno2))
    for i in cursor5:
        if i[0] == "SAVINGS ACCOUNT":
            mydbvar3 = 'SAVINGS'
        elif i[0] == "CURRENT ACCOUNT":
            mydbvar3 = 'CURRENT'
    mydb5.close()

    mydb6 = mcon.connect(host='localhost', user='root', database=mydbvar3, passwd='1234')
    cursor6 = mydb6.cursor()
    cursor6.execute("select Balance from " + Accno2_)
    for i in cursor6:
        try:
            list6.append(i[0])
        except:
            pass
    date_()
    if len(list6) == 0:
        trans()
    else:
        balance1 = list6[-1] - Amount1
        if balance1 >= 0:
            cursor6.execute(
                "INSERT INTO " + Accno2_ + "(narration, Date,Debit, Credit, Balance) VALUES('{}','{}',{},{},{})".format(
                    'Transfer', date, Amount1, 0, balance1))
            mydb6.commit()
        else:
            trans()
    mydb6.close()

    mydb7 = mcon.connect(host='localhost', user='root', database='ACCOUNT_NUMBER', passwd='1234')
    cursor7 = mydb7.cursor()
    cursor7.execute("select Acctype from ACCOUNT_NUMBER where Accno={}".format(Accno3))
    for i in cursor7:
        if i[0] == "SAVINGS ACCOUNT":
            mydbvar4 = 'SAVINGS'
        elif i[0] == "CURRENT ACCOUNT":
            mydbvar4 = 'CURRENT'
    mydb7.close()

    mydb8 = mcon.connect(host='localhost', user='root', database=mydbvar4, passwd='1234')
    cursor8 = mydb8.cursor()
    cursor8.execute("select Balance from " + Accno3_)
    for i in cursor8:
        try:
            list7.append(i[0])
        except:
            pass
    balance2 = list7[-1] + Amount1
    cursor8.execute(
        "INSERT INTO " + Accno3_ + "(narration, Date,Debit, Credit, Balance) VALUES('{}','{}',{},{},{})".format(
            'Transfer', date, 0, Amount1, balance2))
    mydb8.commit()
    mydb8.close()
    out7 = Label(f21_, font=('arial', 25), text="YOU HAVE SUCCESFULLY DONE THE TRANSACTION", bg='#F5F5F5').place(x=215,
                                                                                                                 y=200)
    out8 = Label(f21_, font=('arial', fs4), text="THANK YOU FOR USING OUR BANKING SERVICE", bg='#F5F5F5').place(x=345,
                                                                                                                y=300)
    root.mainloop()

def state():
    global LLIST, LDICT, BD
    f()
    f1()
    f5_.place_forget()
    X11 = 20;
    Y8 = 140;
    Y9 = 40;
    X12 = 200;
    X13 = 100

    f18_ = Frame(root, width=1360, height=603, bd=1, bg='#F5F5F5', relief=RIDGE)
    f18_.pack(side=LEFT, anchor=N)
    label9 = Label(f18_, font=('arial', fs5), text="MINI-STATEMENT", bg='#F5F5F5').place(x=100, y=20)

    label10 = Label(f18_, font=('arial', fs3), text="Account No.", bg='#F5F5F5').place(x=100, y=60)
    E24 = Entry(f18_, font=('arial', fs3), width=15, bg='#F5F5F5', textvariable=E_E24)
    E24.place(x=400, y=60)
    E_E24.set(0)

    LAB1_ = Label(f18_, font=('arial', fs3), width=5, text="S.No.", bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 - Y9)
    LAB2_ = Label(f18_, font=('arial', fs3), width=9, text="Narration", bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + +X12, y=Y8 - Y9)
    LAB3_ = Label(f18_, font=('arial', fs3), width=6, text="Date", bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + +X12 * 2, y=Y8 - Y9)
    LAB4_ = Label(f18_, font=('arial', fs3), width=6, text="Debit", bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + +X12 * 3, y=Y8 - Y9)
    LAB5_ = Label(f18_, font=('arial', fs3), width=6, text="Credit", bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + +X12 * 4, y=Y8 - Y9)
    LAB6_ = Label(f18_, font=('arial', fs3), width=10, text="Balnce", bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + +X12 * 5, y=Y8 - Y9)

    lab1 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[1], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8)
    lab2 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[2], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8)
    lab3 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[3], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8)
    lab4 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[4], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8)
    lab5 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[5], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8)
    lab6 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[6], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8)

    lab7 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[7], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9)
    lab8 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[8], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9)
    lab9 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[9], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9)
    lab10 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[10], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9)
    lab11 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[11], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9)
    lab12 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[12], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9)

    lab13 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[13], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 2)
    lab14 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[14], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 2)
    lab15 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[15], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 2)
    lab16 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[16], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 2)
    lab17 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[17], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 2)
    lab18 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[18], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 2)

    lab19 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[19], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 3)
    lab20 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[20], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 3)
    lab21 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[21], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 3)
    lab22 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[22], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 3)
    lab23 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[23], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 3)
    lab24 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[24], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 3)

    lab25 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[25], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 4)
    lab26 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[26], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 4)
    lab27 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[27], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 4)
    lab28 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[28], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 4)
    lab29 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[29], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 4)
    lab30 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[30], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 4)

    lab31 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[31], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 5)
    lab32 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[32], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 5)
    lab33 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[33], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 5)
    lab34 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[34], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 5)
    lab35 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[35], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 5)
    lab36 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[36], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 5)

    lab37 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[37], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 6)
    lab38 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[38], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 6)
    lab39 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[39], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 6)
    lab40 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[40], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 6)
    lab41 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[41], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 6)
    lab42 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[42], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 6)

    lab43 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[43], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 7)
    lab44 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[44], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 7)
    lab45 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[45], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 7)
    lab46 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[46], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 7)
    lab47 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[47], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 7)
    lab48 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[48], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 7)

    lab49 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[49], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 8)
    lab50 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[50], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 8)
    lab51 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[51], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 8)
    lab52 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[52], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 8)
    lab53 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[53], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 8)
    lab54 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[54], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 8)

    lab55 = Label(f18_, font=('arial', fs3), width=5, text=LDICT[55], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X13, y=Y8 + Y9 * 9)
    lab56 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[56], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12, y=Y8 + Y9 * 9)
    lab57 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[57], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 2, y=Y8 + Y9 * 9)
    lab58 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[58], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 3, y=Y8 + Y9 * 9)
    lab59 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[59], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 4, y=Y8 + Y9 * 9)
    lab60 = Label(f18_, font=('arial', fs3), width=15, text=LDICT[60], bg='#F5F5F5', bd=BD, relief=RIDGE).place(
        x=X11 + X12 * 5, y=Y8 + Y9 * 9)

    Submit = Button(f18_, font=('arial', fs3, 'bold'), text="SUBMIT", command=statesub).place(x=600, y=50)
    root.mainloop()

def statesub():
    global LLIST, LDICT, mydbvar5, LDvar, length
    LDICT = {1: None, 2: None, 3: None, 4: None, 5: None,
             6: None, 7: None, 8: None, 9: None, 10: None,
             11: None, 12: None, 13: None, 14: None, 15: None,
             16: None, 17: None, 18: None, 19: None, 20: None,
             21: None, 22: None, 23: None, 24: None, 25: None,
             26: None, 27: None, 28: None, 29: None, 30: None,
             31: None, 32: None, 33: None, 34: None, 35: None,
             36: None, 37: None, 38: None, 39: None, 40: None,
             41: None, 42: None, 43: None, 44: None, 45: None,
             46: None, 47: None, 48: None, 49: None, 50: None,
             51: None, 52: None, 53: None, 54: None, 55: None,
             56: None, 57: None, 58: None, 59: None, 60: None}
    LDvar = 1
    LLIST = []
    Accno4 = E_E24.get()
    Accno4_ = '_' + str(Accno4)
    mydb9 = mcon.connect(host='localhost', user='root', database='ACCOUNT_NUMBER', passwd='1234')
    cursor9 = mydb9.cursor()
    cursor9.execute("select Acctype from ACCOUNT_NUMBER where Accno={}".format(Accno4))
    for i in cursor9:
        if i[0] == "SAVINGS ACCOUNT":
            mydbvar5 = 'SAVINGS'
        elif i[0] == "CURRENT ACCOUNT":
            mydbvar5 = 'CURRENT'
    mydb9.close()

    mydb10 = mcon.connect(host='localhost', user='root', database=mydbvar5, passwd='1234')
    cursor10 = mydb10.cursor()
    cursor10.execute("select * from " + Accno4_)

    for i in cursor10:
        LLIST.insert(0, i)

    length = len(LLIST)

    for i in range(1, 11, 1):
        for j in range(6):
            if j == 0 and i <= length:
                LDICT[LDvar] = i
            else:
                try:
                    LDICT[LDvar] = LLIST[i - 1][j - 1]
                except:
                    LDICT[LDvar] = None
            LDvar += 1
    state()

def date_():
    global date, currentDay, currentMonth, currentYear
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    date = str(currentDay) + '-' + str(currentMonth) + '-' + str(currentYear)

def main():
    f1()
    fHome()

main()

print(len(globals()))
print(len(locals()))