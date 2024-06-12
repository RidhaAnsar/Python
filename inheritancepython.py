class teacher:
    def __init__(self, name, sub):
        self.name=name
        self.sub=sub
    def printteacher(self):
        print(self.name, self.sub)

obj=teacher("abc", "Maths")
obj.printteacher()

class student(teacher):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def printstudent(self):
        print(self.name, self.age)

obj=student("pqr", 18)
obj.printstudent()