import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(5)  # Adjust speed
t.penup()

# Define the coordinates for the pattern
positions = [
    (4, 100), (3, 80), (2, 60), (1, 40), (0, 20),  # Upper part
    (1, 0), (2, -20), (3, -40), (4, -60)          # Lower part
]

# Draw the pattern
for x, y in positions:
    t.goto(x * 20, y)  # Move to position
    t.dot(10, "black")  # Draw a dot representing '*'

# Hide the turtle and display
t.hideturtle()
turtle.done()