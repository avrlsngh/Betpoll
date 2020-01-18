from django.shortcuts import render

def viewMatches(request):
    return render(request, 'matches/viewMatches.html')