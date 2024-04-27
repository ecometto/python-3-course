
file = open("30-Mifile.txt", "r+")
f = file.readlines()
file.close()

for cada in f:
    print(cada)
    
print(f)

# in the sentence 'With' it open and then close the file
with open("30-Mifile.txt", "r+") as f:
    data = f.readlines()
    for i in range(0,len(data)):
        data[i]=data[i].strip()

dataSet = set()
def armarSet(data):
    global dataSet
    for cada in data:
        dataSet.add(cada)
    return dataSet
    
print(armarSet(data))


with open('30-Mifile.txt') as f:
    tresVecesPrimera = []
    for i in range (1,4):
        linea = f.readline()
        linea = linea.rstrip()
        tresVecesPrimera.append(linea)
        print(f.tell())
        f.seek(0)
        print(f.tell())
    
print(tresVecesPrimera)


print('#'*30)
with open('30-Mifile.txt') as f:
    allFile = f.read()
    print(f"The last character is in position {f.tell()}.")
    dataSplit = allFile.split()
    print(f"the quantity of words is: {len(dataSplit)}")
    dataSet = set()
    for cada in dataSplit:
        dataSet.add(cada)
    print(f"There are {len(dataSplit) - len(dataSet)} repeated words")
    
print(dataSplit)


print('#'*30)
with open('30-Mifile.txt', 'r+') as f:
    allFile = f.read() #para posicionar el cursor al fondo
    totalCharacters = f.tell() #obtengo cantidad de caracteres
    halfCharters = int(totalCharacters / 2)
    f.seek(0) #posiciono cursos en inicio
    halfFile = f.read(halfCharters) #Para leer solamente hasta el caracter indicado como parámetro
    print("the first half of the file is:")
    print(halfFile)
    print("---------------------------")


with open('30-Mifile.txt', 'r') as f:
    mitad = int(len(f.read()) / 2)
    f.seek(0)
    primeraMitad = f.read(mitad)
    print(primeraMitad
          )
    textoAInsertar = "\nI love programing.. (this sentence was added while program execution)\n"

    segundaMitad = f.read()
    print(segundaMitad)
    
    print("---------------------------")
    
    total = primeraMitad + textoAInsertar + segundaMitad
    print(total)
    

with open('30-Mifile.txt', 'r+') as f:
    primera = f.readline()
    segunda = f.readline()
    text = "Aca en el segundo renglon va a ir este texto... Tomá!\n"
    resto = f.read()
    total = primera + segunda + text + resto
    print(total)
    f.seek(0)
    f.write(total)
    f.seek(0)
    print(f.read())