from myapp.businessLogic.getLinks import get_link_names
import queue
import time

def heuristic(curr,target,targetLinks):
    commonLinksCount = 0

    for link in get_link_names(curr):
        if(link.lower() ==  target.lower()):
            return 9999
        if(link in targetLinks):
            commonLinksCount+=1

    return commonLinksCount



def heuristicSearch(start,target):
    targetLinks = get_link_names(target)
    # print("start =",start,"\ttarget =",target,"\nlen(start) =",len(start),"\tlen(target) =",len(target))
    pagesVisited = 0

    PQ = queue.PriorityQueue()
    PQ.put((heuristic(start,target,targetLinks) * -1,start))
    prev = {start:None}

    while(PQ.empty()==False):
        currentHeuristic,currentVertex = PQ.get()
        pagesVisited += 1
        print(currentVertex,currentHeuristic)

        adjacentVertices = get_link_names(currentVertex)
        for av in adjacentVertices:
            if(av not in prev): # if unvisited
                PQ.put((heuristic(av,target,targetLinks) * -1,av))
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
    targetLinks = get_link_names(target)
    start_time = time.time()
    # print(heuristic(start))
    print(heuristicSearch(start,target))
    print("Time taken:",time.time()-start_time)


