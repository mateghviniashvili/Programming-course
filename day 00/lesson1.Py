from turtle import *

#we want to paint a house

#step 1: draw a square
shape("turtle")     
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#drawing a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)      #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("purple")
left(30)
forward(50)
left(90)

color("green")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

color("purple")
forward(50)
right(90)
forward(200)
right(90)
begin_fill()
forward(50)
right(90)
color("green")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()