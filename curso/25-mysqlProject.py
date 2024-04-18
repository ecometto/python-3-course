import mysql.connector as mysql

# #CREAR LA BASE DE DATOS DESDE PYTHON. CONECTAR SOLO AL HOST (CON PUERTO + USUARIO Y PASS), NO LA LA DDBB (porque no existe, obvio)
# conn = mysql.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password=""
# )

# c = conn.cursor()
# c.execute("create database sistema_cursos")
# conn.commit()
# conn.close()

# # CREANDO LA TABLA DESDE PYTHON
# conn = mysql.connect(
#     host="localhost",
#     port=3306, 
#     user="root",
#     password="",
#     db="sistema_cursos",
# )

# c = conn.cursor()
# c.execute("""create table if not exists cursos  (
#     codigo int auto_increment primary key, 
#     nombre varchar(100), 
#     creditos int)""")
# conn.commit()
# conn.close()


# FUNCIONES Y SENTENCIAS CON BASE DE DATOS
def connect():
    conn = mysql.connect(
    host="localhost",
    port=3306, 
    user="root",
    password="",
    db="sistema_cursos",
)
    return conn

def getData():
    conn = connect()
    c = conn.cursor()
    c.execute("select * from cursos")
    data = c.fetchall()
    print(f"*******************************")
    print("code \tdescription \tcredits")
    for cada in data:
        print(f"{cada[0]}  \t{cada[1]} \t{cada[2]}")
    print("******************************")

       
def addData():
    name = input("Type the name of the new course: ")
    credits = int(input("Type de credits for this course: "))
    conn = connect()
    c = conn.cursor()
    c.execute(f"INSERT INTO cursos( nombre, creditos) VALUES ('{name}',{credits})")
    conn.commit()
    conn.close()

def modifyData():
    id = int(input("Type de Id of the course you need to MODIFY: "))
    name = input("Type the NEW name of the new course: ")
    credits = int(input("Type the NEW credits for this course: "))
    conn = connect()
    c = conn.cursor()
    c.execute(f"update cursos set nombre='{name}', creditos={credits} where codigo={id}")
    conn.commit()
    conn.close()

def deleteData():
    id = int(input("Type de Id of the course you need to DELETE: "))
    conn = connect()
    c = conn.cursor()
    c.execute(f"delete from cursos where codigo = {id}")
    conn.commit()
    conn.close()
    
def init():
    exit = False
    while not exit:
        print("""
            SELECT YOUR OPTION: 
            1- Show Courses
            2- Add Courses
            3- Modify courses
            4- Delete Courses
            5- Exit
            """)
        option = int(input("Option: "))
        options = [1,2,3,4,5]
        
        while option not in options:
            print("Please check the entered value.. ")
            option = int(input("Option: "))
            
        if option == 1:
            getData()
        elif option == 2:
            addData()
        elif option == 3:
            modifyData()
        elif option == 4:
            deleteData()
        elif option == 5:
            exit = True



init()