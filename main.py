# This project creates a drawing pad 
# The user gets to select size of pad and turtles, and colors
# The user controls the turtles via left, right, up, and down
# will save the drawing to computer
# using top down design method

import turtle
from turtle import Turtle, Screen, Shape
import tkinter as tk #allows GUI
from tkinter import * 
from tkinter import messagebox
from time import sleep #delays program when needed
turtle.colormode(255) #lets colors to be given as 0 ... 255

shape =((5,-20),(0, 0), (0, 10),(10,10),(10,0))
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
    user.up()
    user.hideturtle()

def show_turtle(user):
    user.down()
    user.showturtle()

def write_Hi(x,y): #function to have turtle write Hi on click
    hide_turtle(user)
    user.goto(-90,45)
    show_turtle(user)
    user.width(10)
    user.speed(3)
    #writes H
    user.left(90)
    user.forward(180)
    user.back(90)
    user.right(90)
    user.forward(90)
    user.left(90)
    user.forward(90)
    user.back(180)
    #writes I
    hide_turtle(user)
    user.right(90)
    user.forward(20)
    show_turtle(user)
    user.forward(90)
    user.back(45)
    user.left(90)
    user.forward(180)
    user.left(90)
    user.forward(45)
    user.back(90)
    hide_turtle(user)
    messagebox.showinfo("Cute!", "check the terminal!")

def sad_face():
    #face
    user.speed(3)
    hide_turtle(user)
    user.goto(-30,-50)
    show_turtle(user)
    user.pencolor(255,213,40)
    user.fillcolor(255,213,40)
    user.begin_fill()
    user.circle(100)
    user.end_fill()
    #eye - right
    hide_turtle(user)
    user.goto(10,50)
    show_turtle(user)
    user.fillcolor('black')
    user.begin_fill()
    user.circle(10)
    user.end_fill()
    #eye - left
    hide_turtle(user)
    user.goto(-70,50)
    show_turtle(user)
    user.fillcolor('black')
    user.begin_fill()
    user.circle(10)
    user.end_fill()
    hide_turtle(user)
    #frown
    user.width(10)
    user.pencolor("black")
    user.goto(10,-20)
    show_turtle(user)
    user.left(90)
    user.circle(40,180)
    hide_turtle(user)

def happy_face():
    #face
    user.speed(3)
    hide_turtle(user)
    user.goto(-30,-50)
    show_turtle(user)
    user.pencolor(255,213,40)
    user.fillcolor(255,213,40)
    user.begin_fill()
    user.circle(100)
    user.end_fill()
    #eye - right
    hide_turtle(user)
    user.goto(10,50)
    show_turtle(user)
    user.fillcolor('black')
    user.begin_fill()
    user.circle(10)
    user.end_fill()
    #eye - left
    hide_turtle(user)
    user.goto(-70,50)
    show_turtle(user)
    user.fillcolor('black')
    user.begin_fill()
    user.circle(10)
    user.end_fill()
    hide_turtle(user)
    #smile
    user.width(10)
    user.pencolor("black")
    user.goto(-70,15)
    show_turtle(user)
    user.right(90)
    user.circle(40,180)
    hide_turtle(user)

def draw(x,y):
    user.ondrag(None)
    user.setheading(user.towards(x,y))
    user.goto(x,y)
    user.ondrag(draw)

def pencil_shape(x,y): 
    user.shape('pencil')
    user.width(3)


def normal_turtle(x,y): #function to have turtle write Hi on click
    user.shape('turtle')

def user_input(yn): 
    while yn == '': #while they don't respond
        yn = input("Sorry did you want to draw?: Y or N: ")
    if yn == 'Y' or yn == 'y' or yn == 'yes': #checks for multiple option
        messagebox.showinfo("Great!", "let's draw")
        user.reset()
        user.clear()
        happy_face()
        user.clear()
    else:
        messagebox.showinfo("Aww okay well that's sad", "but bye I guess ...")
        user.reset()
        user.clear()
        sad_face()
        user.clear()
        hide_turtle(user)
        turtle.bye()

def button_color(colorName,xCord,yCord):
    button = Turtle()
    button.shape('circle')
    button.shapesize(2)
    button.pencolor(colorName)
    button.fillcolor(colorName)
    button.penup()
    button.goto(xCord,yCord)
    button.onclick(blue_onclick)
    button.showturtle()
    return button

def blue_onclick(x,y):
    user.color('cyan')

def black_onclick(x,y):
    user.color(0,0,0)

def red_onclick(x,y):
    user.color('red')

def orange_onclick(x,y):
    user.color('orange')

def yellow_onclick(x,y):
    user.color('yellow')

def green_onclick(x,y):
    user.color('green')

def indigo_onclick(x,y):
    user.color('indigo')

def violet_onclick(x,y):
    user.color('violet')

def undo_button_color(colorName,xCord,yCord):
    button = Turtle()
    button.shape('square')
    button.shapesize(1)
    button.pencolor(colorName)
    button.fillcolor(colorName)
    button.penup()
    button.goto(xCord,yCord)
    button.write("UNDO!", align='center', font=FONT)
    button.sety(yCord + CURSOR_SIZE + FONT_SIZE)
    button.onclick(blue_onclick)
    button.showturtle()
    return button

def undo_drawing(x,y):
    user.undo()

def main():
    welcome_name = getName() #get users name
    win_1 = setUpScreen() #set up screen with user's name in title
    create_pet = createTurtles()

    hide_turtle(create_pet)
    turtle.title(user_name+"'s turtle "+pet_name)  #changes title to turtle name
    show_turtle(create_pet)

    messagebox.showinfo("Hmm it seems " + pet_name + " is shy", "why don't you click on " + pet_name + " to help")
    create_pet.onclick(write_Hi)

    wanna_draw = input("Would you like to draw? Y or N: ")
    user_input(wanna_draw)
    show_turtle(create_pet)

    create_pet.onclick(None) #so it stops writing Hi when clicked 
    create_pet.onclick(pencil_shape)
    create_pet.onrelease(normal_turtle)
    create_pet.speed(0)
    create_pet.ondrag(draw)

    #let user pick color of screen
    black_button = button_color('black',-140,255)
    black_button.onclick(black_onclick)

    red_button = button_color('red', -90,255)
    red_button.onclick(red_onclick)

    orange_button = button_color('orange',-40,255)
    orange_button.onclick(orange_onclick)
    
    yellow_button = button_color('yellow',10,255)
    yellow_button.onclick(yellow_onclick)

    green_button = button_color('green',60,255)
    green_button.onclick(green_onclick)

    blue_button = button_color('cyan',110,255)
    blue_button.onclick(blue_onclick)

    indigo_button = button_color('indigo',160,255)
    indigo_button.onclick(indigo_onclick)

    violet_button = button_color('violet',205,255)
    violet_button.onclick(violet_onclick)

    undo_button = undo_button_color('pink',-200,230)
    undo_button.onclick(undo_drawing)



    #let user right turn to turn turtle, stamp to stamp screen
    #let user save picture
    #let user maybe email?

    
    turtle.done()
    #root.mainloop()
    win_1.mainloop()

if __name__ == "__main__":
    main()
