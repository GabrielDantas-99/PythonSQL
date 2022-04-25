import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

# Criando tabela:
mycursor.execute("CREATE TABLE users (name VARCHAR(255), password VARCHAR(6), location VARCHAR(255))")

# Checando se a tabela existe:
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)

# Inserindo a PRIMARY KEY:
mycursor.execute = ("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Insert dados na tabela (commit()):
sql = "INSERT INTO users (name, password, location) VALUES (%s, %s, %s)"
val = ("Gabriel", "123456", "Natal")
mycursor.execute(sql, val) 
mydb.commit()
print(mycursor.rowcount, 'Record Inserted')

# Inserindo multiplos valores na tabela (mycursor.executemany):
sql = "INSERT INTO users (name, password, location) VALUES (%s, %s, %s)"
val = [
    ('Emerson', '112233', 'Natal'),
    ('Jane', '332211', 'Natal'),
    ('Susan', '512234', 'Campina'),
    ('Vicky', '123512', 'Campina'),
    ('Ben', '661233', 'Campina'),
    ('William', '166845', 'Caicó'),
    ('Chuck', '097634', 'Caicó'),
    ('Viola', '998873', 'Caicó')
]
mycursor.executemany(sql, val) 
mydb.commit()
print(mycursor.rowcount, 'Was Inserted')

# Buscando o id inserido (mycursor.lastrowid):
sql = "INSERT INTO users (name, password, location) VALUES (%s, %s, %s)"
val = ("Berenice", "551233", "Caicó")
mycursor.execute(sql, val)
mydb.commit()
print('1 record inserted, ID:', mycursor.lastrowid)