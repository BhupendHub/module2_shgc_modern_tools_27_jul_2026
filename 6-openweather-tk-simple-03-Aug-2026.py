import os
#import requests
import tkinter as tk
#from dotenv import load_dotenv
#import tkinter.font as tkFont
import techdev_weather_module as tw
#load_dotenv()
#API_KEY = os.getenv("tecdev_weather")

def fetch_weather():
    city = city_entry.get()
    temp,condition=tw.get_weather(city)    
    if temp is None:
        result_label.config(text="Error in Network or API or City")
        return
    
    result_label.config(text=f"{temp}°C\n{condition.capitalize()}")     
# Minimal GUI Setup
win = tk.Tk()
win.title("Weather App")
win.geometry("300x250")
win.config(padx=20, pady=20)

tk.Label(win, text="Enter City Name:", font=("Arial", 12)).pack(pady=5)

city_entry = tk.Entry(win, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)

tk.Button(win, text="Get Weather", command=fetch_weather, bg="#4CAF50", fg="white").pack(pady=15)

result_label = tk.Label(win, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

win.mainloop()