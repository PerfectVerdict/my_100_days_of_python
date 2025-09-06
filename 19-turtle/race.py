from turtle import Turtle, Screen
import random

s = Screen()

s.setup(width=500, height=400)


class Racer:
    def __init__(self, color, y_position):
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x=-230, y=y_position)

    def move_forward(self, distance):
        self.turtle.forward(distance)


# the fallowing are racers
def starting_position():
    return [
        Racer("red", y_position=-150),
        Racer("orange", y_position=-100),
        Racer("yellow", y_position=-50),
        Racer("green", y_position=0),
        Racer("blue", y_position=50),
        Racer("violet", y_position=100),
    ]


racers = starting_position()

user_bet = s.textinput(
    title="make your bet", prompt="Which turtle will win the race? Enter a color: "
)

# race loop

race_on = True
finish_line = 230

while race_on:
    for racer in racers:
        step = random.randint(1, 10)
        racer.move_forward(step)
        if racer.turtle.xcor() >= finish_line:
            race_on = False
            winning_color = racer.turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle was the winner")
            else:
                print(f"You lost! The {winning_color} turtle was the winner")
            break

s.mainloop()
