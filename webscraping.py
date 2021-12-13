# Importing libraries 'requests' and 'BeautifulSoup'
import requests
from bs4 import BeautifulSoup

# The latest DAX price can be collected from investing.com
dax_url = 'https://de.investing.com/indices/germany-30-futures'

# Scraping latest DAX price
response = requests.get(dax_url)
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.find("span", class_="text-2xl")
dax_today = results.get_text()

# Removing comma and dots and create integer 'dax_today_int'
dax_today_int = dax_today[:2] + dax_today[3:6]
dax_today_int = int(dax_today_int)

print("Today's DAX price is:",dax_today_int)