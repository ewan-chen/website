import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle for drawing fireworks
firework = turtle.Turtle()
firework.speed(0)  # Set the drawing speed to the fastest
firework.penup()
firework.color("white")

# Function to draw a firework burst
def draw_firework_burst(x, y):
    firework.goto(x, y)
    firework.pendown()
    for _ in range(36):
        firework.forward(50)
        firework.right(170)
    firework.penup()

# Main fireworks loop
for _ in range(10):  # You can adjust the number of fireworks here
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_firework_burst(x, y)
    screen.update()
    time.sleep(1)  # Delay between fireworks

# Close the window on click
screen.exitonclick()
