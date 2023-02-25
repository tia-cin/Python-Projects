from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#colors
black = "#17181D"
dark = "#292C35"
orange = "#E09145"
pink = "#FCD9B8"
white = "#E9F4FF"

def main ():
    # create program
    root = Tk()
    root.title("Weather Program")
    root.geometry("900x500+300+200")
    root.configure(bg=dark)
    root_icon = PhotoImage(file="weather-app\icon.png")
    root.iconphoto(False, root_icon)

    # input city
    textfield = tk.Entry(root, justify="center", width=17, font=("Calibri", 21), bg=pink, border=0, fg=black)
    textfield.place(x=50, y=50)
    textfield.focus()

    textfield_button = Button(text="Search", borderwidth=0, cursor="hand2", bg=pink, width=10, height=2)
    textfield_button.place(x=250, y=50)


    root.mainloop()


if __name__ == '__main__':
    main()