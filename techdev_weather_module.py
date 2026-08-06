import requests
import os
from dotenv import load_dotenv
import serial
import time
#import techdev_weather_module as tw
load_dotenv()
# --- Hardware Configuration ---
SERIAL_PORT = 'COM4'  # Update to match your Arduino's COM port
BAUD_RATE = 9600
def connectto_arduino(SERIAL_PORT=SERIAL_PORT,BAUD_RATE=BAUD_RATE):
    try:
        arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Arduino connected on {SERIAL_PORT}.")
        time.sleep(2)  # Crucial: Give Arduino 2 seconds to reset after connection
        return arduino
    except Exception as e:
        print(f"Could not connect to Arduino: {e}")
        return None
    
def sendto_arduino(arduino,temp):
    if arduino and arduino.is_open:
        try:
            # Send the float with a newline character for Arduino's parser
            arduino.write(f"{temp}\n".encode('utf-8'))
            print(f"📡 Transmitted {temp}°C to Arduino.")
        except Exception as e:
            print(f" Serial Error: {e}")

def get_weather(city='bhopal',API_KEY=None):
    if API_KEY is None:
        API_KEY = os.getenv("API_KEY")
    #city = input("Enter city name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url).json()
        
        # Check if the API returned a successful 200 OK status
        if response.get("cod") != 200:
            print("Error: City not found or API issue.")
            return None,None
            
        temp = response["main"]["temp"]
        condition = response["weather"][0]["description"]
        return temp, condition
    except requests.exceptions.RequestException as e:
        print("Network error occurred.")
        return None, None