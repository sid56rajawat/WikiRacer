import httplib2
from bs4 import BeautifulSoup, SoupStrainer

def get_links(url): # used to get adjacent vertices of a vertex
    http = httplib2.Http()
    response, content = http.request(url)

    links = []
    for link in BeautifulSoup(content,features="html.parser",parse_only=SoupStrainer('div',{'id': 'bodyContent'})).find_all('a', href=True):
        linkString = link['href']
        if(linkString.startswith("/wiki/") and ":" not in linkString and "#" not in linkString):
            links.append(linkString[6:])

    # [print(i, end='\n') for i in links]
    return links

def BFS(start,target):
    cnt = 0
    Q = []
    Q.append(start)
    prev = {start:None}
    while(len(Q)!=0):
        currentVertex = Q.pop(0)
        cnt += 1
        adjacentVertices = get_links("https://en.wikipedia.org/wiki/" + currentVertex)
        for av in adjacentVertices:
            if(av not in prev.keys()):
                Q.append(av)
                prev[av] = currentVertex
            if(av.lower() == target.lower()):
                path = []
                while(av != None):
                    path.append(av)
                    av = prev[av]
                path.reverse()
                print("No of links visited :",cnt)
                return path
    return []

start = input("Start : ")
target = input("Target : ")
ladder = BFS(start,target)
[print(i ,end=" -> ") for i in ladder]



