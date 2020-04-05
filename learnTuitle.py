import turtle
import  random

#1
tim = turtle.Turtle()
tim.color("red","blue")  
# tim.pensize(5)
# tim.shape("turtle") 
# tim.forward(100)
# tim.left(90)
# tim.penup()  # Lifts the pen
# tim.forward(100)
# tim.left(90)  
# tim.pendown()  # Puts the pen back down
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.width(5)
#2

# tim.begin_fill()
# tim.circle(50)
# tim.end_fill()  
# tim.begin_fill()
# for x in  range(5):
#     tim.forward(100)
#     tim.right(90)
# tim.end_fill()

#3
# colors = ["red","blue","green","purple","yellow","orange","black"]
# tim = turtle.Turtle()
# tim.color("red","blue")
# for x in range(5):
#     randColor = random.randrange(0,len(colors))
#     rand1 = random.randrange(-300,300)
#     rand2 = random.randrange(-300,300)
#     tim.color(colors[randColor],colors[random.randrange(0,len(colors))])
#     tim.penup()
#     tim.setpos((rand1,rand2))
#     tim.pendown()
#     tim.begin_fill()
#     tim.circle(random.randrange(0,80))
#     tim.end_fill()

#4
# import turtle
# import random

# def up():
#     tim.setheading(90)
#     tim.forward(100)

# def down():
#     tim.setheading(270)
#     tim.forward(100)

# def left():
#     tim.set_heading(180)
#     tim.forward(100)

# def right():
#     tim.setheading(0)
#     tim.forward(100)

# colors = ["red", "blue", "green", "yellow", "black"]

# def clickLeft(x, y):  # Make sure to have parameters x, y
#     tim.color(random.choice(colors))

# def clickRight(x, y):
#     tim.stamp()



# turtle.onscreenclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
# turtle.onscreenclick(clickRight, 3) # 3: Right Mouse Button

# tim.onclick(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
# tim.onclick(down, "Down")
# tim.onclick(left, "Left")
# tim.onclick(right, "Right")

# tim.mainloop()  # This will make sure the program continues to run  
#5
import turtle
from turtle import Screen, Turtle

screen = Screen()
t = Turtle("turtle")
t.speed(-1)

def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight():
    t.clear()

def main():  # This will run the program
    turtle.listen()
    
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  # This will continue running main() 

main()