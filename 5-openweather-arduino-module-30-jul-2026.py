import techdev_weather_module as tw
print("Arduino with Module")


# --- Initialize Serial Connection ---
try:
    arduino=tw.connectto_arduino()
    if arduino  is None:
        print("❌ Could not connect to Arduino. Please check the connection and try again.")
        
    print("Type a city name to get live weather, or type 'quit' / 'exit' to close.\n")

# --- Main Application Loop ---
    while True:
        # 1. Get user input
        city = input("Enter city: ").strip()
        
        # Ignore empty inputs
        if not city:
            continue

        # 2. Check for exit command
        if city.lower() in ['quit', 'exit']:
            print("\nClosing the application. Goodbye!")
            if arduino and arduino.is_open:
                arduino.close()
            break
        print(f"Fetching live weather for '{city.title()}'...")
        
        # 3. Fetch data via OpenWeather API (DRY module)
        temp, desc = tw.get_weather(city)
        
        if temp is not None:
            # 4. Display data to the user
            print(f"🌡️  Temperature: {temp}°C")
            print(f"☁️  Condition:   {desc}")
            
        # 5. Send data to Arduino
        if arduino and arduino.is_open:
            tw.sendto_arduino(arduino,temp)
            
except Exception as e:
    print(f"An unexpected error occurred: {e}")

        