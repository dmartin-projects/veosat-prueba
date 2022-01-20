import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="",
    passwd="",
    database="veosatdb"
)

cursor = db.cursor()

