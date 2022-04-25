import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

# Limitando o numero de linhas a serem retornadas
mycursor.execute("SELECT * FROM users LIMIT 2")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

# Começando de outra posição:
mycursor.execute("SELECT * FROM users LIMIT 2 OFFSET 5")
myresult = mycursor.fetchall()

for i in myresult:
    print(i)