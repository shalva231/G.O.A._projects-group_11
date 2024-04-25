from turtle import *
shape("turtle")
#we want to make a house


speed(50)




bgcolor("gray")


# Draw 10 scattered yellow stars
x_coordinates = [-800, -600, -400, -200, 0, 200, 400, 600, 800, 1000]
y_coordinates = [300, 350, 310, 390, 330, 365, 340, 380, 395, 305]

# Draw stars at the specified coordinates
penup()
goto(x_coordinates[0], y_coordinates[0])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[1], y_coordinates[1])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[2], y_coordinates[2])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[3], y_coordinates[3])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[4], y_coordinates[4])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[5], y_coordinates[5])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[6], y_coordinates[6])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[7], y_coordinates[7])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[8], y_coordinates[8])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()

penup()
goto(x_coordinates[9], y_coordinates[9])
pendown()
color("yellow")
fillcolor("yellow")
begin_fill()
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
end_fill()


#draw a moon


# Draw a moon
penup()
goto(-350, 200)
pendown()
color("white")
fillcolor("white")
begin_fill()
circle(100)
end_fill()


# Draw ground


penup()
goto(-1000, 0)
pendown()
color("green")
begin_fill()

forward(2000)
right(90)

forward(2000)
right(90)

forward(2000)
right(90)


forward(2000)
end_fill()


#first house


right(90)
#step 1 square
penup()
goto(0 , 0)
pendown()



speed(50)
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
color("brown")
begin_fill()
forward(100)
right(90)

forward(60)
right(90)

forward(100)
left(90)
end_fill()
#end of door

color("purple")
forward(70)
left(90)
forward(200)

#start of roof
color("red")
begin_fill()

left(45)
forward(142.5)

left(90)
forward(142.5)

left(90 + 45)
forward(200)

end_fill()

#end of roof



penup()
goto(-300 , 0)
pendown()

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
color("brown")
begin_fill()
forward(100)
right(90)

forward(60)
right(90)

forward(100)
left(90)
end_fill()
#end of door

color("purple")
forward(70)
left(90)
forward(200)

#start of roof
color("red")
begin_fill()

left(45)
forward(142.5)

left(90)
forward(142.5)

left(90 + 45)
forward(200)

end_fill()
#end of roof



#start of second house

penup()
goto(300 , 0)
pendown()

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
color("brown")
begin_fill()
forward(100)
right(90)

forward(60)
right(90)

forward(100)
left(90)
end_fill()
#end of door

color("purple")
forward(70)
left(90)
forward(200)

#start of roof
color("red")
begin_fill()

left(45)
forward(142.5)

left(90)
forward(142.5)

left(90 + 45)
forward(200)

end_fill()







#outline

penup()
goto(0 , 0)
pendown()



#step 1 square
speed(50)
width(5)
color("black")
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
#end of square


#door
color("black")
forward(100)
right(90)

forward(60)
right(90)

forward(100)
left(90)
#end of door

color("black")
forward(70)
left(90)
forward(200)

#start of roof
color("black")

left(45)
forward(142.5)

left(90)
forward(142.5)

left(90 + 45)
forward(200)


#end of roof



penup()
goto(-300 , 0)
pendown()

color("black")
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
#end of square


#door
color("black")

forward(100)
right(90)

forward(60)
right(90)

forward(100)
left(90)
#end of door

color("black")
forward(70)
left(90)
forward(200)

#start of roof
color("black")

left(45)
forward(142.5)

left(90)
forward(142.5)

left(90 + 45)
forward(200)



penup()
goto(300 , 0)
pendown()

color("black")
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
#end of square


#door
color("black")
forward(100)
right(90)

forward(60)
right(90)

forward(100)
left(90)
#end of door

color("black")
forward(70)
left(90)
forward(200)

#start of roof
color("black")

left(45)
forward(142.5)

left(90)
forward(142.5)

left(90 + 45)
forward(200)



exitonclick()



