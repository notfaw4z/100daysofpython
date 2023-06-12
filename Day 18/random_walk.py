from turtle import Turtle, Screen
import random

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"]
tim = Turtle()
tim.shape("arrow")
tim.pensize(15)
tim.speed("fast")

movement = [tim.fd(10), tim.bk(100)]
directions = [0, 90, 180, 270]


for _ in range(100):
    tim.fd(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))
