from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Game, Turn

# Create your views here.
def index(request):
    games_list = Game.objects.order_by('id')
    template = loader.get_template('games/index.html')
    context = {
        'games_list': games_list
    }
    return HttpResponse(template.render(context, request))

def game(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
        turns = game.turns.all()
        template = loader.get_template('games/game.html')
        context = {
            'game_time': game.game_time,
            'turn_list': turns,
        }
        return HttpResponse(template.render(context, request))

    except Game.DoesNotExist:
        raise Http404("Game does not exist")

def turn(request, game_id, turn_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("Game does not exist")

    try:
        turn = game.turns.all()[turn_id - 1]
    except Turn.DoesNotExist:
        raise Http404("Turn does not exist")

    template = loader.get_template('games/turn.html')
    context = {
        'turn': turn,
    }
    return HttpResponse(template.render(context, request))