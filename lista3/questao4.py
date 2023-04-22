class Calculadora:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma(self):
        return self.x + self.y

    @classmethod
    def multiplicacao(cls, x, y):
        return x*y

    @staticmethod
    def divisao(x, y):
        if y == 0:
            return "erro"
        return x/y
