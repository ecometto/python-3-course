
class Person():
    def greet(self, person):
        print(f"Hello, I'm a Person. My name is {person}")

class Student():
    def greet(self, student):
        print(f"Hello, I'm an Student. My name is  {student}")

class Worker():
    def greet(self, worker):
        print(f"Hello, I'm a Worker. My name is  {worker}")

#in this function, we can see that puede tomar el saludo de la clase que se le pase como parámetro
def greetingClasses(somebody):
    somebody.greet("albert")
    
p1 = Worker()
greetingClasses(p1)
    