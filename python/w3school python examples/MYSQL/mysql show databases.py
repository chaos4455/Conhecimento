import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.42.222",
  user="usuario",
  passwd="senha"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)