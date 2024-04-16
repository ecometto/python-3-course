class Course:
    def __init__(self, name, cost, teacher):
        self.name = name
        self.cost = cost
        self.__teacher = teacher

    def showCourseDetail(self):
        print("-" * 20)
        if self.__verifyTeacher():
            print(
                "The course {} has a cost of ${} and its teahcer is {}.".format(
                    self.name, self.cost, self.__teacher
                )
            )
        else:
            print("There is not teacher asigned for this course")
        print("-" * 20)

    def __verifyTeacher(self):
        print("Verifing if teacher is alreadey loaded...")
        if self.__teacher != "":
            return True
        else:
            return False

    # GETTERS AND SETTERS (en realidad son métodos internos para trabajar con atributos encapsulados)
    def getTeacher(self):
        return self.__teacher

    def setTeacher(self, teach):
        self.__teacher = teach


eng = Course("English for adults", 200, "Mr. Colleman")

eng.showCourseDetail()

eng.setTeacher("Mis Magoo")  # esta linea setea el valor de __teacher
eng.__teacher = "otro teacher.."  # esta linea crea un nuevo atributo, no setea el valor de __teacher
eng.showCourseDetail()
