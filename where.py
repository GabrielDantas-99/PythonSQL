import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()
'''
# Selecionando com um filtro:
sql = "SELECT * FROM users WHERE location = 'Caicó'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

# Usando o WildCard Characters:
sql = "SELECT * FROM users WHERE location LIKE '%tal%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in myresult:
    print(i)
'''
# Evitando injeção de SQL
sql = "SELECT * FROM users WHERE location = %s"
loc = ("Campina",)

mycursor.execute(sql, loc)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)