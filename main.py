import turtle

def draw_flag_bangladesh():
    turtle.speed(3)
    turtle.penup()
    turtle.goto(-320, 100)  # Adjust starting position for side-by-side arrangement
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)  # Smaller size to fit side-by-side
        turtle.right(90)
        turtle.forward(133)  # Smaller height
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-230, 0)  # Correct position for the circle (centered)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(40)  # Circle size
    turtle.end_fill()

def draw_flag_japan():
    turtle.speed(3)
    turtle.penup()
    turtle.goto(-50, 100)  # Adjust starting position for side-by-side arrangement
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)  # Smaller size to fit side-by-side
        turtle.right(90)
        turtle.forward(133)  # Smaller height
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(50, 0)  # Correct position for the circle (centered)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(40)  # Circle size
    turtle.end_fill()

def draw_flag_russia():
    turtle.speed(3)
    colors = ["white", "blue", "red"]
    y = 100
    for color in colors:
        turtle.penup()
        turtle.goto(200, y)  # Adjust starting position for side-by-side arrangement
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(200)  # Smaller size to fit side-by-side
            turtle.right(90)
            turtle.forward(44)  # Smaller height
            turtle.right(90)
        turtle.end_fill()
        y -= 44

def draw_flag_poland():
    turtle.speed(3)
    turtle.penup()
    turtle.goto(450, 100)  # Adjust starting position for side-by-side arrangement
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)  # Smaller size to fit side-by-side
        turtle.right(90)
        turtle.forward(66)  # Smaller height
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(450, 34)  # Adjust the position of the red part
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)  # Smaller size to fit side-by-side
        turtle.right(90)
        turtle.forward(66)  # Smaller height
        turtle.right(90)
    turtle.end_fill()

# Setup screen to run all functions sequentially
def main():
    turtle.bgcolor("gray")  # Set the background to gray
    draw_flag_bangladesh()
    draw_flag_japan()
    draw_flag_russia()
    draw_flag_poland()
    turtle.done()  # Final step to display the drawing

# Start the drawing process
main()
