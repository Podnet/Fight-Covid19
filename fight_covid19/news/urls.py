from django.urls import path
from fight_covid19.news import views

urlpatterns = [
    path("", views.index, name="index"),
]
