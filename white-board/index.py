from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter

# colors
white = "#EBEBEB"
gray = "#C0C0C0"
blank = "#FAFAFF"

def new_canvas():
    canvas.delete("all")
    colors_palette()

def show_color(new_col):
    global color

    color = new_col

def get_curr_val():
    return "{: .2f}".format(curr_val.get())

def change_slider(ev):
    val_label.configure(text=get_curr_val())

def colors_palette():
    id = colors.create_rectangle((10, 10,30,30), fill="black")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("black"))

    id = colors.create_rectangle((10, 40,30,60), fill="gray")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("gray"))
    
    id = colors.create_rectangle((10, 70,30,90), fill="brown4")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("brown4"))

    id = colors.create_rectangle((10, 100,30,120), fill="red")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("red"))

    id = colors.create_rectangle((10, 130,30,150), fill="orange")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("orange"))

    id = colors.create_rectangle((10, 160,30,180), fill="yellow")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("yellow"))

    id = colors.create_rectangle((10, 190,30,210), fill="green")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("green"))

    id = colors.create_rectangle((10, 220,30,240), fill="blue")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("blue"))

    id = colors.create_rectangle((10, 250,30,270), fill="purple")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("purple"))

    id = colors.create_rectangle((10, 280,30,300), fill="pink")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("pink"))

    id = colors.create_rectangle((10, 310,30,330), fill="white")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("white"))


def locale_xy(work):
    global curr_x, curr_y

    curr_x = work.x
    curr_y = work.y


def add_line(work):
    global curr_x, curr_y

    canvas.create_line((curr_x, curr_y, work.x, work.y), width=get_curr_val(), fill=color, capstyle=ROUND, smooth=TRUE)
    curr_x, curr_y = work.x, work.y

def main():
    global colors, canvas, curr_x, curr_y, color, curr_val, val_label

    # program set up
    root = Tk()
    root.title("White Board")
    root.geometry("1050x620")
    root.configure(bg=white)
    root.resizable(False, False)

    # variables
    curr_x = 0
    curr_y = 0
    color = "black"

    # tools bar
    Canvas(root, bg=gray, width=80, height=520).place(x=20, y=20)

    # eraser
    eraser = Button(root, text="Eraser", bg=gray, command=new_canvas)
    eraser.place(x=40, y=500)

    # color palette
    colors = Canvas(root, bg="#fff", width=40, height=340, bd=0)
    colors.place(x=40, y=60)

    colors_palette()

    # white board
    canvas = Canvas(root, bg=blank, width=890, height=570, cursor="hand2")
    canvas.place(x=130, y=20)
    canvas.bind("<Button-1>", locale_xy)
    canvas.bind("<B1-Motion>", add_line)


    # drawing width change
    curr_val = tkinter.DoubleVar()

    slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=change_slider, variable=curr_val)
    slider.place(x=20, y=560)

    val_label = ttk.Label(root, text=get_curr_val())
    val_label.place(x=20, y=585)

    root.mainloop()

if __name__ == '__main__':
    main()