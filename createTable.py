import mysql.connector
dbcon=None
try:
   dbcon=mysql.connector.connect(host='localhost',user='root',password='Password@1',database='dbone')
   cursor=dbcon.cursor()
   sqlst='''INSERT INTO employees values(101,"rahul",45000.45);'''
   cursor.execute(sqlst)
   dbcon.commit()
   print("new employee record - inserted")



except mysql.connector.errors.Error as e:
    print(e.msg)
