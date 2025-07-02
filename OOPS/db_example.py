import sqlite3
conn=sqlite3.connect("mydb.db")
cur=conn.cursor()
# query="create table if not exists person1(id integer primary key AUTOINCREMENT,name text,age integer)"
# c=cur.execute(query)
# if c:
#     print("Table created successfully...")

# name=input("Please enter username ")
# age=int(input("Please enter age"))

# c=cur.execute("insert into person1(name,age) values (?,?)",(name,age))
# if c:
#      print("Data inserted successfully...")
# conn.commit()
query="select * from person1"
c=cur.execute(query)

lst_person=c.fetchall()
for i in lst_person:
    print(i)