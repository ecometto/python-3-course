class Country():
    def __init__(self, nombre, continente):
        self.nombre = nombre
        self.continente = continente

    def __str__(self) -> str:
        txt = "The country {0} in the contienet: {1}"
        return txt.format(self.nombre,self.continente)


class City():
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def __str__(self) -> str:
            txt = "The city {0} in {1}"
            return txt.format(self.nombre,self.pais)


class Neighborhood():
    def __init__(self, nombre, city):
        self.nombre = nombre
        self.city = city

    def __str__(self) -> str:
            txt = "The neighborhood {0} is in {1}"
            return txt.format(self.nombre, self.city)

Argentina = Country("Argentina", "america")
Cordoba= City("Cordoba", Argentina)
Observatorio = Neighborhood("observatorio", Cordoba)

print(Observatorio)
