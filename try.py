import sqlite3
from sqlite3 import Error
def create_connection():
  
    conn = sqlite3.connect("D:\\Computer Stuff\\Documents\\pyscripts\\app1\\movielist.db")

 
    cur = conn.cursor()
    cur.execute("SELECT *")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
create_connection()
