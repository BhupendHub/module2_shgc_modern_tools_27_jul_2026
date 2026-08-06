import serial
import time
import techdev_weather_module as tw
SERIAL_PORT = 'COM7'  # Update to match your Arduino's COM port
BAUD_RATE = 9600
try:
    #arduino = serial.Serial(Complete this line)
    print(f"Arduino connected on {SERIAL_PORT}.")
    time.sleep(2)  # Crucial: Give Arduino 2 seconds to reset after connection
except Exception as e:
    print(f"Could not connect to Arduino: {e}")
    arduino = None

print("Type a city name to get live weather, or type 'quit' / 'exit' to close.\n")
while True:
    city = input("Enter city: ").strip()
    if city.lower() in ['','quit', 'exit']:
        print("\nClosing the application. Goodbye!")
        if arduino and arduino.is_open:
            #Complete this line
            pass
        break
    print(f"Fetching live weather for '{city.title()}'...")
    temp, condition = tw.get_weather(city)    
    if temp is not None:
        print(f"🌡️  Temperature: {temp}°C ☁️  Condition:{condition}")
        if arduino and arduino.is_open:
            try:
                arduino.write(f"{temp}\n".encode('utf-8'))
                print(f"📡 Transmitted {temp}°C to Arduino.")
            except Exception as e:
                print(f" Serial Error: {e}")
    else:
        print(f" Error: Could not find weather data for '{city}'. Check spelling.")