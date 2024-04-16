import sqlite3

conn = sqlite3.connect('sqliteDDBB.sqlite')


c = conn.cursor()

c.execute(''' create table if not exists students(
    id integer primary key autoincrement,
    firstName text, 
    lastName text, 
    birthDate text, 
    career text)''')

def insert(name, surname, birthDate, career):
    conn = sqlite3.connect('sqliteDDBB.sqlite')
    c = conn.cursor()
    c.execute('insert into students (firstName, lastName, birthDate, career) values (?,?,?,?)' , (name, surname, birthDate, career))
    conn.commit()
    conn.close()
    
def selectData():
    conn = sqlite3.connect('sqliteDDBB.sqlite')
    c = conn.cursor()
    c.execute("select * from students")
    data = c.fetchall()
    print(data)
    conn.close()
    return data

def update(name, surname, birthDate, career):
    conn = sqlite3.connect("sqliteDDBB.sqlite")
    c = conn.cursor()
    c.execute("update students set FirstName = ?, lastName = ?, birthDate = ?, career = ?", (name, surname, birthDate, career))
    conn.commit()
    conn.close()
    
def delete(id):
    conn = sqlite3.connect("sqliteDDBB.sqlite")
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    
insert("Wilson","Smidth","1948-01-23","Politician")
#delete(2)
#update("Charl","Chaplin","1982-01-28","Actor")


data = selectData()

for each in data:
    print(f'''
            Complete name: {each[2]}, {each[1]} \n
            Date of birth: {each[3]} \n
            Career: {each[4]} \n
            -------------------------------
          ''')

conn.close()


