import sys
import requests
import csv

from bs4 import BeautifulSoup
from typing import List
from loguru import logger
import requests.exceptions
from selectolax.parser import HTMLParser



logger.remove()
logger.add(f'books.log',
           level="WARNING",
           rotation="500kb")

logger.add(sys.stderr, level="INFO")

def get_all_books_urls(url: str) -> List[str]:
    """__Recupere toutes les urls des livres à partir d'une URL__

    Args:
        url (str): _URL de départ_
    Returns:
        List[str]: _Liste de toutes les URLs de toutes les pages_
    """
    pass

def get_next_page_url(tree: HTMLParser) -> str:
    """_Recupere l'URLs de la page suivante_

    Args:
        tree (HTMLParser): _Objet HTMLParser de la page_

    Returns:
        str: _URL de la page suivante_
    """
    pass

def get_all_books_urls_on_page(tree: HTMLParser) -> List[str]:
    """_Recupere toutes les URLs des livres present sur une page_

    Args:
        tree (HTMLParser): _Objet HTMLParser de la page_

    Returns:
        List[str]: _Liste de tous les URLs de tous les livres sur la page_
    """
    
    pass

def get_book_informations(url: str) -> List[str]:
    """Recupere toutes les informations d'un livre grace à une URL

    Args:
        url (str): _URL du livre_

    Returns:
        List[str]: _Liste des informations du livre_
    """
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        tree = HTMLParser(response.text)
        name = extract_book_name_from_page(tree=tree)
        price = extract_book_price_from_page(tree=tree)
        availability = extract_book_availability_from_page(tree=tree)
        stars = extract_book_stars_number_from_page(tree=tree)
        image = extract_book_image_from_page(tree=tree)
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la requête HTTPS : {e}")
    
    

def extract_book_name_from_page(tree: HTMLParser) -> str:
    """Extrait de la page le nom du livre 

    Args:
        tree (HTMLParser): _Objet HTMLParser de la page_
        
    Returns:
        str: _nom du livre_
    """
    pass
    
def extract_book_price_from_page(tree: HTMLParser) -> float:
    """Extrait de la page le prix du livre 

    Args:
        tree (HTMLParser): _Objet HTMLParser de la page_
        
    Returns:
        float: _prix du livre_
    """
    pass
    
def extract_book_availability_from_page(tree: HTMLParser) -> int:
    """Extrait de la page le nombre restant de livre 

    Args:
        tree (HTMLParser): _Objet HTMLParser de la page_
        
    Returns:
        int: _nombre de livre restant_
    """
    pass
    
def extract_book_stars_number_from_page(tree: HTMLParser) -> int:
    """Extrait de la page le nombre d'etoiles du livre 

    Args:
        tree (HTMLParser): _Objet HTMLParser de la page_
        
    Returns:
        int: _nombre d'etoile du livre_
    """
    pass
    
def extract_book_image_from_page(tree: HTMLParser) -> str:
    """Extrait de la page l'URL de l'image du livre 

    Args:
        tree (HTMLParser): _Objet HTMLParser de la page_
        
    Returns:
        str: _URL de l'image du livre_
    """
    pass

def main():
    base_URL = "https://books.toscrape.com/index.html"
    all_books_urls = get_all_books_urls(base_URL)
    for book_url in all_books_urls:
        get_book_informations(url=book_url)
    
    pass

if __name__ == '__main__':
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    get_book_informations(url=url)