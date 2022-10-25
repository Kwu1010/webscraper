"""
Title: interface.py
Developer: Kevin Wu
Description: GUI for taking user input for the webscraper.
"""

import tkinter as tk
from tkinter import scrolledtext
import turtle as tt
from turtle import RawTurtle as rt
import math

"""
Build the root window for the GUI.

@param width is the width of the window
@param height is the height of the window
@return the root window
"""
def build_root(width, height):
    root = tk.Tk()
    root.title("Extract")
    root.iconbitmap('papers.ico')
    root.geometry(str(width) + "x" + str(height))
    root.resizable(False, False)
    return root

"""
Create a frame to house the buttons, labels, and entries for the GUI.

@param root is the root window
@return the button frame
"""
def build_frames(root):
    button_frame = tk.LabelFrame(root)
    button_frame.pack(padx=2, pady=5)
    button_frame.place(x=580, y=280)
    return button_frame

"""
Create the Turtle canvas for a background.

@param root is the root window
@param width is the width of the canvas
@param height is the height of the canvas
@return the canvas
"""
def build_canvas(root, width, height, color):
    canvas = tk.Canvas(root, width=width, height=height)
    tt_screen = tt.TurtleScreen(canvas)
    tt_screen.bgcolor(color)
    canvas.pack()
    return tt_screen

"""
Initialize Turtle.

@param tt is the Turtle pen
@param pen_size is the size of the pen
@param draw_speed is the speed to draw the background
"""
def init_turtle(tt, pen_size, draw_speed):
    tt.up()
    tt.pensize(pen_size)
    tt.speed(draw_speed)

"""
Calculate the hypotenuse of an equilateral triangle given a side.

@param side is the side length of an equilateral right triangle
@return the hypotenuse
"""
def calculate_hypotenuse(side):
    return math.sqrt((side ** 2) * 2)

"""
Draw a crystal shape given a length and color choices.

@param tt is the Turtle pen
@param length is the length of an end edge of the crystal
@param pen_color is the border color of the crystal
@param fill_color is the fill color of the crystal
"""
def draw_crystal(tt, length, pen_color, fill_color):
    tt.color(pen_color)
    tt.fillcolor(fill_color)
    tt.begin_fill()
    tt.down()
    tt.right(180)
    tt.forward(length)
    tt.right(45)
    tt.forward(length * 10)
    tt.right(45)
    tt.forward(length)
    tt.right(90)
    tt.forward(length)
    tt.right(45)
    tt.forward(length * 10)
    tt.right(45)
    tt.forward(length)
    tt.left(90)
    tt.end_fill()
    tt.up()

"""
Draw the title of the GUI on the canvas.

@param tt is the Turtle pen
"""
def draw_title(tt, height, length, spacing, text_color):
    tt.color(text_color)
    tt.fillcolor(text_color)

    long_distance = ((length / 5) * spacing)
    short_distance = ((length / 10) * spacing)
    hypotenuse = calculate_hypotenuse(short_distance)

    # Draw E
    tt.begin_fill()
    tt.down()
    tt.forward(long_distance)
    tt.left(90)
    tt.forward(short_distance)
    tt.left(90)
    tt.forward(short_distance)
    tt.right(90)
    tt.forward(short_distance)
    tt.right(90)
    tt.forward(short_distance)
    tt.left(90)
    tt.forward(short_distance)
    tt.left(90)
    tt.forward(short_distance)
    tt.right(90)
    tt.forward(short_distance)
    tt.right(90)
    tt.forward(short_distance)
    tt.left(90)
    tt.forward(short_distance)
    tt.left(90)
    tt.forward(long_distance)
    tt.left(90)
    tt.forward(short_distance * 5)
    tt.up()
    tt.end_fill()
    tt.left(90)
    tt.forward(long_distance + short_distance)

    # Draw x
    tt.begin_fill()
    tt.down()
    tt.left(45)
    tt.forward(hypotenuse)
    tt.right(90)
    tt.forward(hypotenuse)
    tt.left(45)
    tt.forward(short_distance / 2)
    tt.left(90)
    tt.forward(short_distance)
    tt.left(45)
    tt.forward(hypotenuse)
    tt.right(90)
    tt.forward(hypotenuse)
    tt.left(45)
    tt.forward(short_distance)
    tt.left(90)
    tt.forward(short_distance / 2)
    tt.left(45)
    tt.forward(hypotenuse)
    tt.right(90)
    tt.forward(hypotenuse)
    tt.left(45)
    tt.forward(short_distance / 2)
    tt.left(90)
    tt.forward(short_distance)
    tt.left(45)
    tt.forward(hypotenuse)
    tt.right(90)
    tt.forward(hypotenuse)
    tt.left(45)
    tt.forward(short_distance)
    tt.up()
    tt.end_fill()
    tt.left(90)
    tt.forward(long_distance + short_distance)

    # Draw t

"""
Draw the title background on the canvas.

@param tt is the Turtle pen
"""
def draw_title_background(tt, height, length, spacing, pen_color, text_color, draw_speed):
    tt.color(pen_color)
    tt.speed(0)
    for x in range(length):
        hypotenuse = calculate_hypotenuse(spacing * (x + 1))
        excess_hypotenuse = 0
        if spacing * (x + 1) > (height * spacing):
            difference = (spacing * (x + 1)) - (height * spacing)
            excess_hypotenuse = math.sqrt((difference ** 2) * 2)
        hypotenuse -= excess_hypotenuse
        if x % 2 == 0:
            tt.forward(spacing)
            tt.left(135)
            tt.down()
            tt.forward(hypotenuse)
            tt.up()
            tt.right(45)
            if spacing * (x + 1) <= (height * spacing - spacing):
                tt.forward(spacing)
            tt.right(90)
        else:
            if spacing * (x + 1) > (height * spacing):
                tt.forward(spacing)
            tt.down()
            tt.right(45)
            tt.forward(hypotenuse)
            tt.left(45)
            tt.up()
    if(length % 2 == 0):
        tt.left(90)
        tt.forward((height / 2) * spacing)
        tt.right(90)
        tt.back((length / 2) * spacing)
    else:
        tt.right(90)
        tt.forward((height / 2) * spacing)
        tt.left(90)
        tt.back((length / 3) * spacing)
    draw_title(tt, height, length, spacing, text_color)
    tt.speed(draw_speed)

"""
Draw the background for the GUI.

@param canvas is the canvas to draw the background on
"""
def draw_background(tt_screen, pen_size, draw_speed):
    tt = rt(tt_screen)
    init_turtle(tt, pen_size, draw_speed)

    tt.right(45)
    tt.forward(100)
    tt.right(45)
    tt.forward(100)
    tt.left(90)

    tt.back(100)
    tt.right(45)
    tt.forward(300)
    tt.right(45)
    tt.forward(300)
    tt.left(90)
    draw_crystal(tt, 300, "#ffc667", "#ffc667")

    draw_crystal(tt, 100, "white", "white")

    tt.right(90)
    tt.back(300)
    tt.left(45)
    tt.back(300)
    tt.left(45)
    tt.forward(100)
    draw_crystal(tt, 175, "red", "red")

    tt.left(90)
    tt.forward(200)
    tt.left(90)
    tt.forward(100)
    tt.right(180)
    draw_title_background(tt, 10, 25, 10, "white", "#ffc667", draw_speed)

"""
Create the buttons for the GUI.

@param button_frame is the frame housing the buttons
@return a list with all the buttons
"""
def place_buttons(button_frame):
    buttons = []

    input_field = tk.Entry(button_frame, width=100, text="Search")
    input_field.pack()

    buttons.append(input_field)
    return buttons

"""
Main function calling functions to make the GUI.
"""
def main():
    width = 1200
    height = 600

    pen_size = 2
    draw_speed = 0

    root = build_root(width, height)

    tt_screen = build_canvas(root, width, height, "#444444")
    draw_background(tt_screen, pen_size, draw_speed)

    button_frame = build_frames(root)
    buttons = place_buttons(button_frame)

    root.mainloop()

"""
Main function guard.
"""
if __name__ == "__main__":
    main()