import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

sql = "UPDATE users SET location = 'Caicó' WHERE location = 'Natal'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# Previnindo SQL Injection

sql = "UPDATE users SET location = %s WHERE location = %s"
val = ("Natal", "Caicó")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Record(s) affected")