from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserRight, Match, Votes, Chat
from . import forms
from django.http import JsonResponse
import json
from django.core import serializers
from django.http import HttpResponse

@login_required(login_url="/accounts/login")
def viewMatches(request):
    is_admin = UserRight.objects.get(user = request.user).is_admin
    match_list = Match.objects.all().order_by('created_at')
    print(type(match_list))
    return render(request, 'matches/viewMatches.html', {'is_admin': is_admin, 'matches': match_list})

@login_required(login_url="/accounts/login")
def addMatch(request):
    is_admin = UserRight.objects.get(user = request.user).is_admin
    if is_admin:
        if request.method == 'POST':
            form = forms.addMatchForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                print('form is saved')
                return redirect('matches:viewMatches')
        else:
            print('form is incorrect')
            form = forms.addMatchForm()
        return render(request, 'matches/addMatch.html', {'form': form})
    
    return redirect('matches:viewMatches')

@login_required(login_url="/accounts/login")
def detailMatch(request, id):   
    match = Match.objects.get(id=id)
    votes = {
            'player_1_votes': match.player_1_votes,
            'player_2_votes': match.player_2_votes,
        }
    if request.method == 'POST':
        return JsonResponse(votes)
    else:      
        if Votes.objects.filter(match = match, user=request.user).exists():
            vote_side = Votes.objects.get(match = match, user=request.user).vote_side
            return render(request, 'matches/detailMatch.html', {'match':match, 'vote_side': vote_side})
        return render(request, 'matches/detailMatch.html', {'match':match})

@login_required(login_url="/accounts/login")
def voteMatch(request):
    if request.method == 'POST': 
        id = request.POST.get('match_id')
        match = Match.objects.get(id=id)
        instance = Votes()
        instance.vote_side = request.POST.get('vote_side')
        instance.match = match
        instance.user = request.user
        
        # Saving total votes of each side
        if request.POST.get('vote_side') == '0':
            match.player_1_votes = match.player_1_votes + 1
        elif request.POST.get('vote_side') == '1':
            match.player_2_votes = match.player_2_votes + 1
        match.save()
        instance.save()
        return JsonResponse("{'status': 'vote added'}", safe=False)

def addComment(request, status):
    if request.method == 'POST' and int(status) == 0:         
        id = request.POST.get('match_id')
        match = Match.objects.get(id=id)
        user = request.user
        instance = Chat()
        instance.match = match
        instance.user = user
        instance.text = request.POST.get('text')
        instance.save()
        return JsonResponse('{"status": "Comment added"}', safe=False) 
    
    elif request.method == 'POST' and int(status) == 1:
        print('entered')
        id = int(request.POST.get('match_id'))
        match = Match.objects.get(id=id)
        count = int(request.POST.get('count'))
        comments = []
        chats = Chat.objects.filter(match = match)
        comment_count = chats.count()
        comments.append(comment_count)
        if Chat.objects.filter(match = match).exists():
            for chat in chats.order_by('-created_at')[:count]:
                comment = {}
                comment["user"] = request.user.username
                comment["text"] = str(chat.text)
                comment["created_at"] = str(chat.created_at)
                comments.append(comment)
            return JsonResponse(comments, safe=False)
        return JsonResponse('{"status": "No comment found for this match"}', safe=False)
    return JsonResponse('{"status": "some error occured"}', safe=False)

def votedMatches(request):
    if request.method == 'POST':
        user = request.user
        user_votes = Votes.objects.filter(user = user)
        matches = []
        if user_votes:
            for i in user_votes:
                matches.append(i.match)
            data = serializers.serialize('json', matches)
        return JsonResponse(data, safe=False)
    return render(request, 'matches/votedMatches.html')




