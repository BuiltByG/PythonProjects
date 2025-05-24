import turtle
turtle.penup()
turtle.left(180)
turtle.forward(50)
turtle.pendown()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(25)
turtle.penup()

# Prompt the user to enter a point:

x = int(input('Enter x value: '))
y = int(input('Enter y value: '))


turtle.goto(x, y)
turtle.dot(6, "pink")
turtle.hideturtle()
turtle.color("pink")
turtle.pensize(7)
turtle.goto(-180, -175)
if x < -50 or x > 50 or y < -25 or y > 25:
    turtle.write('The point is not inside the rectangle', font=("Garamond", 24, "normal"))
else:
    turtle.write('The point is inside the rectangle', font=('Garamond', 24, 'normal'))
