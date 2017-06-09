import pymysql

db = pymysql.connect(host = "localhost",user = "root",password = "alumno",db = "ElPelado",autocommit = True)
c = db.cursor()
c.execute("SELECT * from Cabeza;")
for item in c:
    print(item[1])
db.close()
