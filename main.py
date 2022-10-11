import colorgram
import turtle
import random

tom = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(500, 500)

colors = colorgram.extract(f="image.jpg", number_of_colors=10)

colors_rgb = []

for color in colors:
    colors_rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))

tom.penup()
tom.hideturtle()
x = -225
y = -225
turtle.colormode(255)

for _ in range(10):
    tom.setx(x)
    tom.sety(y)
    for _ in range(10):
        print(tom.dot(20, random.choice(colors_rgb)))
        print(tom.forward(50))
    y += 50

screen.exitonclick()