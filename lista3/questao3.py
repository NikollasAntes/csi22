# Exemplo polimorfismo

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        print("au au")

class Gato(Animal):
    def som(self):
        print("miau")

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.som()

# Exemplo Duck Typing

class Pato:
    def nadar(self):
        print("Pato nadando")

class Barco:
    def nadar(self):
        print("Barco navegando")

def fazer_nadar(objeto):
    objeto.nadar()

fazer_nadar(Pato())
fazer_nadar(Barco())