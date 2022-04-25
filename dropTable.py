import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

# Deletando uma tabela:
sql = "DROP TABLE users"

mycursor.execute(sql)

# Deletando apenas se existir:
sql = "DROP TABLE IF EXISTS users"
mycursor.execute(sql)