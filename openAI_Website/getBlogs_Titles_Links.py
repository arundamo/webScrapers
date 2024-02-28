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

# Open a CSV file in write mode
with open('openai_blog.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])  # Write the header row

    # Loop through each article and extract title and link
    for article in articles:
        title = article.a.h3.text.strip()  # Extract the title
        link = f"https://openai.com{article.a['href']}"  # Extract the link
        print(f"Title: {title}\nLink: {link}\n")  # Print title and link
        writer.writerow([title, link])  # Write title and link to CSV
