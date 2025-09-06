import turtle as t
import colorgram
# import random

# screen = t.Screen()
# screen.colormode(255)  # Allow RGB tuples with 0-255 values


color_list = [
    (32, 23, 3),
    (9, 24, 4),
    (145, 93, 17),
    (11, 14, 38),
    (88, 82, 10),
    (44, 13, 29),
]

# tim = t.Turtle()
# tim.penup()  # don't draw while moving to start position
# tim.speed(0)
# screen.bgcolor("black")

# Bottom-left quadrant center
# start_x = -screen.window_width() / 4
# start_y = -screen.window_height() / 4
# tim.goto(start_x, start_y)
#
# dots_per_row = 10
# dot_size = 20
# spacing = 40
# rows = 10
#
# for row in range(rows):
#     for _ in range(dots_per_row):
#         tim.dot(dot_size, random.choice(color_list))
#         tim.forward(spacing)
#
#     tim.goto(start_x, tim.ycor() + spacing)
#

# Extract 6 colors from an image.
colors = colorgram.extract("1-astronaught.png", 6)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
# screen.exitonclick()
