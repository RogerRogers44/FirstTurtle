import turtle

turtle.shape("turtle")


turtle.speed(200)

# star thing
for i in range(41):
    turtle.forward(100)
    turtle.right(123)


turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.pendown()
# cool thing
for i in range(50):
    turtle.left(5)
    turtle.forward(5)
    for i in range(8):
        turtle.forward(50)
        turtle.left(45)

turtle.penup()
turtle.right(90)
turtle.forward(300)
turtle.pendown()
turtle.speed(5)
# triangle square that took way too long
for i in range(3):
    turtle.right(90)
    turtle.forward(100)
# makes the turtle look better
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(90)
turtle.penup()
turtle.forward(200)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.right(90)


turtle.exitonclick()
