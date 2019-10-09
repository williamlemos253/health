from django.urls import path
from .views import escalamedica, escalamedicaresultado, escalamedicaresultadosanteriores, escalamedicafiltrada, escalasocial, escalasocialresultado, \
 escalaenfermagem, resumo, escalaenfermagemresultado, escalaenfermagemresultadosanteriores, escalaenfermagemfiltrada, escalasocialresultadosanteriores, escalasocialfiltrada

urlpatterns = [
    path('escalamedica/<int:id_paciente>', escalamedica),
    path('escalamedicaresultado/<int:id_paciente>', escalamedicaresultado),
    path('escalamedicaresultadosanteriores/<int:id>', escalamedicaresultadosanteriores),
    path('escalamedicafiltrada/<int:id>', escalamedicafiltrada),
    path('escalasocial/<int:id>', escalasocial),
    path('escalasocialresultado/<int:id>', escalasocialresultado),
    path('escalsocialresultadosanteriores/<int:id>', escalasocialresultadosanteriores),
    path('escalsocialfiltrada/<int:id>', escalasocialfiltrada),
    path('escalaenfermagem/<int:id>', escalaenfermagem),
    path('escalaenfermagemresultado/<int:id>', escalaenfermagemresultado),
    path('escalenfermagemresultadosanteriores/<int:id>', escalaenfermagemresultadosanteriores),
    path('escalenfermagemfiltrada/<int:id>', escalaenfermagemfiltrada),
    path('resumo/<int:id>', resumo),


]
