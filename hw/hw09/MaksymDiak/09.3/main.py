import tkinter as tk
from tkinter import font
from pyowm import OWM

import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")


owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather():
    place = entry_field.get()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    label[
        "text"
    ] = f"""
    Detailed Status: {w.detailed_status}
    Wind: {w.wind()}
    Humidity: {w.humidity}
    Temperature (Celsius): {w.temperature('celsius')}
    Rain: {w.rain}
    Heat Index: {w.heat_index}
    Clouds: {w.clouds}
    """


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=("Courier", 8),
    command=lambda: get_weather(),
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")


label = tk.Label(lower_frame, font=("Courier", 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
