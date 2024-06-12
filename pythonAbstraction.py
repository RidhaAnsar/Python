from abc import ABC, abstractmethod

class Animal(ABC):
    def makesound(self):
        pass
    def eat(self):
        print("Animal is eating") 
class cat(Animal):
    def makesound(self):
        print('meow')
class dog(Animal):
    def makesound(self):
        print("woof woof")
dg=dog()
ct=cat()
ct.makesound()
ct.eat()
dg.makesound()
dg.eat()