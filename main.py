import requests
from bs4 import BeautifulSoup

def crawl_wikipedia(url):
    # Faz a requisição HTTP e obtém o conteúdo HTML da página
    response = requests.get(url)
    html = response.content

    # Analisa o conteúdo HTML da página com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extrai o nome da página visitada
    title = soup.find('title').text
    print(f'Página principal: {title}')

    # Extrai todos os links da página que apontam para outras páginas da Wikipédia
    wikipedia_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/wiki/') and ':' not in href:
            wikipedia_links.append(href)

    # Realiza uma nova raspagem em cada link capturado
    for link in wikipedia_links:
        new_url = f'https://pt.wikipedia.org{link}'
        response = requests.get(new_url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title').text
        print(f'Página secundária: {title}')

# Chama a função crawl_wikipedia com a URL da página inicial
crawl_wikipedia('https://pt.wikipedia.org/wiki/Am%C3%A9rica_Futebol_Clube_(Belo_Horizonte)')