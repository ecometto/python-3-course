class Persona ():
    def __init__(self, ape, nom, edad):
        self.apellido = ape
        self.nombre = nom
        self.edad = edad

    def presentar(self):
        print(f"El nombre completo de la persona es: {self.apellido}, {self.nombre}. \nEdad {self.edad} años")

p1 = Persona("Ramirez", "Carlos", 25)
p1.presentar()

class Estudiante(Persona):
    def __init__(self, ape, nom, edad, carrera):
        super().__init__(ape, nom, edad)
        self.carrera = carrera

e1 = ("Lopez", "Ricardo", 23, "sistemas")
print(e1.apellido)