#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: GRACE WILSON
May 29, 2020 - September 4, 2020 (recitation date)
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on.
#The start code has some code written for you, to help you get started quickly. The start code sets the drawing window to 750 x 750 pixels, meaning you have 750 pixels horizontally (x), and 750 pixels vertically (y). Remember, the origin (0,0) is at the center of the picture, so to move to the right, your turtle moves forward 375 pixels, and to the left, you'd move -375 pixels. 

panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on.
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)
#FOR FULL CREDIT, these shapes must:
#To Jeff Bezos' picture, add at least 2 different geometric shapes - this could be a circle, a polygon (+4 sides), and/or a line (or a dot, I hope!)
#2. DONE be drawn at different positions on the screen (you can use goto(x,y) for a specific position, or pick up the pen up() and use forward() and turns (left(), right()) to navigate your turtle) 
#GRAD-point 1 DONE - have different weights (or thicknesses) of the lines
#Grad-point 2 DONE - set at least one color using RGB values.
speed('fastest')
penup()
#starting position
goto(-250,200)
#dash
pendown()
width(10)
forward(20)
#dash to dot
penup()
right(90)
forward(30)
left(90)
forward(10)
pendown()
#first dot
dot(10)
#move to second dot
penup()
forward(25)
pendown()
#second dot
dot(10)
penup()
#big space for new letter
forward(50)
pendown()
#third dot
dot(10)
penup()
forward(25)
pendown()
#fourth dot
dot(10)
penup()
#move to next letter
forward(50)
pendown()
dot(10)
penup()
forward(25)
pendown()
dot(10)
penup()
forward(25)
pendown()
dot(10)
penup()
#dot to dash
forward(10)
left(90)
forward(30)
right(90)
pendown()
width(10)
forward(20)
penup()
#move to next dot spot
forward(50)
right(90)
forward(30)
pendown()
dot(10)
left(90)
penup()
forward(50)
pendown()
dot(10)
penup()
forward(25)
pendown()
dot(10)
penup()
forward(25)
pendown()
dot(10)
penup()
forward(50)
left(90)
forward(30)
right(90)
pendown()
forward(20)
penup()
#Do it again but bigger! 
#Grad-point 1. have different weights (or thicknesses) of the lines
goto(-260,100)
#dash
pencolor(139,0,0) #Grad-point 2 - set at least one color using RGB values.
pendown()
width(15)
forward(25)
#dash to dot
penup()
right(90)
forward(40) #larger space for larger dash
left(90)
forward(10)
pendown()
#first dot
dot(15)
#move to second dot
penup()
forward(25)#no larger space here, looked off
pendown()
#second dot
dot(15)
penup()
#big space for new letter
forward(50)
pendown()
#third dot
dot(15)
penup()
forward(25)
pendown()
#fourth dot
dot(15)
penup()
#move to next letter
forward(50)
pendown()
dot(15)
penup()
forward(25)
pendown()
dot(15)
penup()
forward(25)
pendown()
dot(15)
penup()
#dot to dash
forward(10)
left(90)
forward(40)
right(90)
pendown()
forward(25)
penup()
#move to next dot spot
forward(50)
right(90)
forward(40)
pendown()
dot(15)
left(90)
penup()
forward(50)
pendown()
dot(15)
penup()
forward(25)
pendown()
dot(15)
penup()
forward(25)
pendown()
dot(15)
penup()
forward(50)
left(90)
forward(40)
right(90)
pendown()
forward(25)
penup()
goto(25,-65)
width(2)
#GRAD credit
#0.5 pts - create a 3rd shape
pendown()
color(255,153,0)
begin_fill()
begin_poly()
right(10)
forward(90) #fingertop
right(90)
forward(20) #fingerside
right(90)
forward(23)#fingerlength
left(75)
forward(60)#handlength
right(15)
forward(20) #handbottom1
right(60)
forward(70) #handbottom2
left(60)
forward(15) #wrist1
right(95)
forward(20)#wrist 2
right(30)
forward(30)#wrist3
right(40)
forward(30)#wrist 4
end_poly()
end_fill()
penup()


#

#EXTRA CREDIT - did not do
#0.5 pts - create one unfilled and one filled shape


#For full credit, save your .py file as:
#PC02_Graffiti_YOURLASTNAME_PARTNERLASTNAME.py
#=======Add your code here======
