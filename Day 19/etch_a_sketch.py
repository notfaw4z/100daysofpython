from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.setheading(tim.heading()-10)

def turn_left():
    tim.setheading(tim.heading()+10)

def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)      #Notice no parenthesis here for function - refer higher order function
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
