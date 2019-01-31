import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.42.222",
  user="usuario",
  passwd="senha"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")