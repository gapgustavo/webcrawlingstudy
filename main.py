import requests
from bs4 import BeautifulSoup

def crawl_wikipedia(url):
    # Make the HTTP request and get the HTML content of the page
    response = requests.get(url)
    html = response.content

    # Parses the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extracts the name of the visited page
    title = soup.find('title').text
    print(f'Página principal: {title}')

    # Extracts all links on the page that point to other Wikipedia pages
    wikipedia_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/wiki/') and ':' not in href:
            wikipedia_links.append(href)

    # Performs a new scrape on each captured link
    for link in wikipedia_links:
        new_url = f'https://pt.wikipedia.org{link}'
        response = requests.get(new_url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title').text
        print(f'Página secundária: {title}')

# Calls the crawl_wikipedia function with the URL of the homepage
url = 'https://pt.wikipedia.org/wiki/Am%C3%A9rica_Futebol_Clube_(Belo_Horizonte)'
crawl_wikipedia(url)