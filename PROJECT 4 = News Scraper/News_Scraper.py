# simple_news_scraper.py - Easy to understand web scraper

import requests
from bs4 import BeautifulSoup
import pandas as pd

# STEP 1: Get the webpage
print("🌐 Fetching Hacker News...")
url = "https://news.ycombinator.com"
response = requests.get(url)

# STEP 2: Check if it worked
if response.status_code == 200:
    print("✅ Successfully got the webpage!")
    
    # STEP 3: Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # STEP 4: Find all news titles
    titles = []
    
    # Hacker News stores titles in elements with class "titleline"
    for item in soup.find_all(class_="titleline"):
        # Each title is inside an <a> tag
        link = item.find('a')
        if link:
            title = link.get_text()
            titles.append(title)
    
    # STEP 5: Display what we found
    print(f"\n📰 Found {len(titles)} news articles:")
    print("-" * 50)
    
    for i, title in enumerate(titles[:10], 1):  # Show first 10
        print(f"{i}. {title}")
    
    # STEP 6: Save to CSV file
    df = pd.DataFrame({
        'title': titles,
        'source': 'Hacker News',
        'scraped_date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    df.to_csv('news_articles.csv', index=False)
    print(f"\n💾 Saved to 'news_articles.csv'")
    
else:
    print(f"❌ Failed to get webpage. Status code: {response.status_code}")