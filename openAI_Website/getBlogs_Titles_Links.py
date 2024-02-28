import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'https://www.openai.com/blog/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the article titles and links
articles = soup.find_all('li', class_='lg:w-3-cols xs:w-6-cols mt-spacing-6 md:w-4-cols')

with open('openai_blog.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])  # Write the header row
    for article in articles:
        title = article.a.h3.text.strip()
        link = f"https://openai.com{article.a['href']}"
        print(f"Title: {title}\nLink: {link}\n")
        writer.writerow([title, link])
