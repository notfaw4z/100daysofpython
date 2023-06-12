import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r ,g , b)

tim = Turtle()
tim.shape("arrow")
tim.pensize(15)
tim.speed("fast")


directions = [0, 90, 180, 270]


for _ in range(100):
    tim.fd(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())
