from tkinter import Tk, Label, Frame, Button, Entry, Canvas, Scrollbar, BOTTOM


from PIL import ImageTk, Image

import mysql.connector as mysql

from datetime import date

mydb = mysql.connect(

    host = "localhost",

    username = 'root',

    password = 'vishu1812'

    )

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

databases = mycursor.fetchall()

mycursor.execute("USE NSASystems")


#___________________________________________________________________________________________________________________________________

# Add Worker



global wrkr_scrn, addwrkr_scrn, rmvwrkr_scrn, editwrkr_scrn



def wrkr_sql():

    mycursor.execute("Select * from wrkr ORDER BY Salary DESC")

    records = mycursor.fetchall()

    return records



def add():

    Id = emp_idd.get()

    wrkrName = name.get()

    desc = designation.get()

    slry = salary.get()

    gndr=gender.get()

    addrs=Address.get()

    Id = int(Id)

    slry = int(slry)



    s = "INSERT INTO wrkr VALUES(%s,%s,%s,%s,%s,%s,%s)"

    val = [(Id,wrkrName,desc,slry,date.today(),gndr,addrs)]



    mycursor.executemany(s,val)

    mydb.commit()



    fileadd(Id,wrkrName)



    addwrkr_scrn.destroy()

    wrkr_scrn.destroy()

    wrkr()



def addwrkr():

    global addwrkr_scrn



    addwrkr_scrn = Tk()

    addwrkr_scrn.title("Add Worker")



    global emp_idd,name,designation,salary,startDate,gender,Address



    info = Frame(addwrkr_scrn,bg = "black")

    Label(info, text = "Enter Emp_ID:",bg="Black",fg="#F7761B").pack()

    emp_idd = Entry(info,width=50,borderwidth=5,bg="Black",fg="#F7761B")

    emp_idd.pack()



    Label(info, text = "Enter Name:",bg="Black",fg="#F7761B").pack()

    name = Entry(info,width=50,borderwidth=5,bg="Black",fg="#F7761B")

    name.pack()



    Label(info, text = "Enter Designation:",bg="Black",fg="#F7761B").pack()

    designation = Entry(info,width=50,borderwidth=5,bg="Black",fg="#F7761B")

    designation.pack()



    Label(info, text = "Enter Salary:",bg="Black",fg="#F7761B").pack()

    salary = Entry(info,width=50,borderwidth=5,bg="Black",fg="#F7761B")

    salary.pack()

    Label(info, text = "Enter Gender:",bg="Black",fg="#F7761B").pack()

    gender = Entry(info,width=50,borderwidth=5,bg="Black",fg="#F7761B")

    gender.pack()

    Label(info, text = "Enter Address:",bg="Black",fg="#F7761B").pack()

    Address = Entry(info,width=50,borderwidth=5,bg="Black",fg="#F7761B")

    Address.pack()



    Button(info, text = "Add", command=add,fg="Black",bg="#F7761B").pack()

    info.pack()


#___________________________________________________________________________________________________________________________________

# Worker Screen



def wrkr():



    global wrkr_scrn



    wrkr_scrn = Tk()

    wrkr_scrn.title("Workers")

    wrkr_scrn.attributes("-fullscreen",True)

    wrkr_scrn.configure(bg = "Black")

    

    Label(wrkr_scrn,text = "Workers",fg = "#F7761B",bg = "black",font=("Old English Text MT",30),pady = 2,padx = 80).place(x=530,y=30)



    records = wrkr_sql()



    data = [('EMPID','Workers','Description','Salary','Starting Date','Gender','Address')]

    data.extend(records)



    rows = len(data)

    columns = 7



    wrkr_frm = Frame(wrkr_scrn,bg="black")

    wrkr_cnvs = Canvas(wrkr_frm,height = 500,width = 976,bg="black")

    scroll_y = Scrollbar(wrkr_frm, orient="vertical", command=wrkr_cnvs.yview)

    wrkr_frm1 = Frame(wrkr_cnvs)

    

    wrkr_frm1.place(x = 250,y = 100)



    for i in range(rows):

        for j in range(columns):

            if i==0:

                l = Label(wrkr_frm1,text=data[i][j],bg = "black",fg = "#F7761B",padx=15,pady=3)

                l.configure(font =("Algerian",20))

                l.grid(row=i,column=j,sticky="nsew",padx = 1,pady=1)

            else:

                l = Label(wrkr_frm1,text=data[i][j],bg = "#F7761B",padx=3,pady=3)

                l.grid(row=i,column=j,sticky="nsew",padx = 1,pady=1)



    wrkr_cnvs.create_window(1000, 1000, anchor='nw', window=wrkr_frm1)

    wrkr_cnvs.update_idletasks()



    wrkr_cnvs.configure(scrollregion=wrkr_cnvs.bbox('all'),yscrollcommand=scroll_y.set)



    wrkr_cnvs.pack(fill='both', expand=True, side='left')

    scroll_y.pack(fill='y', side='right')



    wrkr_frm.place(x =180,y=100)



    wrkr_frm2 = Frame(wrkr_scrn,bg="Black", padx = 25, pady= 10)

    Button(wrkr_frm2,text="Add Worker",command = addwrkr,bg="#F7761B",padx = 120,pady=10).grid(row = 1,column = 1,padx=10,pady=10)

    Button(wrkr_frm2,text="Remove Worker",command=rmvwrkr,bg="#F7761B",padx=110,pady=10).grid(row = 1,column = 2)

    Button(wrkr_frm2,text="Edit Worker",command=editwrkr,bg="#F7761B",padx=121,pady=10).grid(row = 2,column = 1)

    Button(wrkr_frm2,text="Return",command=wrkr_scrn.destroy, bg="#F7761B",padx = 135,pady=10).grid(row = 2,column = 2)

    wrkr_frm2.place(x = 330,y = 615)



    wrkr_scrn.mainloop()
