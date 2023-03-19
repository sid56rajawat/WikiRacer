import httplib2
import time
from bs4 import BeautifulSoup

def make_wikipedia_url(thing) -> str:
    return "https://en.wikipedia.org/wiki/" + thing

def page_content(url) -> bytes:  #non deterministic therfore no test cases
    http = httplib2.Http()
    response, content = http.request(url)
    return content

def anchors_extractor(content: bytes):
    all_links = BeautifulSoup(content,features="html.parser").find_all('a', href=True)
    return all_links

def is_valid_link(link) -> bool:
    return link.startswith("/wiki/") and ":" not in link and "#" not in link

def get_link_names(thing) -> set[str]: # fetches all the valid links on a given url
    BRANCHING_FACTOR = 100

    url = make_wikipedia_url(thing)

    content = page_content(url)

    all_anchors = anchors_extractor(content)
    valid_link_names = set()

    for anchor in all_anchors:
        link = anchor['href']
        if(is_valid_link(link)):
            link_name = link[:6]
            valid_link_names.add(link_name)
        if(len(valid_link_names) >= BRANCHING_FACTOR): 
            break
    return valid_link_names

if __name__ == '__main__':
    thing = input("Search Wiki : ")
    # startTime = time.time()
    links = get_link_names(thing)
    [print(i) for i in links]
    print("Total links on",thing,"=",len(links))
    # print("Time taken =",time.time()-startTime,"seconds")