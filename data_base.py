import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mc = mydb.cursor()
'''
# Criando um banco de dados 'pythondb'
mc.execute("CREATE DATABASE pythondb")

# Exibindo os bancos de dados criados
mc.execute("SHOW DATABASES")

for i in mc:
    print(i)

# Criando tabela:
mc.execute("CREATE TABLE users (name VARCHAR(255), password VARCHAR(6), location VARCHAR(255))")

# Checando se a tabela existe:
mc.execute("SHOW TABLES")
for i in mc:
    print(i)

# Inserindo a PRIMARY KEY:
mc.execute = ("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Insert dados na tabela:
sql = "INSERT INTO users (name, password, location) VALUES (%s, %s, %s)"
val = ("Gabriel", "123456", "Natal")
mc.execute(sql, val) 
mydb.commit()
print(mc.rowcount, 'Record Inserted')

# Inserindo multiplos valores na tabela:
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
mc.executemany(sql, val) 
mydb.commit()
print(mc.rowcount, 'Was Inserted')
'''

# Buscando o id inserido:
sql = "INSERT INTO users (name, password, location) VALUES (%s, %s, %s)"
val = ("Berenice", "551233", "Caicó")
mc.execute(sql, val)
mydb.commit()
print('1 record inserted, ID:', mc.lastrowid)
