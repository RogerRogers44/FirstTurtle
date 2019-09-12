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
bbob.color("black")
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

# teeth
bowb.penup()
bowb.right(90)
bowb.forward(35)
bowb.right(90)
bowb.forward(120)
bowb.right(180)
bowb.pendown()
for i in range(9):
    bowb.begin_fill()
    bowb.right(120)
    bowb.forward(15)
    bowb.right(120)
    bowb.forward(15)
    bowb.right(120)
    bowb.forward(15)
    bowb.end_fill()
    bowb.penup()
    bowb.forward(30)
    bowb.pendown()

# right eye
bbob.penup()
bbob.forward(50)
bbob.left(90)
bbob.forward(75)
bbob.right(90)
bbob.forward(25)
bbob.pendown()
bbob.begin_fill()
bbob.color("white")
bbob.circle(50)
bbob.end_fill()
bbob.color("black")
bbob.circle(50)

# left eye
bobb.penup()
bobb.forward(50)
bobb.left(90)
bobb.forward(75)
bobb.right(90)
bobb.forward(25)
bobb.backward(200)
bobb.pendown()
bobb.begin_fill()
bobb.color("white")
bobb.circle(50)
bobb.end_fill()
bobb.color("black")
bobb.circle(50)

# makes turtles pretty
Bob.penup()
Bob.right(90)
Bob.forward(50)

Bobe.penup()
Bobe.right(90)
Bobe.forward(100)

bawb.penup()
bawb.right(180)
bawb.forward(200)

bowb.penup()
bowb.right(90)
bowb.forward(200)
bowb.color("brown")

bbob.penup()
bbob.right(90)
bbob.forward(300)

bobb.penup()
bobb.right(90)
bobb.forward(300)

turtle.exitonclick()
