# Python program to create a simple square animation
# importing the turtle module
import turtle

# making an instance of the turtle object for drawing
ttl = turtle.Turtle()
# creating a screen to draw
screen = turtle.Screen()
# setting the screen size
screen.setup(400, 500)
# setting the background color as pink
screen.bgcolor('pink')
# setting the color of the pen to light blue
ttl.pencolor('light blue')
# setting the size of the pen
ttl.pensize(6)
# setting the speed of drawing with the pen
ttl.speed(1.2)
# setting the shape of the pen as turtle
ttl.shape('turtle')
# starting to draw the square
ttl.forward(120)  # top (first) side
ttl.right(90)
ttl.forward(120)  # right (second) side
ttl.right(90)
ttl.forward(120)  # bottom (third) side
ttl.right(90)
ttl.forward(120)  # left (fourth) side

# Printing the heading on the screen
ttl.penup()
ttl.setpos(-100, 90)
ttl.pendown()
ttl.pencolor('white')
ttl.write('Square Animation', font=("Arial", 20, "bold"))
ttl.penup()
ttl.ht()
