import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Catch the Turtle Game")
screen.bgcolor("lightblue")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)

# Score variables
score = 0

# Function to move turtle to a random position
def move_turtle():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)

# Function to update score and move the turtle when clicked
def click_turtle(x, y):
    global score
    score += 1
    print(f"Score: {score}")
    move_turtle()

# Move turtle initially and set up click event
move_turtle()
t.onclick(click_turtle)

# Keep the game running
screen.mainloop()