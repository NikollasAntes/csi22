import turtle

# cria a janela
screen = turtle.Screen()
screen.title("Questao 1")
screen.setup(500, 500)
screen.bgcolor("#98FB98")

# cria a tartaruga
t = turtle.Turtle()
t.speed(3)
t.pensize(3)
t.color("#FF69B4")

# posiciona a tartaruga nas posicoes desejadas e desenha os quadrados
t.penup()
t.goto(-10, -10)
t.pendown()

for i in range(4):
    t.forward(20)
    t.left(90)

t.penup()
t.goto(-20, -20)
t.pendown()

for i in range(4):
    t.forward(40)
    t.left(90)

t.penup()
t.goto(-30, -30)
t.pendown()

for i in range(4):
    t.forward(60)
    t.left(90)

t.penup()
t.goto(-40, -40)
t.pendown()

for i in range(4):
    t.forward(80)
    t.left(90)

t.penup()
t.goto(-50, -50)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-60, -60)
t.pendown()

# mantem a janela aberta ate o usuario fecha-la
turtle.done()
