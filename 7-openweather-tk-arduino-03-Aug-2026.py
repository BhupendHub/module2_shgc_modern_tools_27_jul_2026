import os
import tkinter as tk
import techdev_weather_module as tw
arduino=None
#arduino=Complete this line
if arduino  is None:
    print("Could not connect to Arduino. Please check the connection and try again.")
def fetch_weather():
    city = city_entry.get()
    temp,condition=tw.get_weather(city)  #It gives temperature,weather  
    if temp is None:
        result_label.config(text="Error in Network or API or City")
        return #Terminate Fn
    #Otherwise
    result_label.config(text=f"{temp}°C\n{condition.capitalize()}") 
    #Additional Logic - Send to Arduino
    if arduino and arduino.is_open:
            tw.sendto_arduino(arduino,temp)    
def on_closing(): #What happens when we close window
    if arduino and arduino.is_open:
        arduino.close()
    win.destroy() #Test-2: How to close tkinter window
# Minimal GUI Setup
win = tk.Tk() #Object of Tk class
win.title("TecDev Weather App")
win.geometry("300x250")
win.config(padx=20, pady=20)

tk.Label(win, text="Enter City Name:", font=("Arial", 12)).pack(pady=5)

city_entry = tk.Entry(win, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)

tk.Button(win, text="Get Weather", command=fetch_weather, bg="#4CAF50", fg="white").pack(pady=15)

result_label = tk.Label(win, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)
#Test-2: Register Window close Event
#win.protocol(Complete this line)
win.mainloop()