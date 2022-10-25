import turtle as tt
import tkinter as tk

def press():
    pass

def main():
    screen = tt.Screen()
    tt.forward(100)
    screen.bgcolor("white")
    canvas = screen.getcanvas()
    button = tk.Button(canvas.master, text="Press me", command=press)
    canvas.create_window(-200, -200, window=button)
    tt.done()

if __name__ == "__main__":
    main()