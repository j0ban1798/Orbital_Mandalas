# Patrick Schassberger
# CSCI 101 - Section C
# Create - Mandala


import turtle
import math
import sys

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# interface


print(
    "Hello!!! \nAnd welcome to our solar system!\nWe will be using turtle and a little bit of math to trace some beautiful mandala patterns made by our planets and their orbits!")
print("Our planets are as follows:\n- Mercury\n- Venus\n- Earth\n- Mars\n- Jupiter\n- Sarturn\n- Uranus\n- Neptune")
(a, b) = input("Please enter your two favorite planets in our system:\n> ").split()
a = a.capitalize()
b = b.capitalize()
while (a or b) not in (planet_list):
    (a, b) = input("Error, please enter two valid planets from our solar system:\n> ").split()
    a = a.capitalize()
    b = b.capitalize()
time = int(input("Enter how many years you would like to plot:\n> "))
print("\nPlease enjoy the following animation.")

# my graphics window
my_screen = turtle.Screen()
my_screen.setup(1000, 1000)
my_screen.bgcolor("black")


# creating my objects(planets)
def sol():
    sol = turtle.Turtle()
    sol.shape("circle")
    sol.color("yellow")
    sol.shapesize(5, 5)
    sol.setpos(0, 0)


# Mercury
def mercury():
    mercury = turtle.Turtle()
    mercury.penup()
    mercury.speed(100)
    mercury.goto(60, 0)
    mercury.pendown()
    mercury.shape("circle")
    mercury.color("chocolate")
    mercury.shapesize(0.8, 0.8)
    origin = 60
    deg = 3

    return mercury, deg, origin


# Venus
def venus():
    venus = turtle.Turtle()
    venus.penup()
    venus.speed(100)
    venus.goto(100, 0)
    venus.pendown()
    venus.shape("circle")
    venus.color("gold")
    venus.shapesize(1, 1)
    origin = 100
    deg = 1.7

    return venus, deg, origin


# earth
def earth():
    gaia = turtle.Turtle()
    gaia.penup()
    gaia.speed(80)
    gaia.goto(160, 0)
    gaia.pendown()
    gaia.shape("circle")
    gaia.color("skyblue")
    gaia.shapesize(1.3, 1.3)
    origin = 160
    deg = 1

    return gaia, deg, origin


# mars
def mars():
    mars = turtle.Turtle()
    mars.penup()
    mars.speed(80)
    mars.goto(225, 0)
    mars.pendown()
    mars.shape("circle")
    mars.color("maroon")
    mars.shapesize(1.3, 1.3)
    origin = 225
    deg = 0.5

    return mars, deg, origin


# jupiter
def jupiter():
    jupiter = turtle.Turtle()
    jupiter.penup()
    jupiter.speed(80)
    jupiter.goto(300, 0)
    jupiter.pendown()
    jupiter.shape("circle")
    jupiter.color("gold")
    jupiter.shapesize(3.5, 3.5)
    origin = 300
    deg = 0.08

    return jupiter, deg, origin


# saturn
def saturn():
    saturn = turtle.Turtle()
    saturn.penup()
    saturn.speed(80)
    saturn.goto(350, 0)
    saturn.pendown()
    saturn.shape("circle")
    saturn.color("brown")
    saturn.shapesize(3, 3)
    origin = 350
    deg = 0.03

    return saturn, deg, origin


# uranus
def uranus():
    uranus = turtle.Turtle()
    uranus.penup()
    uranus.speed(80)
    uranus.goto(440, 0)
    uranus.pendown()
    uranus.shape("circle")
    uranus.color("turquoise")
    uranus.shapesize(2.8, 2.8)
    origin = 440
    deg = 0.011

    return uranus, deg, origin


# neptune
def neptune():
    neptune = turtle.Turtle()
    neptune.penup()
    neptune.speed(80)
    neptune.goto(600, 0)
    neptune.pendown()
    neptune.shape("circle")
    neptune.color("blue")
    neptune.shapesize(2.8, 2.8)
    origin = 600
    deg = 0.006

    return neptune, deg, origin


# create motion being multiplied by sine cosine by increments
def A_motion(planet, deg, origin):  # updates x and y positions over time
    x_pos = origin * math.cos(deg)
    y_pos = origin * math.sin(deg)
    planet.goto(x_pos, y_pos)
    a_pos = (x_pos, y_pos)

    return a_pos


def B_motion(planet, deg, origin):  # updates x and y positions over time
    x_pos = origin * math.cos(deg)
    y_pos = origin * math.sin(deg)
    planet.goto(x_pos, y_pos)
    b_pos = (x_pos, y_pos)

    return b_pos


# update position and drawing a line between the two planets
def line(a_pos, b_pos):  # updates x and y positions over time
    line = turtle.Turtle()
    line.color("white")
    line.speed(100)
    line.hideturtle()
    line.penup()
    line.goto(a_pos)
    line.pendown()
    line.goto(b_pos)
    line.penup()


# Making it happen

# if game picking a planet
if a == "Mercury":
    (planet_a, deg_a, origin_a) = mercury()
if a == "Venus":
    (planet_a, deg_a, origin_a) = venus()
if a == "Earth":
    (planet_a, deg_a, origin_a) = earth()
if a == "Mars":
    (planet_a, deg_a, origin_a) = mars()
if a == "Jupiter":
    (planet_a, deg_a, origin_a) = jupiter()
if a == "Saturn":
    (planet_a, deg_a, origin_a) = saturn()
if a == "Uranus":
    (planet_a, deg_a, origin_a) = uranus()
if a == "Neptune":
    (planet_a, deg_a, origin_a) = neptune()

if b == "Mercury":
    (planet_b, deg_b, origin_b) = mercury()
if b == "Venus":
    (planet_b, deg_b, origin_b) = venus()
if b == "Earth":
    (planet_b, deg_b, origin_b) = earth()
if b == "Mars":
    (planet_b, deg_b, origin_b) = mars()
if b == "Jupiter":
    (planet_b, deg_b, origin_b) = jupiter()
if b == "Saturn":
    (planet_b, deg_b, origin_b) = saturn()
if b == "Uranus":
    (planet_b, deg_b, origin_b) = uranus()
if b == "Neptune":
    (planet_b, deg_b, origin_b) = neptune()

i = 0
sol()
for k in range(time * 64):
    a_pos = A_motion(planet_a, i * deg_a, origin_a)
    b_pos = B_motion(planet_b, i * deg_b, origin_b)
    line(a_pos, b_pos)
    i += 0.1

sys.exit()