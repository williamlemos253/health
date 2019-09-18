from django.urls import path
from .views import home, declaracaodesaude, create_profile

urlpatterns = [
    path('', home),
    path('declaracaodesaude', declaracaodesaude),
    path('criarusuario', create_profile),
]
