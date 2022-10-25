import tkinter as tk
from turtle import RawTurtle as rt

def build_root(width, height):
    root = tk.Tk()
    root.title("Webscraper")
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

def draw_background(canvas):
    tt = rt(canvas)

    tt.begin_fill()

    tt.fillcolor("red")
    tt.right(45)
    tt.forward(100)
    tt.right(45)
    tt.forward(100)
    tt.right(90)
    tt.forward(100)
    tt.right(45)
    tt.forward(1000)
    tt.right(45)
    tt.forward(100)
    tt.right(90)
    tt.forward(100)
    tt.right(45)
    tt.forward(900)
    tt.end_fill()

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