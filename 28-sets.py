# sets = colecciones desordenadas de elementos únicos

numeros = {1, 3, 3, 5, 7, 9, 5, 4, 8, 6, 3, 9, 6}
print(numeros)

numeros2 = {3, 5, 11, 17, 9, 6}

numerosEnComunNOREPETIDOS = numeros.intersection(numeros2)
todosLosNumerosNOREPETIDOS = numeros.union(numeros2)
soloDiferentes = numeros.symmetric_difference(numeros2)

print("---------------------")
print(numerosEnComunNOREPETIDOS)
print(todosLosNumerosNOREPETIDOS)
print(soloDiferentes)

text = "Este es un texto donde voy a contar la cantidad de palabras que contiene. voy a repetir algunas como: texto, contar, cantidad, palabras. Veremos cuantas cuenta en total, y cuantas no repetidas"

def contar (texto):
    txt1 = texto.replace(",", " ")
    txt2 = txt1.replace(".", " ") #las dos funciones anteriores e pueden 'anidar' txt1 = texto.replace(",", " ").replace(".", " ")
    list = txt2.split()
    setPalabras = set(list)
    return setPalabras

print("---------------------")
unicas = contar(text)
print(len(unicas))
print(contar(text))

print("---------------------")
lista = list(unicas)
lista.sort()
print(lista)

def prueba(texto):
    texto = texto.replace(",", " ")
    listaPrueba = texto.split()
    listaNueva = []
    for n in listaPrueba:
        if  n in listaNueva:
            continue
        else:
            listaNueva.append(n)
    return listaNueva

txtPrueba="esto es un texto de prueba, texto de prueba"

print(prueba(txtPrueba))