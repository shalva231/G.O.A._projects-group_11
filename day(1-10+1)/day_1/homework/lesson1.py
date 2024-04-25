from turtle import *
shape("turtle")
#we want to make a house




#step 1 square
speed(5)
width(5)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)
end_fill()
#end of square


#door
color("yellow")
begin_fill()
forward(100)
right(90)

forward(60)
right(90)

forward(100)
left(90)
end_fill()
#end of door

penup()
goto(200 , 200)
pendown()

#start of roof
color("red")
begin_fill()
left(135)
forward(141.5)

left(90)
forward(141.5)
end_fill()
#end of roof

penup()
goto(25 , 175)
pendown()

#start of left_windows
color("cyan")
begin_fill()
left(45)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
end_fill()
#end of left_window
 
penup()
goto(175 , 175)
pendown()

#start right_window
color("cyan")
begin_fill()
forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
end_fill()


#end of right_window


penup()
goto(201 , 201)
pendown()
width(5)
color("black")
left(90)

#start outline
forward(201)
left(90)

forward(201)
left(90)

forward(201)
left(90)

forward(201)
left(45)

forward(142)
left(90)

forward(142.5)


penup()
goto(70 , 0)
pendown()
right(45+90)
forward(101)

right(90)
forward(60)

right(90)
forward(100)

penup()
goto(24 , 176)
pendown()

forward(51)
left(90)

forward(51)
left(90)

forward(51)
left(90)

forward(51)


penup()
goto(176 , 176)
pendown()

forward(51)
left(90)

forward(51)
left(90)

forward(51)
left(90)

forward(51)
left(90)

penup()
goto(70+50 , 45)
pendown()
forward(0.1)

penup()
goto(300 , 300)
pendown()

exitonclick()