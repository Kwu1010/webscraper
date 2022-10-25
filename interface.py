import turtle as tt
import tkinter as tk

def initialize_turtle():
    tt.setup(800, 600)
    tt.up()
    tt.title("Webscraper")
    tt.pensize(2)
    tt.speed(2)

def draw_background_design():
    tt.begin_fill()
    for x in range(4):
        tt.forward(100)
        tt.right(90)
    tt.end_fill()

def place_buttons(canvas, screen):
    button = tk.Button(canvas.master, text="Press me", command=press)
    canvas.create_window(screen.window_width() / 2, screen.window_height() / 2, window=button)

def press():
    print("test")

def main():
    initialize_turtle()
    screen = tt.Screen()
    screen.bgcolor("white")
    draw_background_design()

    canvas = screen.getcanvas()
    place_buttons(canvas, screen)

    tt.done()

if __name__ == "__main__":
    main()