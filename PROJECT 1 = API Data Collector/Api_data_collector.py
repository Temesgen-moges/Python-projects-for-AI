import requests  # Library to "ask" websites for data (like a web browser in code)
import json      # Built-in tool to read/write JSON format (API data is usually JSON)
import pandas as pd  # Library for tables/dataframes (makes CSV easy)
from datetime import datetime  # Built-in for current date/time

# Your settings: Change these!
API_KEY = "1b5adfbcd5fe0288b5a161b9dac2ad00"  # Free key from openweathermap.org
CITY = "bahir dar"                # Your city name
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
# f-string: Glues CITY and API_KEY into the URL dynamically

# Fetch the data
response = requests.get(URL)  # Sends request, gets back a "response object"
if response.status_code == 200:  # 200 means "success!" (like HTTP OK)
    data = response.json()     # Converts raw response to Python dict/list
    
    # Add timestamp for tracking when fetched
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["timestamp"] = timestamp
    
    # Save as JSON file (human-readable)
    with open(f"weather_{CITY.lower()}.json", "w") as f:
        json.dump(data, f, indent=4)  # Writes dict to file, pretty-formatted
    print("✅ Saved to JSON!")
    
    # Save as CSV (easy for Excel/pandas analysis)
    df = pd.DataFrame([{
        "city": CITY,
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "timestamp": timestamp
    }])
    df.to_csv(f"weather_{CITY.lower()}.csv", index=False)  # Saves table to CSV
    print("✅ Saved to CSV!")
else:
    print(f"❌ Error: {response.status_code}")  # Handles failures (e.g., bad key)
