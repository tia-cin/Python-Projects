from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk

# colors
white = "#EBEBEB"

def main():
    root = Tk()
    root.title("White Board")
    root.geometry("1050x720")
    root.configure(bg=white)
    root.resizable(False, False)

    root.mainloop()

if __name__ == '__main__':
    main()