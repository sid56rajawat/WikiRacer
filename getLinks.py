import httplib2
from bs4 import BeautifulSoup, SoupStrainer

def get_links(url): # used to get adjacent vertices of a vertex
    http = httplib2.Http()
    response, content = http.request(url)

    links = set()
    for link in BeautifulSoup(content,features="html.parser").find_all('a', href=True):
        linkString = link['href']
        if(linkString.startswith("/wiki/") and ":" not in linkString and "#" not in linkString):
            links.add(linkString[6:])

    # [print(i, end='\n') for i in links]
    # print(len(links))
    return links

# get_links("https://en.wikipedia.org/wiki/Snake")