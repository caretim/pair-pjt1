from django.urls import path
from . import views


app_name = "pair"

urlpatterns= [
    path("",views.index, name= "pair/index"),
]