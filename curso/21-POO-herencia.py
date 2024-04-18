class Persona ():
    def __init__(self, ape, nom, edad):
        self.apellido = ape
        self.nombre = nom
        self.edad = edad

    def presentar(self):
        print(f'''---------------------------------------- \nEl nombre completo de la persona es: {self.apellido}, {self.nombre}. \nEdad {self.edad} años''')
    
    def showData(self):
        self.presentar()

#p1 = Persona("Ramirez", "Carlos", 25)
#p1.presentar()

class Estudiante(Persona):
    def __init__(self, ape, nom, edad, carrera):
        super().__init__(ape, nom, edad)
        self.carrera = carrera

# para la sustitución de métodos se usa el mismo nombre, y por principio de especificidad, el programa toma la clase hija. 
# También se puede utilizar el método de la clase padre, anteponiendo 'super().metodo()'
    def showData(self):
        print("hello from sdhowData Estudent")    
        super().showData()

e1 = Estudiante("Lopez", "Ricardo", 23, "sistemas")
print(e1.showData())



        