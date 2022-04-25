import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

# Deletando linhas com o lacation 'Campina'
# Importante inserir 'WHERE' quando não se quer deletar todas as linhas
sql = "DELETE FROM users WHERE name = 'Gabriel'"

mycursor.execute(sql)
# Necessário para fazer mudanças no bd
mydb.commit()

print(mycursor.rowcount, 'record(s) deleted')

# Previninco SQL Injecction:
sql = "DELETE FROM users WHERE location = %s"
loc = ("Caicó",)

mycursor.execute(sql, loc)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
