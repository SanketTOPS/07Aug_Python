import pymysql

# Database create/connect
try:
    db=pymysql.connect(host='localhost',user='root',password='',database='testdb')
    print("Database connected!")
except Exception as e:
    print(e)


cr=db.cursor()

# Table Create
tbl_create="create table studinfo(id integer primary key auto_increment, name text, sub text)"
try:
    cr.execute(tbl_create)
    print("Table created successfully!")
except Exception as e:
    print(e)


# Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('nirav','java'),('ashok','php'),('hitesh','react'),('meet','c++')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


# Update Data
"""update_data="update studinfo set sub='python' where id=5"
try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)
except Exception as e:
    print(e)
