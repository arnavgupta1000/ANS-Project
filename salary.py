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

# Salary Screen



def do():

    d.destroy()



    for i in range(noOfRec):

        if records[i][0] in present:

            string = "SELECT Salary FROM wrkr WHERE emp_idd = %s"%(records[i][0])

            mycursor.execute(string)

            salary = mycursor.fetchone()

            records[i][2]+=1

            records[i][-1]+=(salary[0]//30)

        else:

            records[i][3]+=1

    fileput(records)



    slry_scrn.destroy()

    slry()



def done():

    global d

    d = Tk()

    d.configure(bg="black")

    Button(d,text = "done",command = do,bg="#F7761B",fg="black").pack()



def p():

    present.append(adhaar)

    tndnce_scrn.destroy()

    indtndnce(num+1)



def ab():

    tndnce_scrn.destroy()

    indtndnce(num+1)



def indtndnce(i):

    if i>=noOfRec:

        done()

        return 0

    global name, adhaar,tndnce_scrn, num

    num = i

    name = records[i][1]

    adhaar = records[i][0]

    tndnce_scrn = Tk()

    tndnce_scrn.configure(bg="black")

    t = "Is %s there ?\nAdhar Number - %s"%(name,adhaar)

    Label(tndnce_scrn,text = t,bg = "black",fg = "#F7761B").pack()



    Button(tndnce_scrn,text = "Present", command = p,bg = "#F7761B",fg="black").pack()

    Button(tndnce_scrn,text = "Absent",command = ab,bg = "#F7761B",fg = "black").pack()



def mrktndnce():

    global present, noOfRec, records

    present = []

    records = fileget()

    noOfRec = len(records)

    indtndnce(0)



def vrtmDone():

    adhaarNumber = int(adhaar.get())

    noOfHr = int(noh.get())



    string = "SELECT Salary FROM wrkr WHERE emp_idd = %s"%(adhaarNumber)

    mycursor.execute(string)

    salary = mycursor.fetchone()

    salary = salary[0]//(30*24)



    vrtm_scrn.destroy()



    records = fileget()

    for i in range(len(records)):

        if records[i][0] == adhaarNumber:

            records[i][-2]+=noOfHr

            records[i][-1]+=(noOfHr*salary)

    

    fileput(records)



    slry_scrn.destroy()

    slry()



def vrtm():

    global vrtm_scrn, adhaar, noh

    vrtm_scrn = Tk()

    vrtm_scrn.title("Overtime")

    vrtm_scrn.configure(bg="black")

    vrtmFrame = Frame(vrtm_scrn,bg="black")



    Label(vrtmFrame,text="Enter Emp_ID: ",bg="black",fg="#F7761B").pack()

    adhaar = Entry(vrtmFrame, width=50,borderwidth=5,bg="black",fg="#F7761B")

    adhaar.pack(pady = 5,padx=10)



    Label(vrtmFrame,text="Enter Number of hours: ",bg="black",fg='#F7761B').pack()

    noh  = Entry(vrtmFrame, width=50,borderwidth=5,bg="black",fg="#F7761B")

    noh.pack(pady = 5,padx=10)

    

    Button(vrtmFrame,text="Done",command = vrtmDone,bg="#F7761B",fg="black").pack()



    vrtmFrame.pack()



def zrattndnce():

    records = fileget()

    noOfRec = len(records)

    for i in range(noOfRec):

        records[i][2],records[i][3],records[i][4],records[i][5]=0,0,0,0

    fileput(records)



    slry_scrn.destroy()

    slry()



def slry():

    global slry_scrn

    slry_scrn = Tk()

    slry_scrn.title("Salary")

    slry_scrn.attributes("-fullscreen",True)

    slry_scrn.configure(bg="black")



    Label(slry_scrn,text = "Salary",fg = "#F7761B",bg = "black",font=("Old English Text MT",30),pady = 2,padx = 80).place(x=545,y=30)

    

    records = fileget()



    data = [('EMPID','Workers','Attendance','Holidays','overtime','Salary')]

    data.extend(records)



    rows = len(data)

    columns = 6



    slry_frm = Frame(slry_scrn, bg="black")

    slry_cnvs = Canvas(slry_frm,height = 500,width = 1025,bg="black")

    scroll_y = Scrollbar(slry_frm, orient="vertical", command=slry_cnvs.yview)

    slry_frm1 = Frame(slry_cnvs)

    

    slry_frm1.place(x = 250,y = 100)



    for i in range(rows):

        for j in range(columns):

            if i==0:

                l = Label(slry_frm1,text=data[i][j],bg="black",fg = "#F7761B",padx=10,pady=3)

                l.configure(font = ("Algerian",20))

                l.grid(row=i,column=j,sticky="nsew",padx = 1,pady=1)

            else:

                l = Label(slry_frm1,text=data[i][j],bg="#F7761B",fg="black",padx=3,pady=3)

                l.grid(row=i,column=j,sticky="nsew",padx = 1,pady=1)



    slry_cnvs.create_window(1000, 1000, anchor='nw', window=slry_frm1)

    slry_cnvs.update_idletasks()



    slry_cnvs.configure(scrollregion=slry_cnvs.bbox('all'),yscrollcommand=scroll_y.set)



    slry_cnvs.pack(fill='both', expand=True, side='left')

    scroll_y.pack(fill='y', side='right')



    slry_frm.place(x = 175,y=100)



    slry_frm2 = Frame(slry_scrn,bg = "black")

    Button(slry_frm2,text="Mark Attendance",command = mrktndnce,bg="#F7761B",fg="black",padx = 102,pady=10).grid(row = 1,column = 1,padx=10,pady=10)

    Button(slry_frm2,text="Overtime",command = vrtm,bg="#F7761B",fg="black",padx = 116,pady=10).grid(row = 1,column = 2)

    Button(slry_frm2,text="Give Salary",command = zrattndnce,bg="#F7761B",fg="black",padx = 119,pady=10).grid(row = 2,column = 1)

    Button(slry_frm2,text="Return",command = slry_scrn.destroy,bg="#F7761B",fg="black",padx=122,pady=10).grid(row = 2,column = 2)

    slry_frm2.place(x = 375,y = 615)



    slry_scrn.mainloop()



