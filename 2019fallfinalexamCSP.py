#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Isaiah White-Stevens
#Date
# 12/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
Writer = trtl.Turtle()
Writer.shape("circle")
Writer.shapesize(.5)
Writer.speed(0)
#create variables
toggle_pen = 1
pen_size = 1

#tell the user the controls
print("--Controls--")
print("Movement: Arrow Keys")
print("Pensize: P to increase and O to decrease")
print("Toggle pen on or off: U")
print("Change Pen Color: Press C then type name of color into console amd press ENTER")
print("Clear Canvas: Press SPACE")
print("Change the Background Color: Press B and then type the name of the color into the console and press ENTER")
#movement functions
def up():
    Writer.setheading(90)
    Writer.forward(10)

def down():
    Writer.setheading(270)
    Writer.forward(10)

def left():
    Writer.setheading(180)
    Writer.forward(10)

def right():
    Writer.setheading(0)
    Writer.forward(10)


#color/drawing functions
def clearscreen():
    Writer.clear()
    print("Cleared Canvas")
def setpen():
    global toggle_pen   
    
    if (toggle_pen < 1):
        Writer.pendown()
        toggle_pen = 1
        print("Pen Dropped")
    else: 
        Writer.penup()
        toggle_pen = 0
        print("Pen Lifted")

def bigger_pen():
    global pen_size
    pen_size += 1
    Writer.pensize(pen_size)
    print("Pen Size:", pen_size)

def smaller_pen():
    global pen_size
    pen_size -= 1
    Writer.pensize(pen_size)
    print("Pen Size:", pen_size)

def change_color():
    pen_color = input("Type your pen color:")
    Writer.pencolor(pen_color)

def change_background_color():
    back_color = input("Type your background color:")
    wn.bgcolor(back_color)


#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(clearscreen, "space")
wn.onkeypress(setpen, "u")
wn.onkeypress(bigger_pen, "p")
wn.onkeypress(smaller_pen, "o")
wn.onkeypress(change_color, "c")
wn.onkeypress(change_background_color, "b")
#listen
wn.listen()

#mainloop
wn.mainloop()