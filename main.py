# This project creates a drawing pad 
# The user gets to select size of pad and turtles, and colors
# The user controls the turtles via left, right, up, and down
# will save the drawing to computer
# using top down design method

import turtle
from turtle import Turtle, Screen, Shape
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from time import sleep

turtle.colormode(255)
shape = ((5,-20),(0, 0),(0,10),(10,10),(10,0))
turtle.register_shape('pencil', shape)

CURSOR_SIZE = 20
FONT_SIZE = 10
FONT = ('Arial', FONT_SIZE, 'bold')

def getName():
    global user_name, pet_name
    user_name = turtle.textinput("Hi there!", "What's your name?")
    messagebox.showinfo("Welcome "+ user_name, "let's meet your turtle")
    pet_name = turtle.textinput("But first ... ", "name your turtle")    
    return(user_name,pet_name)

def setUpScreen():
    global wn
    wn = turtle.Screen()
    wn.setup(490,640)
    turtle.title(user_name+"'s turtle")
    wn.bgpic("paper_lined.gif")
    wn.addshape('paper.gif')
    return wn

def createTurtles():
    global user
    user = turtle.Turtle()
    user.shape('turtle')
    return(user)

def hide_turtle(user):
    user.penup()

def show_turtle(user):
    user.pendown()

def draw_face(x, y, color):
    user.speed(3)
    user.penup()
    user.goto(x, y)
    user.pendown()
    user.fillcolor(color)
    user.begin_fill()
    user.circle(100)
    user.end_fill()

def draw_eyes(x, y, color):
    user.fillcolor(color)
    user.begin_fill()
    user.penup()
    user.goto(x, y)
    user.pendown()
    user.circle(10)
    user.end_fill()

def draw_mouth(x, y, color, angle):
    user.width(10)
    user.pencolor(color)
    user.penup()
    user.goto(x, y)
    user.pendown()
    user.setheading(angle)
    user.circle(40, 180)

def sad_face():
    draw_face(-30,-50,(255,213,40))
    draw_eyes(10,50,'black')
    draw_eyes(-70,50,'black')
    draw_mouth(10,-20,'black',90)

def happy_face():
    draw_face(-30,-50,(255,213,40))
    draw_eyes(10

              def select_pen_color():
global pen_color
    pen_color = turtle.askcolor()[1]
    user.pencolor(pen_color)

def select_fill_color():
    global fill_color
    fill_color = turtle.askcolor()[1]
    user.fillcolor(fill_color)

def select_bg_color():
    global bg_color
    bg_color = turtle.askcolor()[1]
    wn.bgcolor(bg_color)

def select_bg_image():
    global bg_image
    bg_image = turtle.filedialog.askopenfilename(title="Choose a background image",
    filetypes=[("GIF files", ".gif"), ("All Files", ".*")])
    wn.bgpic(bg_image)

def save_drawing():
    file_path = turtle.filedialog.asksaveasfilename(defaultextension='.eps')
    user.getcanvas().postscript(file=file_path, colormode='color')

def main():
    getName()
    setUpScreen()
    createTurtles()

# add turtle controls
wn.onkey(lambda: user.setheading(90), "Up")
wn.onkey(lambda: user.setheading(180), "Left")
wn.onkey(lambda: user.setheading(0), "Right")
wn.onkey(lambda: user.setheading(270), "Down")
wn.onkey(select_pen_color, "p")
wn.onkey(select_fill_color, "f")
wn.onkey(select_bg_color, "b")
wn.onkey(select_bg_image, "i")
wn.onkey(save_drawing, "s")
wn.onclick(write_Hi)
wn.onclick(pencil_shape, btn=3)
wn.onclick(normal_turtle, btn=2)
user.ondrag(draw)
sad_face()

# ask user if they want to start drawing
user_input('')

# start listening for events
turtle.listen()
turtle.done()
              
if name == "main":
main()
