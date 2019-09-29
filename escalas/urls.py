from django.urls import path
from .views import escalamedica, escalamedicaresultado

urlpatterns = [
    path('escalamedica/<int:id_paciente>', escalamedica),
    path('escalamedicaresultado/<int:id_paciente>', escalamedicaresultado),

]
