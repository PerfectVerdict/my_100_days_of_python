from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

screen.bgcolor("black")
t.speed(0)


colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "maroon",
    "navy",
    "olive",
    "teal",
    "lime",
    "indigo",
    "violet",
    "coral",
    "salmon",
    "turquoise",
    "aquamarine",
    "orchid",
    "plum",
    "tan",
    "beige",
    "khaki",
    "lavender",
    "thistle",
    "wheat",
    "ivory",
    "snow",
    "chocolate",
    "tomato",
    "firebrick",
    "crimson",
    "darkred",
    "darkorange",
    "orangered",
    "darkgoldenrod",
    "goldenrod",
    "darkgreen",
    "forestgreen",
    "seagreen",
    "mediumseagreen",
    "springgreen",
    "lawngreen",
    "chartreuse",
    "mediumspringgreen",
    "lightgreen",
    "palegreen",
    "darkcyan",
    "cadetblue",
    "deepskyblue",
    "dodgerblue",
    "royalblue",
    "mediumblue",
    "darkblue",
    "slateblue",
    "mediumslateblue",
    "steelblue",
    "lightsteelblue",
    "powderblue",
    "skyblue",
    "lightskyblue",
    "mediumaquamarine",
    "darkturquoise",
    "mediumturquoise",
    "lightseagreen",
    "midnightblue",
    "darkviolet",
    "darkorchid",
    "mediumorchid",
    "mediumvioletred",
    "deeppink",
    "hotpink",
    "lightpink",
    "palevioletred",
    "rosybrown",
    "indianred",
    "sienna",
    "saddlebrown",
    "peru",
    "burlywood",
    "darkslategray",
    "slategray",
    "lightgray",
    "gainsboro",
    "honeydew",
    "mintcream",
    "azure",
    "aliceblue",
    "ghostwhite",
    "floralwhite",
    "seashell",
    "linen",
    "antiquewhite",
    "bisque",
    "blanchedalmond",
    "lemonchiffon",
    "lightyellow",
    "moccasin",
    "navajowhite",
    "papayawhip",
    "peachpuff",
    "mistyrose",
    "oldlace",
]


def change_facing_direction():
    for i in range(201):
        for i in range(40):
            t.color(random.choice(colors))
            t.left(i)
            t.circle(50)
        t.forward(200)
    for i in range(3):
        t.setheading(90 * i)


change_facing_direction()

screen.exitonclick()
