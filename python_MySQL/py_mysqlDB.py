import mysql.connector
from tabulate import tabulate
import sys

con= mysql.connector.connect(host="localhost",user="root", password="Punaic", database="pythondb")

if con:
    print("connection available'")
else :
    print("connection not available'")

def insert(name, age,city):
    query_cursor= con.cursor()
    sql = "INSERT INTO USERS (NAME, AGE, CITY) VALUES (%s, %s, %s)"# %s is placeholder for getting respective values
    user= (name, age, city)
    query_cursor.execute(sql, user)
    con.commit() # we must have to commit insert, update and delete commands 
    print("User inserted successfully")

def update(name, age, city, id):
    query_cursor= con.cursor()
    sql = "UPDATE USERS SET NAME= %s, AGE=%s, CITY=%s where ID=%s"# %s is placeholder for getting respective values
    user= (name, age, city, id)
    query_cursor.execute(sql, user)
    con.commit() # we must have to commit insert, update and delete commands 
    print("User Updated successfully")


def select():
    query_cursor= con.cursor() #query_cursor is  a cursor object returned by the con.cursor() method
    sql = "SELECT ID, NAME, AGE, CITY from users"
    query_cursor.execute(sql)
    result = query_cursor.fetchall() # other mnethods fetchmany(5): returns first 5 rows or fetchall() returns all the rows
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))
    

def delete(id):
    query_cursor= con.cursor()
    sql= "DELETE FROM users WHERE id=%s"
    user =(id,)
    query_cursor.execute(sql,user)
    con.commit() 
    print ("User Deleted successfully")


while True:
    print("===========================")
    print("1. Insert Data")
    print("2. update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5.Exit")
    choice= int(input("Please enter your Choice:"))
    if choice >= 1 and choice <= 5:
        if choice == 1:
            name = input("Enter Name: ")
            age = input("Enter age: ")
            city= input("Enter city: ")
            insert(name,age,city)
        elif choice == 2:
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter age: ")
            city= input("Enter city: ")
            update(name,age,city, id)
        elif choice==3:
            select()
        elif choice==4:
            id = int(input("Enter ID of Record you want to del:"))
            delete(id)
        elif choice==5:
            sys.exit()
    else :
        print("Invalid choice. Pls Try again")
