from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("atharv", views.atharv, name="atharv"),
    path("<str:name>", views.greet, name="greet")
]