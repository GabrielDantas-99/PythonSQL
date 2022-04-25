import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

print(mydb)