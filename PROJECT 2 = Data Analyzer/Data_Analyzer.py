import pandas as pd
import glob
import os
from datetime import datetime

# Option A: Specify the exact path to your collector's folder
# COLLECTOR_FOLDER = r"C:\Users\YourName\Documents\weather_collector" 
COLLECTOR_FOLDER = r"C:\Users\temu1\OneDrive\Desktop\python projects for ai\PROJECT 1 = API Data Collector"  # Windows
# COLLECTOR_FOLDER = "/home/username/weather_collector"  # Mac/Linux

# Or use relative path (if analyzer is in a subfolder)
# COLLECTOR_FOLDER = "../weather_collector"  # Go up one level then into collector folder

def analyze_weather_data(csv_filename=None):
    """
    Analyze temperature data from your weather collector's CSV files
    """
    
    # Change to collector's directory
    if csv_filename is None:
        # Look for CSV files in the collector's folder
        search_pattern = os.path.join(COLLECTOR_FOLDER, "weather_*.csv")
        csv_files = glob.glob(search_pattern)
        
        if not csv_files:
            print(f"❌ No weather CSV files found in: {COLLECTOR_FOLDER}")
            print("Check if the path is correct!")
            return None, None, None
        
        csv_filename = csv_files[-1]
        print(f"📁 Found CSV file: {csv_filename}")

    try:
        # Load the CSV file
        df = pd.read_csv(csv_filename)
        
        # Display basic info about the data
        print("\n📊 DATA PREVIEW")
        print("="*40)
        print(df.head())
        print("\n📋 Data Info:")
        print(f"   - Rows: {len(df)}")
        print(f"   - Columns: {list(df.columns)}")
        print("="*40)
        
        # Check which columns are available
        temp_column = None
        if 'temp' in df.columns:
            temp_column = 'temp'
        elif 'temperature' in df.columns:
            temp_column = 'temperature'
        elif 'main.temp' in df.columns:
            temp_column = 'main.temp'
        
        if temp_column is None:
            print("\n⚠️  Temperature column not found!")
            print(f"Available columns: {list(df.columns)}")
            print("\nYour CSV structure might be different. Here's what we found:")
            print(df.to_string())
            return None, None, None
        
        # Calculate statistics
        avg_temp = df[temp_column].mean()
        max_temp = df[temp_column].max()
        min_temp = df[temp_column].min()
        median_temp = df[temp_column].median()
        temp_range = max_temp - min_temp
        
        # Print beautiful summary
        print("\n" + "🌡️  TEMPERATURE ANALYSIS SUMMARY")
        print("="*40)
        print(f"📍 City: {df['city'].iloc[0] if 'city' in df.columns else CITY}")
        print(f"📅 Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-"*40)
        print(f"📊 Average temperature: {avg_temp:.1f}°C")
        print(f"📈 Highest temperature: {max_temp:.1f}°C")
        print(f"📉 Lowest temperature:  {min_temp:.1f}°C")
        print(f"📐 Median temperature: {median_temp:.1f}°C")
        print(f"📏 Temperature range:  {temp_range:.1f}°C")
        print("-"*40)
        print(f"📝 Total records analyzed: {len(df)}")
        print("="*40)
        
        # Additional insights if humidity exists
        if 'humidity' in df.columns:
            avg_humidity = df['humidity'].mean()
            print(f"\n💧 Additional Info:")
            print(f"   Average humidity: {avg_humidity:.0f}%")
            
            # Check for extreme weather
            if max_temp > 35:
                print(f"   ⚠️  Extreme heat detected!")
            elif min_temp < 0:
                print(f"   ❄️  Freezing temperatures detected!")
        
        return avg_temp, max_temp, min_temp
        
    except FileNotFoundError:
        print(f"❌ Error: File '{csv_filename}' not found!")
        return None, None, None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None, None, None

def analyze_multiple_readings():
    """
    Analyze all weather CSV files you've collected over time
    """
    csv_files = glob.glob("weather_*.csv")
    
    if len(csv_files) < 2:
        print("Need at least 2 readings for trend analysis")
        return
    
    print("\n📈 TREND ANALYSIS (Multiple Readings)")
    print("="*50)
    
    all_data = []
    for file in csv_files:
        df = pd.read_csv(file)
        if 'temp' in df.columns and 'timestamp' in df.columns:
            all_data.append({
                'file': file,
                'timestamp': df['timestamp'].iloc[0],
                'temp': df['temp'].iloc[0]
            })
    
    if all_data:
        trend_df = pd.DataFrame(all_data)
        trend_df['timestamp'] = pd.to_datetime(trend_df['timestamp'])
        trend_df = trend_df.sort_values('timestamp')
        
        print(f"📊 Temperature trend over {len(trend_df)} readings:")
        print("-"*50)
        for idx, row in trend_df.iterrows():
            print(f"   {row['timestamp'].strftime('%Y-%m-%d %H:%M')}: {row['temp']:.1f}°C")
        
        # Calculate trend
        first_temp = trend_df['temp'].iloc[0]
        last_temp = trend_df['temp'].iloc[-1]
        change = last_temp - first_temp
        
        print("-"*50)
        if change > 0:
            print(f"📈 Temperature increased by {change:.1f}°C over time")
        elif change < 0:
            print(f"📉 Temperature decreased by {abs(change):.1f}°C over time")
        else:
            print(f"➡️  Temperature remained stable")

# Main execution
if __name__ == "__main__":
    print("🌤️  WEATHER DATA ANALYZER")
    print("="*40)
    
    # Option 1: Analyze the most recent CSV file
    print("\n📂 Analyzing most recent weather data...")
    analyze_weather_data()
    
    # Option 2: If you have multiple files, analyze trends
    print("\n" + "="*40)
    analyze_multiple_readings()
    
    print("\n💡 TIPS:")
    print("   - Run your data collector multiple times at different times")
    print("   - Then run this analyzer to see temperature changes")
    print("   - You can modify the code to add more analysis features!")