from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def drawShape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(4)
        tim.right(angle)


for shape_side_n in range(10, 101):
    drawShape(shape_side_n)


screen.exitonclick()
