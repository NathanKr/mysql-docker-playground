import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123abc",
  database = 'db1'
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employees")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)