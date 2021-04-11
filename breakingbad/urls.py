from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('episode/<int:pk>/', views.episode, name='episode'),
    path('character/<str:name>/', views.character, name='character'),
    path('searchbar', views.searchbar, name='searchbar'),
]
