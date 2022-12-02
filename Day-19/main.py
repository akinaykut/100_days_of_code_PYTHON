import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

leonardo = Turtle()
donatello = Turtle()
raphael = Turtle()
michelangelo = Turtle()
akin = Turtle()


leonardo.color((51, 153, 255))
donatello.color((204, 0, 255))
raphael.color((255, 0, 0))
michelangelo.color((255, 153, 0))
akin.color((0, 204, 0))
screen = Screen()

# def move_forward():
#     leonardo.forward(20)
#
#
# def move_backward():
#     leonardo.backward(20)
#
#
# def turn_clockwise():
#     leonardo.setheading(leonardo.heading() - 20)
#
#
# def turn_counter_clockwise():
#     leonardo.setheading((leonardo.heading() + 20))
#
#
# def clear_screen():
#     leonardo.reset()
#
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="a", fun=turn_counter_clockwise)
# screen.onkeypress(key="s", fun=move_backward)
# screen.onkeypress(key="d", fun=turn_clockwise)
# screen.onkeypress(key="c", fun=clear_screen)


raphael.penup()
michelangelo.penup()
donatello.penup()
leonardo.penup()
akin.penup()
akin.shape("turtle")
leonardo.shape("turtle")
raphael.shape("turtle")
michelangelo.shape("turtle")
donatello.shape("turtle")
akin.goto(y=0, x=-230)
michelangelo.goto(y=75, x=-230)
leonardo.goto(y=150, x=-230)
raphael.goto(y=-75, x=-230)
donatello.goto(y=-150, x=-230)






screen.setup(width=500, height=400)


