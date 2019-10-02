from django.urls import path
from .views import escalamedica, escalamedicaresultado, escalamedicaresultadosanteriores, escalamedicafiltrada, escalasocial, escalasocialresultado, escalaenfermagem, resumo, escalaenfermagemresultado

urlpatterns = [
    path('escalamedica/<int:id_paciente>', escalamedica),
    path('escalamedicaresultado/<int:id_paciente>', escalamedicaresultado),
    path('escalamedicaresultadosanteriores/<int:id>', escalamedicaresultadosanteriores),
    path('escalamedicafiltrada/<int:id>', escalamedicafiltrada),
    path('escalasocial/<int:id>', escalasocial),
    path('escalasocialresultado/<int:id>', escalasocialresultado),
    path('escalaenfermagem/<int:id>', escalaenfermagem),
    path('escalaenfermagemresultado/<int:id>', escalaenfermagemresultado),
    path('resumo/<int:id>', resumo),


]
