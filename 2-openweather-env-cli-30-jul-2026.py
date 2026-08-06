#pip install requests
#pip install python-dotenv
import requests
import os
#from dotenv import Complete this line
load_dotenv()
print("Loaded From .env")
API_KEY = os.getenv("API_KEY")

def get_weather():
    city = input("Enter city name: ")
    #url=Complete this line
    try:
        #response=Complete this line
        
        # Check if the API returned a successful 200 OK status
        if response.get("cod") != 200:
            print("Error: City not found or API issue.")
            return
            
        temp = response["main"]["temp"]
        condition = response["weather"][0]["description"]
        
        print(f"\nCurrent weather in {city.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition.capitalize()}")
        
    except requests.exceptions.RequestException as e:
        print("Network error occurred.")

if __name__ == "__main__":
    get_weather()