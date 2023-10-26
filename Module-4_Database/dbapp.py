import sqlite3

# Database create/connect
try:
    db=sqlite3.connect('tempdb.db')
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create
tbl_create="create table studinfo(id integer primary key autoincrement, name text, sub text)"
try:
    db.execute(tbl_create)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('nirav','java'),('ashok','php'),('hitesh','react'),('meet','c++')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

