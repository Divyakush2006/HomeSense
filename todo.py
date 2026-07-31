import mysql.connector as mc
import datetime as dt
from datetime import date
import time
import creds

connection=mc.connect(host="localhost",user="root",database="todo",password=creds.password)
cursor=connection.cursor()
today=date.today()


def add(work):  
    dat1=(work,today,"Not Done")
    q="insert into data values(%s,%s,%s)"
    cursor.execute(q,dat1)
    connection.commit()

def updatework(work):
    q="update data set status=%s where work=%s and dateow=%s"
    dat1=("Done",work,today)
    cursor.execute(q,dat1)
    connection.commit()

def delete(work):
    q="delete from data where dateow=%s and work=%s"
    dat1=(today,work)
    cursor.execute(q,dat1)
    connection.commit()

def show():
    q="select work,status from data where dateow=%s"
    dat1=(today,)
    cursor.execute(q,dat1)
    res=cursor.fetchall()
    return res