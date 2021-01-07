from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordList = fulltext.split()

    wordDic = {}
    for word in wordList:
        if word in wordDic:
            wordDic[word] += 1
        else:
            wordDic[word] = 1

    sortedWords = sorted(wordDic.items(), key = operator.itemgetter(1), reverse = True )
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordList), 'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')
