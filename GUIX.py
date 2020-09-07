# GUI-X is a simple Snake Game written in Python 3
# By RPM

import turtle
import time

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("GUI-X Game by RPM")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Functions
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)


def move():
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)


def move():
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "i")
wn.onkeypress(go_down, "k")
wn.onkeypress(go_left, "j")
wn.onkeypress(go_right, "l")

# Main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()
