import httplib2
import time
from bs4 import BeautifulSoup, SoupStrainer

def get_links(query): # fetches all the valid links on a given url
    url = "https://en.wikipedia.org/wiki/" + query
    http = httplib2.Http()
    response, content = http.request(url)

    links = set()
    for link in BeautifulSoup(content,features="html.parser").find_all('a', href=True):
        linkString = link['href']
        if(linkString.startswith("/wiki/") and ":" not in linkString and "#" not in linkString):
            links.add(linkString[6:])
        # if(len(links) > 500): # branching factor
        #     break
    return links

if __name__ == '__main__':
    thing = input("Search Wiki : ")
    startTime = time.time()
    links = get_links(thing)
    [print(i) for i in links]
    print("Total links on",thing,"=",len(links))
    print("Time taken =",time.time()-startTime,"seconds")