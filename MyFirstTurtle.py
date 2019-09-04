import turtle

turtle.shape("turtle")

turtle.speed(200)
# outside hexagon shape
for a in range(2):
    for b in range(50):
        turtle.color("purple")
        turtle.forward(100)
        turtle.right(123)
    turtle.left(90)
    turtle.forward(100)
    for c in range(50):
        turtle.color("green")
        turtle.forward(100)
        turtle.right(123)
    turtle.left(90)
    turtle.forward(100)
    for i in range(50):
        turtle.color("orange")
        turtle.forward(100)
        turtle.right(123)
    turtle.left(90)
    turtle.forward(100)
turtle.penup()
turtle.right(213)
turtle.forward(100)
turtle.left(90)
turtle.pendown()
# inside thing
for a in range(4):
    for b in range(50):
        turtle.color("purple")
        turtle.forward(50)
        turtle.right(123)
    turtle.right(120)
    turtle.forward(100)
    for c in range(50):
        turtle.color("green")
        turtle.forward(50)
        turtle.right(123)
    turtle.right(120)
    turtle.forward(100)
    for i in range(50):
        turtle.color("orange")
        turtle.forward(50)
        turtle.right(123)
    turtle.right(120)
    turtle.forward(100)
turtle.penup()
turtle.left(50-23)
turtle.forward(200)
turtle.exitonclick()
