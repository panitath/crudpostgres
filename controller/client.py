
import sys

sys.path.insert(1, 'service')

import connectpostgres as con

#Function insert 
def insert(fullname,email,age):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "insert into person (fullname,email,age) values (%s,%s,%s)"
    cursor.execute(sql,(fullname,email,age))
    conn.commit()
    cursor.close()

def select_all():
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "select * from person"
    cursor.execute(sql)
    result = cursor.fetchall()
    rows = [['ID','Fullname','Email','Age','Date']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows


def select_by_id(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "select * from person where id =%s"
    cursor.execute(sql,(id))
    result = cursor.fetchall()
    rows = [['ID','Fullname','Email','Age','Date']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows

def update(id,fullname,email,age):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "update person set fullname = %s, email = %s, age = %s where id =%s"
    cursor.execute(sql,(fullname,email,age,id))
    conn.commit()
    cursor.close()

def delete(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "delete from person where id =%s"
    cursor.execute(sql,(id,))
    conn.commit()
    cursor.close()
