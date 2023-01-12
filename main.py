# This project creates a drawing pad 
# The user gets to select size of pad and turtles, and colors
# The user controls the turtles via left, right, up, and down
# will save the drawing to computer
# using top down design method

import turtle
import tkinter as tk #allows GUI
from tkinter import messagebox
from time import sleep
turtle.colormode(255) #lets colors to be given as 0 ... 255

def getName():
    global user_name, pet_name
    #user_name = input("Hi there! What's your name? ")
    user_name = turtle.textinput("Hi there!", "What's your name?")
    sleep(.50)
    print("Cool name! ", user_name)
    sleep(.50)
    print("Welcome", user_name, "let's meet your turtle")
    sleep(.50)
    print("But first ...")
    sleep(.50)
    pet_name = turtle.textinput("Please name your turtle: ", "turtle")    
    return(user_name,pet_name)

def setUpScreen():
    global wn
    wn = turtle.Screen()
    wn.setup(490,640)
    turtle.title(user_name+"'s turtle")
    wn.bgpic("paper_lined.gif")
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

def introduce_turtle():
    sleep(.50)
    print('Please meet', pet_name)
    sleep(.50)
    print('Ahm ... please meet', pet_name)
    sleep(.50)
    print('...')
    sleep(.50)

def move_Screen(yesNo): #tells user to move the screen
    while yesNo == '': #while they don't respond
        yesNo = input('Sorry did you move the screen?, Y or N: ')
    if yesNo == 'Y' or yesNo == 'y' or yesNo == 'yes': #checks for multiple option
        print("That's better! Now, meet ", pet_name)
    else:
        print("Sorry but you have to move the screen to see ", pet_name, "!")

def next_steps():
    sleep(.50)
    print('...')
    sleep(.50)
    print(pet_name, "your friend ", user_name, "is trying to say hi")
    print('Hmm it seems', pet_name, 'is shy')
    sleep(.50)
    print("why don't you click on ", pet_name, "to help", pet_name, "say hi")
    sleep(.50)

def print_slow(): #Prints the text letter by letter like in old fashion games
    phrase = input("Enter a phrase: ")
    words = phrase.split()  # ['I', 'need', 'practice']
    for word in words:
        sleep(.5)
        for i in word:
            print(i, end=" ") #keeps it on the same line
    return()

#function to have turtle write Hi on click
def write_Hi(x,y):
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

def sad_face():
    #face
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

def user_input(yn): 
    while yn == '': #while they don't respond
        yn = turtle.textinput("Sorry did you want to draw?","Y or N:")
    if yn == 'Y' or yn == 'y' or yn == 'yes': #checks for multiple option
        print("Great! let's draw! ", pet_name)
        user.reset()
        user.clear()
        happy_face()
        user.clear()
    else:
        print("Aww okay well that's sad but bye I guess ...")
        user.reset()
        user.clear()
        sad_face()
        #close screen

def main():
    welcome_name = getName() #get users name
    win_1 = setUpScreen() #set up screen with user's name in title
    create_pet = createTurtles()
    hide_turtle(create_pet)
    turtle.title(user_name+"'s turtle "+pet_name)  #changes title to turtle name
    introduce_turtle()
    show_turtle(create_pet)
    print('Hmm it seems the screen is hidden, why not moving it in order to see '+ pet_name)
    tell_them_to_move = input('Did you move the screen Y or N: ')
    move_Screen(tell_them_to_move) #tells user to move the screen
    next_steps() #message explaining next steps
    create_pet.onclick(write_Hi)
    #create way to make them wait
    wanna_draw = turtle.textinput("Would you like to draw?", "Y or N: ")
    user_input(wanna_draw)
    show_turtle(create_pet)
    create_pet.onclick(None)
    #create on click turns into pen
    create_pet.speed(0)
    create_pet.ondrag(draw)
    messagebox.showinfo("showinfo", "Information")
    #let user pick color of turtle
    #let user pick color of screen
    #let user right turn to turn turtle, stamp to stamp screen
    #change color click change color
    #to finish click done
    #let user save picture
    #let user maybe email?
    turtle.done()
    win_1.mainloop()

if __name__ == "__main__":
    main()
