import turtle

# Create the screen

my_wn = turtle.Screen()

my_wn.bgcolor("lime")

my_wn.title("The Spiral")

# Create the turtle

my_pen = turtle.Turtle()

my_pen.speed(0) # Set the speed to max

size = 1 # Start size

while size < 200: # Adding a stopping condition

    for i in range(4):

        my_pen.forward(size)

my_pen.left(90)


size += 5 # Increase the size for the spiral effect

turtle.done()