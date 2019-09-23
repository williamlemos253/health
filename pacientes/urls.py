from django.urls import path
from .views import home, declaracaodesaude, create_profile, hashsenhas, PacientesListView

urlpatterns = [
    path('', home),
    path('declaracaodesaude', declaracaodesaude),
    path('criarusuario', create_profile),
    path('hashsenhas', hashsenhas),
    path('pacientes', PacientesListView.as_view(), name='Pacientes-view'),
]
