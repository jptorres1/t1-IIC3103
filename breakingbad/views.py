from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    DetailView
)
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


def episode(request, pk):
    episode = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/{pk}').json()[0]

    return render(request, 'breakingbad/episode.html', {'episode': episode})

def character(request, name):
    character = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={name}').json()[0]
    quotes = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={name}').json()

    return render(request, 'breakingbad/character.html', {'character': character, 'quotes': quotes})