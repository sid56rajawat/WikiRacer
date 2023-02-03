from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name="index"),
    path('homepage/',views.displayLadderView, name="displayLadder"),
]