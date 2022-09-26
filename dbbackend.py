import sqlite3
#backend

def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, SDS TEXT, Name TEXT, LEI TEXT, Email TEXT,Tel TEXT, Sales TEXT, Parent TEXT, Notes TEXT)")
    con.commit()
    con.close()

def addStdRec(SDS, Name, LEI , Email ,Tel, Sales, Parent, Notes):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?) ", (SDS, Name,LEI,Email,Tel, Sales,Parent,Notes))
    con.commit()
    con.close()
    
def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows
    
def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close()
    
def searchData(SDS="", Name="", LEI="",Email="", Tel="", Sales="", Parent="", Notes=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE 'SDS'=? OR 'Name'=? OR 'LEI'=? OR 'Email'=? OR 'Tel'=? OR 'Sales'=? OR 'Parent'=? OR 'Notes'=?",(SDS,Name,LEI,Email,Tel, Sales,Parent,Notes))
    rows = cur.fetchall()
    con.close()
    return rows
    
def dataUpdate(id,SDS="", Name="", LEI="",Email="", Tel="", Sales="", Parent="", Notes=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET SDS=?, Name=?, Email=?,Tel=?,Parent=?Notes=?,WHERE id=?", (SDS, Name, LEI, Email, Tel, Sales, Parent, Notes, id))
    con.commit()
    con.close()

studentData()
