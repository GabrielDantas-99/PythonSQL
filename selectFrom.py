import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

# Selecionando todos os resultados de uma tabela (SELECT):
mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

# Selecionando Colunas (SELECT + nomeColuna):
mycursor.execute("SELECT name, location FROM users")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Retornando a primeira linha (fetchone())
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchone()
print(myresult)