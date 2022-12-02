import turtle
from turtle import Turtle, Screen
import random
import colorgram
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


tim = Turtle()
tim.speed(0)

directions = [0, 90, 180, 270]


def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)


def random_walk():
    for _ in range(50):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(30)


def draw_spinograph(gape):
    tim.color(random.choice(colors))
    for _ in range(int(360 / gape)):
        tim.circle(10)
        tim.setheading(tim.heading() + gape)


# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

colors = [(253, 251, 248), (254, 250, 252), (231, 251, 242), (198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61), (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169), (78, 234, 201), (50, 234, 244), (3, 66, 40)]


def make_a_dot():
    tim.dot(20, random.choice(colors))


def make_a_space():
    tim.penup()
    tim.forward(50)
    tim.pendown()


def draw_dot_for_line():
    for _ in range(10):
        make_a_dot()
        make_a_space()


def go_up_line():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)
    tim.pendown()


def run():
    for _ in range(10):
        draw_dot_for_line()
        go_up_line()


def tim_start_position():
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    tim.pendown()


tim_start_position()
run()
screen = Screen()
screen.exitonclick()
