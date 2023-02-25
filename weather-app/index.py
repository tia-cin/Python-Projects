from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from dotenv import load_dotenv
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen


load_dotenv()

API_KEY = os.getenv("API_KEY")

#colors
black = "#17181D"
dark = "#292C35"
orange = "#E09145"
pink = "#FCD9B8"
white = "#E9F4FF"

def get_weather():
    try: 
        city = textfield.get()

        # get location
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        res = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        # get current time of location
        local = pytz.timezone(res)
        local_time = datetime.now(local)
        curr_time = local_time.strftime("%I:%M %p")
        clock.config(text=curr_time)
        name.config(text="Current Weather")

        # request API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

        json_data = requests.get(url).json()
        condition = json_data["weather"][0]["main"]
        desc = json_data["weather"][0]["description"]
        temperature = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=(temperature, "°C"))
        c.config(text=(condition, "|", "feels", "like", temperature, "°C"))

        w.config(text=wind)
        d.config(text=desc)
        p.config(text=pressure)
        h.config(text=humidity)

        city_label = Label(text=city.capitalize(), font=("Calibri", 40), fg=white, bg=dark)
        city_label.place(x=200, y=170)

    except Exception as e:
        messagebox.showerror(f"Weather App", "Invalid Input, please try again")
        print(e)


def main ():
    # turn variables to global
    global textfield
    global name
    global clock

    global t
    global c

    global w
    global h
    global d
    global p

    global root

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

    # current and local info
    name = Label(root, font=("Calibri", 14), bg=dark, fg=white)
    name.place(x=30, y=100)
    clock = Label(root, font=("Calibri", 20), bg=dark, fg=white)
    clock.place(x=30, y=130)

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
    t = Label(font=("Calibri", 60), bg=dark, fg=white)
    t.place(x= 400, y=150)

    c = Label(font=("Calibri", 16), bg=dark, fg=white)
    c.place(x= 400, y=250)

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