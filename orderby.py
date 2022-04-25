import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

# Ordernando linhas através pelo nome
sql = "SELECT * FROM users ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

# Ordernando linhas de forma descendente:
sql = "SELECT * FROM users ORDER BY location DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in myresult:
    print(i)