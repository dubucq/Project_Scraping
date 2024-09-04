import requests
from bs4 import BeautifulSoup

"""Verifier que le site est accessible arg : url(string) """

def verifSite(url):
    try:
        reponse = requests.get(url)
    except:
        print("site bloqué")

links = []

for i in range(51):

    url = 'https://books.toscrape.com/catalogue/page-'+str(i)+'.html'
    reponse = requests.get(url)

    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        livres = soup.findAll('article')
            
        for article in livres:
            a = article.find('a')
            link = a['href']
            links.append('https://books.toscrape.com/' + link)
            
   

print(len(links))
