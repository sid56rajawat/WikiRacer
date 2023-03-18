from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.businessLogic import main

# Create your views here.
def displayLadderView(request):
    if request.method == 'GET':
        data = request.GET
        ladder,linksVisited,ladderLength = "","",""
        if(len(data)):
            start = data['start']
            target = data['target']
            solution = main.BFS(start,target)
            ladder = " -> ".join(solution[0])
            linksVisited = "No. of links visited:" + str(solution[1])
            ladderLength = "Length of ladder:" + str(len(solution[0]))

        return render(request, "homepage/index.html", {'ladder': ladder, 'linksVisited': linksVisited, 'ladderLength': ladderLength})


