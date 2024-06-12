class person1:
    def name(self):
        print("My name is ABC")
    def place(self):
        print("I am from Kochi")
class person2:
    def name(self):
        print("My name is XYZ")
    def place(self):
        print("I am from Trissur")

p1=person1()   #p1 is the object of person1 class
p2=person2()   #p2 is the object of person2 class

for x in (p1, p2):
    x.name()
    x.place()
