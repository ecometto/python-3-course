
#forma tradicional de filtrar (sin filter function)
edades = [11,22,51,43,10,65]

def mayorEdad(edades):
    mayores = []
    for edad in edades:
        if edad > 18:
            mayores.append(edad)
    return mayores

mayores = mayorEdad(edades)
print(mayores)

# --------------------------------------------------------------------------------------------------
# filtrado usando filter
#primero se define la funcion que, según la condicion indicada, retornará True o False
def mayor(edad):
    return edad > 18

#luego se aplica la funcion generada, a la lista de objetos iterables. Parametros: (función, objeto iterable)
mayoresFilter = filter(mayor, edades)
print(mayoresFilter) 
#dado que retorna un objeto filter, se debe transformar a lista
mayoresFilterLista = list(filter(mayor, edades))
print(mayoresFilterLista)

#-------------------------------------------------------------------------
# #otro ejemplo
print("----------------------------------------")

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} anios"
        
listaPersonas2 = [ Persona("juana", 30), Persona("pedro", 20), Persona("maria", 55), Persona("lucas", 32) ]

def mayores30(persona):
    return persona.edad > 30


personasMas30 = list(filter(mayores30, listaPersonas2))
for persona in personasMas30:
    print(persona)


# MAP ---------------------------------
tuplaPrueba=(1,11,22,52,32,4,58,96,37,44)
def doble(num):
    return num * 2

dobles = list(map(doble, tuplaPrueba)) 
print(dobles)


palabrasEnie = ["año", "caño", "caña", "compañia"]
def reemplazarEnie(palabra):
    corrected = palabra.replace("ñ", "n")
    # corrected = "--" + palabra + "--"
    return corrected

c = list(map(reemplazarEnie, palabrasEnie))
print(c)