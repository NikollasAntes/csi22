class Pai1:
    def mensagem(self):
        print("Mensagem do Pai1")

class Pai2:
    def mensagem(self):
        print("Mensagem do Pai2")

class Pai3:
    def mensagem(self):
        print("Mensagem do Pai3")

class Filho1(Pai1, Pai2, Pai3):
    pass

class Filho2(Pai2, Pai1, Pai3):
    pass

class Filho3(Pai3, Pai1, Pai2):
    pass

f1 = Filho1()
f1.mensagem()

f2 = Filho2()
f2.mensagem()

f3 = Filho3()
f3.mensagem()