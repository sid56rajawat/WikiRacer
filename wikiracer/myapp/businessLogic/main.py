from myapp.businessLogic.getLinks import get_links
import queue
import time


def heuristic(curr):
    commonLinksCount = 0

    for link in get_links(curr):
        if(link.lower() ==  target.lower()):
            return 9999
        if(link in targetLinks):
            commonLinksCount+=1

    return commonLinksCount



def heuristicSearch(start,target):
    # print("start =",start,"\ttarget =",target,"\nlen(start) =",len(start),"\tlen(target) =",len(target))
    pagesVisited = 0

    PQ = queue.PriorityQueue()
    PQ.put((heuristic(start) * -1,start))
    prev = {start:None}

    while(PQ.empty()==False):
        currentHeuristic,currentVertex = PQ.get()
        pagesVisited += 1
        print(currentVertex,currentHeuristic)

        adjacentVertices = get_links(currentVertex)
        for av in adjacentVertices:
            if(av not in prev): # if unvisited
                PQ.put((heuristic(av) * -1,av))
                prev[av] = currentVertex
            if(av.lower() == target.lower()): # if target
                path = []
                while(av != None):
                    path.append(av)
                    av = prev[av]
                path.reverse()
                return [path,pagesVisited]
    return []


if __name__ == "__main__":
    start = input("Enter start: ")
    target = input("Enter target: ")
    targetLinks = get_links(target)
    start_time = time.time()
    # print(heuristic(start))
    print(heuristicSearch(start,target))
    print("Time taken:",time.time()-start_time)


