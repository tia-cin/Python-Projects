from tkinter import *
from tkinter import messagebox
import pybase64
import os

def main():
    screen=Tk()
    screen.geometry("530x400") # program size
    
    # program icon and name
    icon = PhotoImage(file="encryption-decryption\icon.png")
    screen.iconphoto(False, icon)
    screen.title("SafeCrypting")

    # reset function (clear all inputs)
    def reset():
        code.set("")
        text1.delete(1.0, END)
    
    # app content
    Label(text="Please provide text for encryption or decryption", fg="#100e34", font=("calibri", 18)).place(x=10, y=10)

    text1 = Text(font="Robote 14", bg="#fff", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=510, height=100)

    Label(text="Please enter KEY for encryption and decryption", fg="#100e34", font=("calibri", 12)).place(x=110, y=170)

    code = StringVar()
    Entry(textvariable=code, width=17, bd=0, font=("Arial", 25), show="*").place(x=110, y=200)

    Button(text="ENCRYPT", height="2", width=20, bg="#4f48ec", fg="#fff", bd=0).place(x=80, y=250)
    Button(text="DECRYPT", height="2", width=20, bg="#ffbf18", fg="#fff", bd=0).place(x=303, y=250)
    Button(text="RESET", height="2", width=52, bg="#100e34", fg="#fff", bd=0, command=reset).place(x=80, y=300)

    screen.mainloop()

if __name__ == "__main__":
    main()