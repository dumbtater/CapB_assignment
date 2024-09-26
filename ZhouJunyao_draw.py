#from turtle import *
import turtle
print("----- Draw A Cute Cat Student Name: Zhou Junyao UID:3036311651 ----")
# Set up the screen
screen = turtle.Screen()
screen.title("Phone Drawing")
screen.bgcolor("white")

# Create a turtle object
phone = turtle.Turtle()
phone.speed(0)
phone.color("black")
phone.width(3)

# Draw the phone
phone.penup()
phone.goto(-100, 200)
phone.pendown()
phone.fillcolor("#a4b0be")
phone.begin_fill()
for _ in range(2):
    phone.forward(200)
    phone.right(90)
    phone.forward(400)
    phone.right(90)
phone.end_fill()

# Draw the screen
phone.penup()
phone.goto(-80, 180)
phone.pendown()
phone.fillcolor("black")
phone.begin_fill()
for _ in range(2):
    phone.forward(160)
    phone.right(90)
    phone.forward(320)
    phone.right(90)
phone.end_fill()


# Hide the turtle and display the drawing
phone.hideturtle()
screen.mainloop()

