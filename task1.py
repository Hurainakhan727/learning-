import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website ka URL (Hum 'Quotes to Scrape' use kar rahe hain)
url = "https://quotes.toscrape.com/"

# Step 2: Website se data mangwana
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Data ko dhoondna (Quotes aur Author ke naam)
quotes_list = []
all_quotes = soup.find_all('div', class_='quote')

for item in all_quotes:
    text = item.find('span', class_='text').text
    author = item.find('small', class_='author').text
    quotes_list.append({'Quote': text, 'Author': author})

# Step 4: Data ko CSV file mein save karna
df = pd.DataFrame(quotes_list)
df.to_csv('internship_data.csv', index=False)

print("Mubarak ho! Task 1 khatam. 'internship_data.csv' check karein.")