from django.urls import path
from .views import home, declaracaodesaude

urlpatterns = [
    path('', home),
    path('declaracaodesaude', declaracaodesaude),
]
