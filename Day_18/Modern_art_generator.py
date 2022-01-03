import turtle as t
import random
import colorgram


def rgb_color_extractor():
    for color in range(0,len(colors)):
        rgb = colors[color].rgb
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        rgb_colors.append((red, green, blue))
    return rgb_colors

def canvas_size(rows, columns):
    for y in range(-rows*25, rows*25, 50):
        painting.sety(y)
        for x in range(-columns*25, columns*25, 50):
            painting.setx(x)
            rgb_colors = rgb_color_extractor()
            painting.color(random.choice(rgb_colors))
            painting.dot(15)


painting = t.Turtle()
painting.shape("blank")
painting.penup()
painting.speed(0)
t.colormode(255)

colors = colorgram.extract('paint_pallet.jpg', 25)
rgb_colors = []

rows = int(input("How many rows do you want your painting to have?"))
columns = int(input("How many columns do you want your painting to have?"))
canvas_size(rows, columns)

canvas = t.Screen()
canvas.exitonclick()
