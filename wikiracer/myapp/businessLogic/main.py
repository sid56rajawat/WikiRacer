from myapp.businessLogic.getLinks import get_links

def BFS(start,target):
    cnt = 0
    Q = []
    Q.append(start)
    prev = {start:None}
    while(len(Q)!=0):
        currentVertex = Q.pop(0)
        cnt += 1
        # print(cnt)
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
                return [path,cnt]
    return []




