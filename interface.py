import tkinter as tk
from turtle import RawTurtle as rt

def build_root(width, height):
    root = tk.Tk()
    root.title("Extract")
    root.iconbitmap('papers.ico')
    root.geometry(str(width) + "x" + str(height))
    root.resizable(False, False)
    return root

def build_frames(root):
    button_frame = tk.LabelFrame(root)
    button_frame.pack(padx=2, pady=5)
    button_frame.place(x=10, y=10)
    return button_frame

def build_canvas(root, width, height):
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    return canvas

def init_turtle(tt):
    tt.up()
    tt.pensize(2)
    tt.speed(10)

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

def draw_background(canvas):
    tt = rt(canvas)
    init_turtle(tt)

    tt.right(45)
    tt.forward(100)
    tt.right(45)
    tt.forward(100)
    tt.left(90)
    draw_crystal(tt, 100, "red", "red")

    tt.back(100)
    tt.right(45)
    tt.forward(300)
    tt.right(45)
    tt.forward(300)
    tt.left(90)
    draw_crystal(tt, 300, "#ffc667", "#ffc667")

def place_buttons(button_frame):
    input_field = tk.Entry(button_frame, width=131, text="Null")
    input_field.pack()
    return input_field

def main():
    width = 1200
    height = 600

    root = build_root(width, height)

    canvas = build_canvas(root, width, height)
    draw_background(canvas)

    button_frame = build_frames(root)
    place_buttons(button_frame)

    root.mainloop()

if __name__ == "__main__":
    main()