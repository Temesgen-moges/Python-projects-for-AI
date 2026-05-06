# simple_cli.py - Easy to understand CLI tool
# Save this file and run it from command line

import sys
import random
from datetime import datetime

# ============ FUNCTIONS FOR EACH COMMAND ============

def say_hello():
    """Command 1: Greet the user"""
    print(f"\n👋 Hello! Welcome to CLI Tool!")
    print(f"📅 Today is: {datetime.now().strftime('%A, %B %d, %Y')}")
    print(f"⏰ Current time: {datetime.now().strftime('%H:%M:%S')}")

def roll_dice():
    """Command 2: Roll a dice"""
    number = random.randint(1, 6)
    print(f"\n🎲 You rolled a {number}!")
    
    # Show visual dice
    dice_faces = {
        1: "⚀", 2: "⚁", 3: "⚂",
        4: "⚃", 5: "⚄", 6: "⚅"
    }
    print(f"   {dice_faces[number]}")

def get_temperature():
    """Command 3: Get sample temperature (simulated data)"""
    # Simulate weather data (like your weather API would give)
    temp = random.randint(15, 35)
    humidity = random.randint(40, 90)
    
    print(f"\n🌡️  Current Weather Reading:")
    print(f"   Temperature: {temp}°C")
    print(f"   Humidity: {humidity}%")
    
    # Simple analysis
    if temp > 30:
        print(f"   🔥 It's hot outside!")
    elif temp < 20:
        print(f"   🧥 It's cool outside!")
    else:
        print(f"   👍 Perfect weather!")

def show_help():
    """Show available commands"""
    print("""
╔════════════════════════════════════╗
║     SIMPLE CLI TOOL - HELP         ║
╚════════════════════════════════════╝

COMMANDS:
  hello    - Get a friendly greeting
  dice     - Roll a dice (1-6)
  weather  - Get simulated temperature
  help     - Show this menu
  exit     - Exit the tool

EXAMPLES:
  python simple_cli.py hello
  python simple_cli.py dice
  python simple_cli.py weather
    """)

# # ============ BONUS FUNCTIONS FOR PRACTICE ============

# def roll_advanced_dice():
#     """Bonus: Roll dice with custom number of sides"""
#     # Check if user specified number of sides
#     if len(sys.argv) > 2:
#         try:
#             sides = int(sys.argv[2])
#             if sides < 2:
#                 print("\n❌ Sides must be at least 2!")
#                 return
#             number = random.randint(1, sides)
#             print(f"\n🎲 You rolled a {number} (1-{sides})!")
#         except ValueError:
#             print("\n❌ Please provide a valid number!")
#     else:
#         # Default to 6 sides
#         number = random.randint(1, 6)
#         print(f"\n🎲 You rolled a {number}!")

# def tell_joke():
#     """Bonus: Tell a random joke"""
#     jokes = [
#         ("Why don't scientists trust atoms?", "Because they make up everything!"),
#         ("What do you call a fake noodle?", "An impasta!"),
#         ("Why did the scarecrow win an award?", "He was outstanding in his field!"),
#         ("What do you call a bear with no teeth?", "A gummy bear!"),
#     ]
    
#     joke = random.choice(jokes)
#     print(f"\n😂 {joke[0]}")
#     print(f"   {joke[1]}")

# def get_real_weather():
#     """Bonus: Get real weather using API (if requests is installed)"""
#     try:
#         import requests
#         API_KEY = "1b5adfbcd5fe0288b5a161b9dac2ad00"  # Your API key
#         city = sys.argv[2] if len(sys.argv) > 2 else "bahir dar"
        
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
#             temp = data['main']['temp']
#             humidity = data['main']['humidity']
#             description = data['weather'][0]['description']
            
#             print(f"\n🌍 Real Weather for {city.title()}:")
#             print(f"   Temperature: {temp}°C")
#             print(f"   Humidity: {humidity}%")
#             print(f"   Conditions: {description}")
#         else:
#             print(f"\n❌ Could not get weather for {city}")
#     except ImportError:
#         print("\n❌ Install requests: pip install requests")
#     except Exception as e:
#         print(f"\n❌ Error: {e}")

# ============ MAIN CLI LOGIC ============

# Check if user provided any command
if len(sys.argv) < 2:
    print("\n❌ No command given!")
    print("💡 Try: python simple_cli.py help")
    sys.exit(1)

# Get the command (first argument after script name)
command = sys.argv[1].lower()

# Route to appropriate function
if command == "hello":
    say_hello()
elif command == "dice":
    roll_dice()
elif command == "weather":
    get_temperature()
elif command == "help":
    show_help()
elif command == "exit":
    print("\n👋 Goodbye!")
    sys.exit(0)
# ============ BONUS COMMANDS (Uncomment to use) ============
# elif command == "advdice":
#     roll_advanced_dice()
# elif command == "joke":
#     tell_joke()
# elif command == "realweather":
#     get_real_weather()
else:
    print(f"\n❌ Unknown command: '{command}'")
    print("💡 Type 'help' to see available commands")
    sys.exit(1)

# Successful exit
sys.exit(0)


# # Command_Line_Tools.py
# # A complete CLI tool for weather data - No external dependencies needed!

# import sys
# import json
# import os
# from datetime import datetime

# # Try to import pandas, but provide fallback if not installed
# try:
#     import pandas as pd
#     PANDAS_AVAILABLE = True
# except ImportError:
#     PANDAS_AVAILABLE = False
#     print("⚠️  Note: pandas not installed. Install with: pip install pandas")
#     print("   Basic functionality will still work!\n")

# # Try to import requests for API calls
# try:
#     import requests
#     REQUESTS_AVAILABLE = True
# except ImportError:
#     REQUESTS_AVAILABLE = False
#     print("⚠️  Note: requests not installed. Install with: pip install requests")
#     print("   Weather fetching will not work!\n")

# # ============ CONFIGURATION ============
# API_KEY = "1b5adfbcd5fe0288b5a161b9dac2ad00"  # Your OpenWeatherMap API key
# DEFAULT_CITY = "bahir dar"
# DATA_FILE = "weather_data.json"  # Store all data in one JSON file

# # ============ DATA STORAGE FUNCTIONS ============

# def load_all_data():
#     """Load all weather data from JSON file"""
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, 'r') as f:
#             return json.load(f)
#     return []

# def save_all_data(data):
#     """Save all weather data to JSON file"""
#     with open(DATA_FILE, 'w') as f:
#         json.dump(data, f, indent=4)

# def save_weather_record(city, temperature, humidity, description):
#     """Save a single weather record"""
#     data = load_all_data()
    
#     record = {
#         "city": city,
#         "temperature": temperature,
#         "humidity": humidity,
#         "description": description,
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
    
#     data.append(record)
#     save_all_data(data)
#     print(f"✅ Weather data saved for {city}")

# # ============ WEATHER FUNCTIONS ============

# def get_weather(city=None):
#     """Fetch current weather for a city"""
#     if not REQUESTS_AVAILABLE:
#         print("❌ Cannot fetch weather: requests library not installed")
#         print("   Install with: pip install requests")
#         return
    
#     if city is None:
#         city = DEFAULT_CITY
    
#     print(f"\n🌤️  Fetching weather for {city.title()}...")
    
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
#     try:
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
            
#             # Extract weather info
#             temperature = data['main']['temp']
#             humidity = data['main']['humidity']
#             description = data['weather'][0]['description']
            
#             # Display weather
#             print("\n" + "="*50)
#             print(f"📍 CITY: {city.title()}")
#             print(f"🌡️  TEMPERATURE: {temperature}°C")
#             print(f"💧 HUMIDITY: {humidity}%")
#             print(f"🌤️  CONDITIONS: {description}")
#             print(f"🕐 TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#             print("="*50)
            
#             # Save to storage
#             save_weather_record(city, temperature, humidity, description)
            
#             # Also save to CSV if pandas is available
#             if PANDAS_AVAILABLE:
#                 save_to_csv(city, temperature, humidity, description)
                
#         elif response.status_code == 401:
#             print("❌ Invalid API key! Please check your API_KEY")
#         elif response.status_code == 404:
#             print(f"❌ City '{city}' not found!")
#         else:
#             print(f"❌ Error: Status code {response.status_code}")
            
#     except Exception as e:
#         print(f"❌ Error fetching weather: {e}")

# def save_to_csv(city, temperature, humidity, description):
#     """Save weather data to CSV file"""
#     df = pd.DataFrame([{
#         "city": city,
#         "temperature": temperature,
#         "humidity": humidity,
#         "description": description,
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }])
    
#     filename = f"weather_{city.lower()}.csv"
#     if os.path.exists(filename):
#         df.to_csv(filename, mode='a', header=False, index=False)
#         print(f"📊 Appended to {filename}")
#     else:
#         df.to_csv(filename, index=False)
#         print(f"📊 Created {filename}")

# # ============ ANALYSIS FUNCTIONS ============

# def analyze_data(city=None):
#     """Analyze collected weather data"""
#     data = load_all_data()
    
#     if not data:
#         print("\n❌ No weather data found!")
#         print("   First collect some data: python Command_Line_Tools.py weather")
#         return
    
#     # Filter by city if specified
#     if city:
#         filtered_data = [record for record in data if record['city'].lower() == city.lower()]
#         if not filtered_data:
#             print(f"\n❌ No data found for city: {city}")
#             return
#         data = filtered_data
    
#     # Calculate statistics
#     temperatures = [record['temperature'] for record in data]
#     humidities = [record['humidity'] for record in data]
    
#     avg_temp = sum(temperatures) / len(temperatures)
#     max_temp = max(temperatures)
#     min_temp = min(temperatures)
#     avg_humidity = sum(humidities) / len(humidities)
    
#     # Display analysis
#     print("\n" + "🌡️  WEATHER ANALYSIS SUMMARY")
#     print("="*50)
#     if city:
#         print(f"📍 CITY: {city.title()}")
#     else:
#         print(f"📍 ALL CITIES ({len(set([r['city'] for r in data]))} cities)")
#     print(f"📅 PERIOD: {data[0]['timestamp']} to {data[-1]['timestamp']}")
#     print("-"*50)
#     print(f"📊 AVERAGE TEMPERATURE: {avg_temp:.1f}°C")
#     print(f"📈 HIGHEST TEMPERATURE: {max_temp:.1f}°C")
#     print(f"📉 LOWEST TEMPERATURE: {min_temp:.1f}°C")
#     print(f"💧 AVERAGE HUMIDITY: {avg_humidity:.0f}%")
#     print(f"📝 TOTAL READINGS: {len(data)}")
#     print("="*50)
    
#     # Show recent readings
#     print("\n📋 RECENT READINGS (last 5):")
#     print("-"*50)
#     for record in data[-5:]:
#         print(f"   {record['timestamp']} | {record['city'].title():15} | {record['temperature']:3}°C | {record['humidity']:3}% | {record['description']}")
    
#     # If pandas is available, show more stats
#     if PANDAS_AVAILABLE and len(data) > 1:
#         show_advanced_stats(data)

# def show_advanced_stats(data):
#     """Show advanced statistics using pandas"""
#     df = pd.DataFrame(data)
#     print("\n📊 ADVANCED STATISTICS (pandas):")
#     print("-"*50)
#     print(f"Temperature Standard Deviation: {df['temperature'].std():.2f}°C")
#     print(f"Temperature Median: {df['temperature'].median():.1f}°C")
#     print(f"Temperature Range: {df['temperature'].max() - df['temperature'].min():.1f}°C")

# def show_all_data():
#     """Display all collected weather data"""
#     data = load_all_data()
    
#     if not data:
#         print("\n❌ No data found!")
#         return
    
#     print("\n📚 ALL COLLECTED WEATHER DATA")
#     print("="*80)
#     print(f"{'#':<3} {'City':<15} {'Temperature':<12} {'Humidity':<10} {'Time':<20}")
#     print("-"*80)
    
#     for i, record in enumerate(data, 1):
#         print(f"{i:<3} {record['city'].title():<15} {record['temperature']:>5}°C      {record['humidity']:>3}%      {record['timestamp']:<20}")
    
#     print("="*80)
#     print(f"Total records: {len(data)}")

# def delete_data(city=None):
#     """Delete weather data"""
#     data = load_all_data()
    
#     if not data:
#         print("\n❌ No data to delete!")
#         return
    
#     if city:
#         # Delete specific city
#         original_count = len(data)
#         new_data = [record for record in data if record['city'].lower() != city.lower()]
        
#         if len(new_data) == original_count:
#             print(f"\n❌ No data found for city: {city}")
#             return
        
#         save_all_data(new_data)
#         print(f"\n✅ Deleted {original_count - len(new_data)} record(s) for {city}")
#     else:
#         # Delete all data
#         confirm = input("\n⚠️  Delete ALL weather data? (yes/no): ")
#         if confirm.lower() == 'yes':
#             save_all_data([])
#             print("\n✅ All data deleted!")
#         else:
#             print("\n❌ Deletion cancelled")

# def export_data():
#     """Export data to different formats"""
#     data = load_all_data()
    
#     if not data:
#         print("\n❌ No data to export!")
#         return
    
#     print("\n📤 EXPORT DATA")
#     print("-"*30)
#     print("1. Export to JSON")
#     print("2. Export to CSV")
#     print("3. Export to Text Report")
    
#     choice = input("\nChoose format (1-3): ")
    
#     if choice == '1':
#         # Export to JSON
#         filename = f"weather_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#         print(f"✅ Exported to {filename}")
        
#     elif choice == '2' and PANDAS_AVAILABLE:
#         # Export to CSV
#         filename = f"weather_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
#         df = pd.DataFrame(data)
#         df.to_csv(filename, index=False)
#         print(f"✅ Exported to {filename}")
        
#     elif choice == '3':
#         # Export to text report
#         filename = f"weather_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
#         with open(filename, 'w') as f:
#             f.write("WEATHER DATA REPORT\n")
#             f.write("="*50 + "\n")
#             f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
#             f.write(f"Total Records: {len(data)}\n\n")
            
#             for record in data:
#                 f.write(f"{record['timestamp']} | {record['city']} | {record['temperature']}°C | {record['humidity']}% | {record['description']}\n")
        
#         print(f"✅ Exported to {filename}")
    
#     else:
#         print("❌ Invalid choice or pandas not available")

# # ============ HELP & UTILITY FUNCTIONS ============

# def show_help():
#     """Display help menu"""
#     print("""
# ╔══════════════════════════════════════════════════════════════════╗
# ║                    COMMAND LINE TOOL - HELP MENU                 ║
# ╚══════════════════════════════════════════════════════════════════╝

# 📖 USAGE:
#     python Command_Line_Tools.py <command> [arguments]

# 🎯 AVAILABLE COMMANDS:

#     weather [city]     - Get current weather for a city
#                         Example: python Command_Line_Tools.py weather
#                         Example: python Command_Line_Tools.py weather london

#     analyze [city]     - Analyze collected weather data
#                         Example: python Command_Line_Tools.py analyze
#                         Example: python Command_Line_Tools.py analyze bahir dar

#     list              - Show all collected weather data
#                         Example: python Command_Line_Tools.py list

#     delete [city]     - Delete weather data (specific city or all)
#                         Example: python Command_Line_Tools.py delete
#                         Example: python Command_Line_Tools.py delete london

#     export            - Export data to JSON/CSV/TXT
#                         Example: python Command_Line_Tools.py export

#     help              - Show this help menu
#                         Example: python Command_Line_Tools.py help

#     version           - Show version information

# 💡 TIPS:
#     • Install required libraries: pip install pandas requests
#     • Data is stored in 'weather_data.json' file
#     • CSV files are created for each city automatically

# 🔧 FIRST TIME SETUP:
#     1. Make sure you have an API key from OpenWeatherMap
#     2. Update the API_KEY variable in this script
#     3. Run: python Command_Line_Tools.py weather
#     """)

# def show_version():
#     """Show version information"""
#     print("""
# ╔════════════════════════════════════════════╗
# ║     COMMAND LINE TOOL v2.0                 ║
# ║     Weather Data Collector & Analyzer      ║
# ╚════════════════════════════════════════════╝

# 📦 Features:
#     ✓ Real-time weather fetching
#     ✓ Data persistence (JSON storage)
#     ✓ CSV export with pandas
#     ✓ Data analysis & statistics
#     ✓ Multi-city support
#     ✓ Data export capabilities

# 🔧 Requirements:
#     Python: 3.6+
#     Libraries: requests, pandas (optional)

# 📁 Files created:
#     - weather_data.json (main database)
#     - weather_[city].csv (individual city data)
#     - weather_export_*.json/csv/txt (exports)

# 💻 System Info:
#     Python Version: {sys.version.split()[0]}
#     pandas: {'✓ Installed' if PANDAS_AVAILABLE else '✗ Not installed'}
#     requests: {'✓ Installed' if REQUESTS_AVAILABLE else '✗ Not installed'}
#     """.format(sys=sys))

# # ============ MAIN CLI HANDLER ============

# def main():
#     """Main CLI entry point"""
    
#     # Check if no arguments provided
#     if len(sys.argv) < 2:
#         print("\n❌ No command provided!")
#         print("💡 Type: python Command_Line_Tools.py help")
#         return
    
#     # Get the command (first argument)
#     command = sys.argv[1].lower()
    
#     # Handle commands
#     if command == "weather":
#         # Get city from second argument if provided
#         city = sys.argv[2] if len(sys.argv) > 2 else None
#         get_weather(city)
        
#     elif command == "analyze":
#         city = sys.argv[2] if len(sys.argv) > 2 else None
#         analyze_data(city)
        
#     elif command == "list":
#         show_all_data()
        
#     elif command == "delete":
#         city = sys.argv[2] if len(sys.argv) > 2 else None
#         delete_data(city)
        
#     elif command == "export":
#         export_data()
        
#     elif command == "help":
#         show_help()
        
#     elif command == "version":
#         show_version()
        
#     else:
#         print(f"\n❌ Unknown command: '{command}'")
#         print("💡 Available commands: weather, analyze, list, delete, export, help, version")

# # ============ RUN THE APP ============
# if __name__ == "__main__":
#     print("\n" + "🔧"*20)
#     print("   COMMAND LINE TOOL - Weather Data System")
#     print("🔧"*20)
#     main()
#     print("\n" + "="*50 + "\n")