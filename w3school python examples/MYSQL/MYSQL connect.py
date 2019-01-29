import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.42.222",
  user="usuario",
  passwd="senha"
)

print(mydb)
