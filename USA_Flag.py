#!/usr/bin/env python

# Author: Omer Abdulaziz
# ID: ETS0988/10
# Group: 6
# Section: D
# Submitted to: Eyob Samuel

# Graphics Assignment - Drawing the flag of United States of America (USA)

from py_graphics import *

win_height = 480
win_width = 640

win = GraphWin('Flag of United States of America', win_width, win_height)
win.setBackground("white")

def draw_star(x: float = 0, y: float = 0, scale: float = 1, color = "black"):
    init_x = [ 7, 9, 14, 10, 11, 7 ,3 ,4 ,0, 5 ]
    init_y = [ 0, 5, 5, 8, 13, 10, 13, 8, 5, 5 ]

    pts = []
    for i in range(0,len(init_y)):
        pts.append(Point((init_x[i] + x) * scale, (init_y[i] + y) * scale))

    pl = Polygon(pts)
    pl.setFill(color)
    pl.setOutline(color)
    return pl

red_bar_height = win_height / 13
red_shade = color_rgb(187, 19, 62)

for i in range(0, 13):
    if i % 2 == 0:
        red_rec = Rectangle(Point(0,red_bar_height*i), Point(win_width, (red_bar_height*i) + red_bar_height))
        red_rec.setFill(red_shade)
        red_rec.setOutline(red_shade)
        red_rec.draw(win)

blue_shade = color_rgb(0, 38, 100)

blue_rec = Rectangle(Point(0,0), Point(300, red_bar_height*7))
blue_rec.setFill(blue_shade)
blue_rec.setOutline(blue_shade)
blue_rec.draw(win)

for j in range(0, 4):
    for i in range(0, 6):
        draw_star((i*28) + 5, 5 + (j * 30), scale=1.8, color="white").draw(win)

    for i in range(0, 5):
        draw_star((i*28) + 20, 20 + (j * 30), scale=1.8, color="white").draw(win)

for i in range(0, 6):
    draw_star((i*28) + 5, 5 + (4 * 30.1), scale=1.8, color="white").draw(win)

win.getMouse()
win.close()
