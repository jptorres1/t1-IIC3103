from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='breakingbad-home'),
    path('episode/<int:pk>/', views.episode, name='breakingbad-episode'),
    path('character/<str:name>/', views.character, name='breakingbad-character'),
]
