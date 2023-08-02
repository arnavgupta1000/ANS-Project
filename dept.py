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

mycursor.execute("USE FM")

#___________________________________________________________________________________________________________________________________

# department Screen
def dept_sql():

    mycursor.execute("Select * from department")

    records = mycursor.fetchall()

    return records

def dept():

    

    global dept_screen



    dept_scrn = Tk()

    dept_scrn.title("Department")

    dept_scrn.attributes("-fullscreen",True)

    dept_scrn.configure(bg = "Black")

    

    Label(dept_scrn,text = "Department",fg = "#F7761B",bg = "black",font=("Old English Text MT",30),pady = 2,padx = 80).place(x=530,y=30)



    records = dept_sql()



    data = [('Dname','Dnumber')]

    data.extend(records)



    rows = len(data)

    columns = 2



    dept_frm = Frame(dept_scrn,bg="black")

    dept_cnvs = Canvas(dept_frm,height = 500,width = 976,bg="black")

    scroll_y = Scrollbar(dept_frm, orient="vertical", command=dept_cnvs.yview)

    dept_frm1 = Frame(dept_cnvs)

    

    dept_frm1.place(x = 250,y = 100)



    for i in range(rows):

        for j in range(columns):

            if i==0:

                l = Label(dept_frm1,text=data[i][j],bg = "black",fg = "#F7761B",padx=15,pady=3)

                l.configure(font =("Algerian",20))

                l.grid(row=i,column=j,sticky="nsew",padx = 1,pady=1)

            else:

                l = Label(dept_frm1,text=data[i][j],bg = "#F7761B",padx=3,pady=3)

                l.grid(row=i,column=j,sticky="nsew",padx = 1,pady=1)



    dept_cnvs.create_window(1000, 1000, anchor='nw', window=dept_frm1)

    dept_cnvs.update_idletasks()



    dept_cnvs.configure(scrollregion=dept_cnvs.bbox('all'),yscrollcommand=scroll_y.set)



    dept_cnvs.pack(fill='both', expand=True, side='left')

    scroll_y.pack(fill='y', side='right')



    dept_frm.place(x =180,y=100)



    dept_frm2 = Frame(dept_scrn,bg="Black", padx = 25, pady= 10)

    Button(dept_frm2,text="Add Worker",command = adddept,bg="#F7761B",padx = 120,pady=10).grid(row = 1,column = 1,padx=10,pady=10)

    Button(dept_frm2,text="Remove Worker",command=rmvdept,bg="#F7761B",padx=110,pady=10).grid(row = 1,column = 2)

    Button(dept_frm2,text="Edit Worker",command=editdept,bg="#F7761B",padx=121,pady=10).grid(row = 2,column = 1)

    Button(dept_frm2,text="Return",command=dept_scrn.destroy, bg="#F7761B",padx = 135,pady=10).grid(row = 2,column = 2)

    dept_frm2.place(x = 330,y = 615)



    dept_scrn.mainloop()
