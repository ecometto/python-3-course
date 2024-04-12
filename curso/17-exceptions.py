# exception is an error during the execution of a program

def division(n1, n2):
    return (n1/n2)
    
divisor=[250,800,500,"hello",160]
dividendo=[2,4,0,12,16]


for i in range(len(divisor)):
    try:
        print(f"la division es: {division(divisor[i],dividendo[i])}")
    except ZeroDivisionError:
        print("Error. Revise el valor ingresado del dividendo. (Debe ser diferente a cero)")
    except TypeError:
        print("Error en el tipo de datos ingresado")
    except:
        print("hubo algún error no identificado")
    finally:
        print("vuelta finalizada \n")