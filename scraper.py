import requests
from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/catalogue/page-'


"""Verifier que le site est accessible arg : url(string) """

def verifSite(url):
    try:
        reponse = requests.get(url)
        return True
    except:
        print("site bloqué")


def get_urls(url):
    links = []
    
    for i in range(1, 51):

        print(url + str(i) +'.html')
        reponse = requests.get(url + str(i) +'.html')

        if reponse.ok:

            soup = BeautifulSoup(reponse.text, 'html.parser')
            livres = soup.findAll('article')

        for article in livres:

            a = article.find('a')
            link = a['href']
            links.append('https://books.toscrape.com/catalogue/' + link)   

    return links

def writeTxt(liste):

    with open('urls.txt', 'w') as file:  

        for i in range (len(liste)):

            file.write(liste[i] + '\n')

def get_book_information(fichierText):
    file = fichierText
    with open('urls.txt', 'r') as file:  

        for row in file:
            url = row.strip()
            reponse = requests.get(url) 

            if reponse.ok:
                soup = BeautifulSoup(reponse.text, 'html.parser')
                nomLivre = soup.find('h1')
                prix = soup.find('p', class_="price_color")

                print(nomLivre.text + ' au prix de : ' + prix.text)
            else:
                print("erreur")





get_book_information("url.txt")



"""liste = []
liste = get_urls(url)
writeTxt(liste)
"""
print('finish')

"""links = []

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
            
   

print(len(links))"""
