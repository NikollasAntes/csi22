import turtle

# cria a janela
screen = turtle.Screen()
screen.title("Questao 2")
screen.bgcolor("#98FB98")

# cria a tartaruga
tess = turtle.Turtle()
tess.speed(4)
tess.pensize(3)
tess.color("#FF69B4")

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

# draw_poly(tess, 8, 50)

# mantem a janela aberta ate o usuario fecha-la
turtle.done()