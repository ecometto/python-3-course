# traditional function:
def getMultiplos(value, limite):
    num = 1
    lista = []
    while num < limite:
        lista.append(num*value)
        num = num + 1
    return lista

print(getMultiplos(2, 10))

# with generators we obtain the values of the list, one by one
def getMultiplosGen(value, limite):
    num = 1
    while num < limite:
        yield num * value
        num = num + 1

listaGen = getMultiplosGen(3,10)
# for x in listaGen:
#     print(x)

print(f"el primer numero es: {next(listaGen)}")
print("aca pueden ir muchas lineas de codigo \n ")
      
print(f"el SEGUNDO numero es: {next(listaGen)}")
print("aca pueden ir muchas lineas de codigo \n ")

print(f"el TERCERO numero es: {next(listaGen)}")
print("aca pueden ir muchas lineas de codigo \n ")


def printRange(r):
    for i in range(r):
        yield i

rango = printRange(20)
print("esto es una linea")
print(next(rango))
print("esto es una linea")
print(next(rango))
print("esto es una linea")
print(next(rango))

for r in printRange(20):
    print("-" * 20)
    print("new line for generator")
    print(r)

