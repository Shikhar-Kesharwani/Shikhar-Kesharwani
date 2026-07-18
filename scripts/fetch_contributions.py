import os
import sys
import json
import requests
from bs4 import BeautifulSoup

def main():
    username = "Shikhar-Kesharwani"
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch contributions: {e}")
        sys.exit(1)
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract total contributions from the h2 tag
    total_str = "0"
    h2 = soup.find('h2', class_='f4 text-normal mb-2')
    if h2:
        parts = h2.text.strip().split()
        if parts:
            total_str = parts[0].replace(',', '')
            
    # Parse the table cells (tool-tipped elements now use tool-tip elements in modern github HTML)
    # But for the graph cells, they are typically 'td' with class 'ContributionCalendar-day'
    cells = soup.find_all('td', class_='ContributionCalendar-day')
    
    days = []
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    best_day_count = 0
    
    for cell in cells:
        date_str = cell.get('data-date')
        if not date_str:
            continue
            
        level = int(cell.get('data-level', 0))
        
        # Tooltip text contains the count
        tooltip = cell.text.strip()
        count = 0
        if "No contributions" not in tooltip:
            parts = tooltip.split()
            if parts and parts[0].isdigit():
                count = int(parts[0])
                
        days.append({
            "date": date_str,
            "level": level,
            "count": count
        })
        
        # Streaks
        if count > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0
            
        # Best day
        if count > best_day_count:
            best_day_count = count
            
    # For current streak, we count backwards from the last day
    current_streak = 0
    for day in reversed(days):
        if day['count'] > 0:
            current_streak += 1
        else:
            if current_streak == 0 and day == days[-1]:
                continue
            break
            
    data = {
        "username": username,
        "total_contributions": int(total_str) if total_str.isdigit() else sum(d['count'] for d in days),
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": best_day_count,
        "days": days
    }
    
    os.makedirs('data', exist_ok=True)
    with open('data/contributions.json', 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully scraped {len(days)} days of contributions.")

if __name__ == "__main__":
    main()
