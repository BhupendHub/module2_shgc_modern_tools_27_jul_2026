#pip install requests
#pip install python-dotenv
import techdev_weather_module as tw
def main():
    print("Type a city name to get live weather, or type 'quit' / 'exit' to close.\n")
    # --- Main Application Loop ---
    while True:
        city = input("Enter city: ").strip()
        if not city:
            continue
        if city.lower() in ['quit', 'exit']:
            print("\nClosing the application. Goodbye!")
            break
        print(f"Fetching live weather for '{city.title()}'...")
        # Fetch data via OpenWeather API (DRY module)
        #temp, desc = Complete this line
        if temp is not None:
            print(f"\nCurrent weather in {city.capitalize()}:")
            print(f"🌡️  Temperature: {temp}°C")
            print(f"☁️  Condition:   {desc}")
if __name__ == "__main__":
    main()
            