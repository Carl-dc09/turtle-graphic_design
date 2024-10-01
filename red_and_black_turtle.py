# Import turtle module
from turtle import *
# Import colors
import colorsys

# Set the background color
bgcolor("black")

# Set the drawing speed
tracer(500)

# Set a function to draw
def draw():
    # Set a value for the color transitions
    hue = 0
    # Set the loop
    for iteration in range(100):
        # Convert into RGB color
        colors_ = colorsys.hsv_to_rgb(hue, 1, 1)
        
        hue += 0.5
        up()
        # Position the turtle
        goto(0, 0)
        down()
        # Set the outline color of the shapes
        color("black")
        # Set the fill color to the RGB color
        fillcolor (c)
        # Start the filling of the shape
        begin_fill()
        # Position the turtle
        rt (98)
        # Draw a circle
        circle(i, 12)
