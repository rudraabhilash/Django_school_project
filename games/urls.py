from django.urls import path
from . import views

urlpatterns = [
    path('award_winners/', views.award_winners_page, name='award_winnerspage'),
    path('gamessubmitform', views.submitform, name='submitform'),
    path('award_data/', views.award_data, name='award_data'),
    path('game_data/', views.game_data, name='game_data'),
    path('', views.home_page, name = 'home_page'),

]