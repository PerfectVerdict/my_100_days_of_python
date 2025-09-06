from turtle import Turtle, Screen

t = Turtle()
s = Screen()

t.shapesize(stretch_wid=2, stretch_len=3)  # width x height
t.pensize(5)  # Sets the pen thickness to 5


def forward():
    t.forward(10)


def turn_right():
    t.color("blue")
    t.right(25)


def turn_left():
    t.color("red")
    t.left(25)


def pen_up():
    t.penup()
    print("Pen lifted")  # Debug message


def pen_down():
    t.pendown()
    print("Pen down")  # Debug message


s.listen()
s.onkey(key="Right", fun=turn_right)
s.onkey(key="Left", fun=turn_left)
s.onkey(key="space", fun=forward)
s.onkey(key="Up", fun=pen_up)
s.onkey(key="Down", fun=pen_down)

s.mainloop()  # use mainloop instead of exitonclick
