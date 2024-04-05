
name = input("What's your name? ")
age = input("What's your age? ")

def introduce(n, a):
    print("Hello. Your name is {} and you are {} years old!!".format(n, a))
    print(f"Otra forma de concatenar la edad es convertirla en str. Tu tienes {str(a)} anios")

introduce(name, age)