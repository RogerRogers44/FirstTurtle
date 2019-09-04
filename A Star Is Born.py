import turtle

turtle.speed(200)


def Star(side):
    for size in range(5):
        turtle.forward(side)
        turtle.right(144)


def StarSpiral():
    for size in range(95):
        Star(size)
        turtle.right(7)


StarSpiral()

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()

StarSpiral()

turtle.penup()
turtle.goto(100, -200)
turtle.pendown()

StarSpiral()

turtle.exitonclick()
