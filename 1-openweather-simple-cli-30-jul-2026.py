#pip install requests
import requests
API_KEY = "6c802fce2ba54d99642485312a7ae189"

def get_weather():
    city = input("Enter city name: ")
    #url=Complete this line
    try:
        #response = Complete this line
        
        # Check if the API returned a successful 200 OK status
        if response.get("cod") != 200:
            print("Error: City not found or API issue.")
            return
            
        #temp = Complete this line
        #condition = Complete this line
        print(f"\nCurrent weather in {city.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition.capitalize()}")
        
    except requests.exceptions.RequestException as e:
        print("Network error occurred.")

if __name__ == "__main__":
    get_weather()