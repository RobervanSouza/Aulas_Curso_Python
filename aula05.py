import requests
from bs4 import BeautifulSoup

url = "https://www.vagas.com.br/vagas-de-python"
req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')

# busca todos os links do site
links = soup.find_all('a')
cards = soup.find_all('div', class_='informacoes-header')
jobs = []
for card in cards:
    # print(card.find('a'))
    job = {
        'title': card.find('a').get('title'),
        'link': f" https://www.vagas.com.br/{card.find('a').get('href')}"
    }
    jobs.append(job)
print(jobs)
print('################################################################')
        # print(card.find('a').get('href')),
# nessa aula cria um buscador de vagas