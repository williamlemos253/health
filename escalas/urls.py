from django.urls import path
from .views import escalamedica

urlpatterns = [
    path('escalamedica/<int:id_paciente>', escalamedica),

]
