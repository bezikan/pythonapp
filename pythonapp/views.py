from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('<h1>Eggs are great!</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    print(fulltext)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist)})
