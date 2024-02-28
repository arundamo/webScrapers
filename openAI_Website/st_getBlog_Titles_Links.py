import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from io import BytesIO


def scrape_openai_blog():
    # URL of the website to scrape
    url = 'https://www.openai.com/blog/'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the article titles and links
    articles = soup.find_all('li', class_='lg:w-3-cols xs:w-6-cols mt-spacing-6 md:w-4-cols')

    # Store titles and links in a list of dictionaries
    results = []
    for article in articles:
        title = article.a.h3.text.strip()
        link = f"https://openai.com{article.a['href']}"
        results.append({'Title': title, 'Link': link})

    return results


# Streamlit app
def main():
    st.title('Get Blog Titles from OpenAI blog website')
    st.write('Click the button below to fetch blog titles.')

    if st.button('Get Blog Titles'):
        results = scrape_openai_blog()
        st.write('### Results')
        if results:
            st.write('Found {} blog titles:'.format(len(results)))
            for result in results:
                st.write('- **{}:** [Link]({})'.format(result['Title'], result['Link']))

            # Add download button for CSV
            csv_data = BytesIO()
            df = pd.DataFrame(results)
            df.to_csv(csv_data, index=False)
            csv_data.seek(0)
            st.download_button(label='Download CSV', data=csv_data, file_name='openai_blog_titles.csv', mime='text/csv')
        else:
            st.write('No blog titles found.')


if __name__ == '__main__':
    main()
