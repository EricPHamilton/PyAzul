from django.urls import path
from . import views

urlpatterns = [
    # /games/
    path('', views.index, name='index'),

    #/games/5/
    path('<int:game_id>/', views.game, name='detail'),

    #/games/5/1
    path("<int:game_id>/<int:turn_id>/", views.turn, name='turn'),
]