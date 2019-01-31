import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.42.222",
  user="usuario",
  passwd="senha",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE clientes (name VARCHAR(255), address VARCHAR(255))")