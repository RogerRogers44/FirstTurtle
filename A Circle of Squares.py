import turtle

turtle.shape("turtle")


turtle.speed(200)


def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)


for x in range(60):
    square(100)
    turtle.right(5)


turtle.exitonclick()
