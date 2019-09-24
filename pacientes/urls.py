from django.urls import path
from .views import home, declaracaodesaude, create_profile, hashsenhas, pacientes

urlpatterns = [
    path('', home),
    path('declaracaodesaude', declaracaodesaude),
    path('criarusuario', create_profile),
    path('hashsenhas', hashsenhas),

    path('pacientes', pacientes),
]
