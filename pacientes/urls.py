from django.urls import path
from .views import home, declaracaodesaude, create_profile, hashsenhas, pacientes,consultadeclaracaodesaude, jsonPacientes, jsonEscalamedica, update_profile

urlpatterns = [
    path('', home),
    path('declaracaodesaude', declaracaodesaude),
    path('criarusuario', create_profile),
    path('atualizarperfil/<int:id>', update_profile),
    path('hashsenhas', hashsenhas),
    path('pacientes', pacientes),
    path('consultadeclaracaodesaude/<int:id>', consultadeclaracaodesaude),
    path('jsonpacientes', jsonPacientes),
    path('jsonescalamedica', jsonEscalamedica),
]
