import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mc = mydb.cursor()

# Criando um banco de dados 'pythondb'
mc.execute("CREATE DATABASE pythondb")

# Exibindo os bancos de dados criados
mc.execute("SHOW DATABASES")

for i in mc:
    print(i)


