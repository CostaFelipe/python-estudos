#coding=utf-8
#classes
#Criando e usando uma classe
class Dog():
    """Uma tentativa simples de modelar uma classe"""
    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def rool_over(self):
        print(self.name.title() + " rolled over!")

#Criando uma instância a partir de uma classe
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#Chamando métodos
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.rool_over()
