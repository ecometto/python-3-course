
txt = "Hello World !!"

print(txt.lower())
print(txt.upper())
print(txt.capitalize())
print(txt.title())

world = txt.find("World")
print(f"la palabra World inicia en la posicion: {world}")

countO= txt.lower().count("o")
print("la cantidad de letras 'o' y 'O' es: " + str(countO))

print(txt.replace("H", "h"))
print(txt)

array = txt.split(" ")
print(array)