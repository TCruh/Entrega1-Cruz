from django.urls import path
from views import Template
urlpatterns = [
    path('',Template,name= 'Inicio' ),
]