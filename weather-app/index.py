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

def get_weather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    res = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    print(res)

def main ():
    # turn variables to global
    global textfield

    # create program
    root = Tk()
    root.title("Weather Program")
    root.geometry("900x500+300+200")
    root.configure(bg=dark)
    root_icon = PhotoImage(file="weather-app\icon.png")
    root.iconphoto(False, root_icon)

    # input city
    Label(text="Please provide a city", fg=white, font=("calibri", 20), bg=dark).place(x=330, y=10)
    textfield = tk.Entry(root, justify="center", width=17, font=("Calibri", 21), bg=pink, border=0, fg=black)
    textfield.place(x=300, y=50)
    textfield.focus()
    textfield_button = Button(text="Search", borderwidth=0, cursor="hand2", bg=pink, width=10, height=2, command=get_weather)
    textfield_button.place(x=500, y=50)

    # weather labels
    wind_label = Label(root, text="Wind", font=("Calibri", 16), fg=white, bg=dark)
    wind_label.place(x=120, y=400)

    humidity_label = Label(root, text="Humidity", font=("Calibri", 16), fg=white, bg=dark)
    humidity_label.place(x=220, y=400)

    desc_label = Label(root, text="Description", font=("Calibri", 16), fg=white, bg=dark)
    desc_label.place(x=320, y=400)

    pressure_label = Label(root, text="Pressure", font=("Calibri", 16), fg=white, bg=dark)
    pressure_label.place(x=450, y=400)

    # weather results
    w = Label(text="---", font=("Calibri", 16), bg=dark, fg=white)
    w.place(x= 120, y=430)

    h = Label(text="---", font=("Calibri", 16), bg=dark, fg=white)
    h.place(x= 220, y=430)

    d = Label(text="---", font=("Calibri", 16), bg=dark, fg=white)
    d.place(x= 320, y=430)

    p = Label(text="---", font=("Calibri", 16), bg=dark, fg=white)
    p.place(x= 450, y=430)


    root.mainloop()


if __name__ == '__main__':
    main()