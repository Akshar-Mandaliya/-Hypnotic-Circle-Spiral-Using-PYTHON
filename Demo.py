import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

for i in range(100):
    t.color(colors[i % 6])
    t.circle(i * 2)
    t.left(10)

turtle.done()
