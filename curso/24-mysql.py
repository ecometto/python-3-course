import mysql.connector as mysql

def connect():
    try:
        conn = mysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="condominio"
        )
        if conn.is_connected():
            print("connetion stablished successfully")
            return conn

    except mysql.Error as ex:
        print("Error while connectiong", ex)

def closeConnection(conn):
    if conn.is_connected():
        conn.close()
        print("** Connection successfully closed **")
        
def showData():
    conn = connect()
    c = conn.cursor()
    c.execute("select * from tipousuario")
    data = c.fetchall()
    # print(data)
    for n in data :
        print(f"Tipo propietario: {n[1]}")
#    print(f"total de registros: {c.rowcount}")
    closeConnection(conn)
        
def insertData():
    nombre = input("INGRESE UN TIPO de USUARIO: ")
    conn = connect()
    c = conn.cursor()
    # c.execute("insert into tipousuario (nombre, vigencia) values (%s, 1)", (nombre,))
    c.execute("insert into tipousuario (nombre, vigencia) values ('{0}', 1)".format(nombre))

    conn.commit()
    closeConnection(conn)
 
def UpdateData():
    conn = connect()
    c = conn.cursor()
    id = int(input("insert User ID you want to update/modify: "))
    newName = input("Insert the new name: ")
    c.execute(f"update tipousuario set nombre = '{newName}' where codigo = {id}")
    conn.commit()
    closeConnection(conn)

def deleteData():
    conn = connect()
    c = conn.cursor()
    id = int(input("insert User ID you want to delete: "))
    c.execute(f"DELETE from tipousuario where codigo = {id}")
    conn.commit()
    closeConnection(conn)
    
# insertData()
UpdateData()
# deleteData()

showData()