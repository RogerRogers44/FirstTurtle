import turtle

Bob = turtle.Turtle()
Bobe = turtle.Turtle()
bawb = turtle.Turtle()
bobb = turtle.Turtle()
bbob = turtle.Turtle()
bowb = turtle.Turtle()

Bob.color("yellow")
Bobe.color("black")
bawb.color("red")
bobb.color("purple")
bbob.color("red")
bowb.color("white")

# Face fill
Bob.penup()
Bob.right(90)
Bob.forward(200)
Bob.left(90)
Bob.pendown()
Bob.begin_fill()
Bob.circle(250)
Bob.end_fill()

# Outline
Bobe.penup()
Bobe.right(90)
Bobe.forward(200)
Bobe.left(90)
Bobe.pendown()
Bobe.circle(250)
# Mouth
bawb.penup()
bawb.right(90)
bawb.forward(35)
bawb.left(90)
bawb.pendown()
bawb.backward(125)
bawb.begin_fill()
bawb.forward(250)
bawb.right(90)
for i in range(10):
    bawb.forward(5)
    bawb.right(5)
for i in range(8):
    bawb.forward(10)
    bawb.right(5)
bawb.forward(85)
for i in range(9):
    bawb.forward(10)
    bawb.right(5)
for i in range(10):
    bawb.forward(5)
    bawb.right(5)
bawb.end_fill()

bowb.right(90)
bowb.forward(35)
bowb.left(90)
bowb.forward(90)

bobb.backward(200)
bbob.forward(100)

turtle.exitonclick()
