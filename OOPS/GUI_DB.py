import tkinter as tk
from tkinter import messagebox
import sqlite3
root=tk.Tk()
root.title("Insert Data")
conn=sqlite3.connect("mydb.db")
cur=conn.cursor()

def insertData():
    name=txtName.get()
    age=txtAge.get()
    c=cur.execute("insert into person1(name,age) values (?,?)",(name,age))
    if c:
        conn.commit()    
        messagebox.showinfo("Success","Data inserted successfully")
def showData():
    query="select * from person1"
    c=cur.execute(query)
    lst_person=c.fetchall()
    for i in lst_person:
        print(i)
        data=str(i[0])+"\t"+i[1]+"\t"+str(i[2])+"\n"
        txtAll.insert(index=tk.END,chars=data)
lblName=tk.Label(text="Enter Name ")
lblName.grid(row=0,column=0)
txtName=tk.Entry()
txtName.grid(row=0,column=1)
lblAge=tk.Label(text="Enter age ")
lblAge.grid(row=1,column=0)
txtAge=tk.Entry()
txtAge.grid(row=1,column=1)
btnOk=tk.Button(text="Insert",command=insertData)
btnOk.grid(row=2,column=0)
btnAll=tk.Button(text="Show All",command=showData)
btnAll.grid(row=2,column=1)
txtAll=tk.Text(height=20,width=30)
txtAll.grid(row=3,column=0)
root.mainloop()
