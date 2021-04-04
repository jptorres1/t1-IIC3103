from django.shortcuts import render
from django.http import HttpResponse
import requests
from itertools import groupby

def home(request):
    episodes =  requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()

    bcs = filter(lambda episode: episode if episode['series'] == 'Better Call Saul' else None, episodes)
    bb = filter(lambda episode: episode if episode['series'] == 'Breaking Bad' else None, episodes)

    bcs_seasons = groupby(bcs, lambda episode: episode['season'])
    bcs_seasons = [(grouper, list(values)) for grouper, values in bcs_seasons]

    bb_seasons = groupby(bb, lambda episode: episode['season'])
    bb_seasons = [(grouper, list(values)) for grouper, values in bb_seasons]

    return render(request, 'breakingbad/home.html', {'BB': bb_seasons, 'BCS': bcs_seasons})
