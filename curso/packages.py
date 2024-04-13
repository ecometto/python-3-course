'''
from packages.mathematicalOperations import *
from packages.stringsOperations import  *

print(sumar(8,5))
print(dividir(10,4))
print(contarLetras("hello Wolrd!!"))
print(separarPalabras("hello wolrd! Python is great.."))
'''

import packages.mathematicalOperations as mathOp
import packages.stringsOperations as stringOp

print(mathOp.sumar(8,5))
print(mathOp.dividir(10,4))
print(stringOp.contarLetras("hello Wolrd!!"))
print(stringOp.separarPalabras("hello wolrd! Python is great.."))
