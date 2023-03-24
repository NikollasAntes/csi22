import turtle

# cria a janela
screen = turtle.Screen()
screen.title("Questao 4")
screen.bgcolor("#98FB98")

# cria a tartaruga
t = turtle.Turtle()
t.speed(10)
t.pensize(1)
t.color("#0000CD")

# posiciona a tartaruga
t.penup()
t.goto(-150, 0)
t.pendown()

# cria a primeira imagem
for i in range(100):
    t.forward(2*i)
    t.right(90)

# posiciona a tartaruga
t.penup()
t.goto(150, 0)
t.pendown()

# cria a segunda imagem
for i in range(100):
    t.forward(2*i)
    t.right(89)

# manter a janela aberta
turtle.done()