import tkinter as tk
from tkinter import messagebox
def greet():
    #messagebox.INFO()
    #messagebox.showinfo(message="This is my first msg box")
    messagebox.showwarning(message="Are you sure ?")
root=tk.Tk()
tk.Label(root,text="Enter your Name ").grid(row=0,column=0)
tk.Entry(root).grid(row=0,column=1)

tk.Button(root,text="OK",command=greet).grid(row=0,column=2)

tk.Label(root,text="Enter your Name ").grid(row=1,column=0)
tk.Entry(root).grid(row=1,column=1)

tk.Button(root,text="OK",command=greet).grid(row=1,column=2)
#print(txtname.get())
tk.mainloop()
