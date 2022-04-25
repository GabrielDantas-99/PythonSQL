import mysql.connector
from numpy import MAY_SHARE_BOUNDS

mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "1234567",
  database = "pythondb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT, name VARCHAR(255), fav INT)")

sql = "INSERT INTO customers (id, name, fav) VALUES (%s, %s, %s)"
val = [
    ('1', 'John', '154'),
    ('2', 'Peter', '154'),
    ('3', 'Amy', '155'),
    ('4', 'Hannah', '156'),
    ('5', 'Michael', '156'),
]

mycursor.executemany(sql, val) 
mydb.commit()

mycursor.execute("CREATE TABLE products (id INT, name VARCHAR(255))")

sql2 = "INSERT INTO products (id, name) VALUES (%s, %s)"
val2 = [
    ('154', 'Chocolate Heaven'),
    ('155', 'Tasty Lemons'),
    ('156', 'Vanilla Dreams'),
]

mycursor.executemany(sql2, val2) 
mydb.commit()

# Combinando duas tabelas
sql = "SELECT \
  customers.name AS customer, \
  products.name AS favorite \
  FROM customers \
  INNER JOIN products ON customers.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print("INNER JOIN")
    print(x)

# Left Join
sql = "SELECT \
    customers.name AS customer, \
    products.name AS favorite \
    FROM customers \
    LEFT JOIN products ON customers.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
print("LEFT JOIN: ")
for i in myresult:
    print(i)

# RIGHT JOIN
sql = "SELECT \
    customers.name AS customer, \
    products.name AS favorite \
    FROM users \
    RIGHT JOIN products ON customers.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
print("RIGHT JOIN: ")
for i in myresult:
    print(i)