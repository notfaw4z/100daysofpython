import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

def draw_line():
    for i in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.fd(50)


tim.penup()
tim.hideturtle()
for i in range(0,500,50):
    tim.setposition(-200.0, -200.0 + i)
    tim.pendown()
    draw_line()
