import sqlite3
db=sqlite3.connect("list.db")
cr=db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS list(ID INTEGER,name TEXT,phone TEXT)")
print ("""Choose From The Following Options\n
[A]_Add
[B]_Delete
[C]_Retrive
[D]Update""")
op=input("==>")
if (op=='a' or op=='A'):
    
    try:
       
       print ("Insert The ID , Phone.no And The Name of The person You Want")
       idd=input("ID=>")
       n=input("Name=>")
       p=input("Phone.No=>")
      
       cr.execute(f"INSERT INTO list (ID,Name,Phone) values ('{idd}','{n}','{p}')")
       db.commit()
       db.close()
       print("________Done..Check The Data In Sqlite3__________")
    except:
       print("ERROR")
#Deleting
elif(op=='b' or op=='B'):
   try:
        #db=sqlite3.connect("list.db")
        #cr=db.cursor() 
        print ("Enter The ID of The Person")
        idf=input("ID=>")
        cr.execute(f"DELETE FROM list WHERE ID ='{idf}'")
        db.commit()
        db.close()
        print("________Done..Check The Data In Sqlite3__________")
   except :
       print ("ERROR")
elif (op=='c' or op=='C'):
    try:
        cr.execute("SELECT * FROM list")
        print(cr.fetchall())
        db.commit()
        db.close()
    except:
        print("ERROR")
else:
    try:
        print ("Enter The ID of The Person")
        idr=input("ID=>")
        print ("Enter The Name of The Person")
        nu=input("Name=>")
        cr.execute(f"UPDATE List SET Name='{nu}' WHERE ID={idr}")
        db.commit()
        db.close()
    except:
        print("ERROR")