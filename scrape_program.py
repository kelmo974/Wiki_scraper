
url = input(f"Paste the URL you'd like to scrape here: ")


def wiki_scrape(url):
    import requests
    from bs4 import BeautifulSoup
    response =requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
