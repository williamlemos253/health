from django.urls import path
from .views import escalamedica, escalamedicaresultado, escalamedicaresultadosanteriores, escalamedicafiltrada, escalasocial, escalasocialresultado, \
 escalaenfermagem, resumo, escalaenfermagemresultado, escalaenfermagemresultadosanteriores, escalaenfermagemfiltrada, escalasocialresultadosanteriores, escalasocialfiltrada, \
     escalafisioterapia, escalafisioterapiaresultado, escalafisioterapiaresultadosanteriores, escalafisioterapiafiltrada

urlpatterns = [
    path('escalamedica/<int:id_paciente>', escalamedica),
    path('escalamedicaresultado/<int:id_paciente>', escalamedicaresultado),
    path('escalamedicaresultadosanteriores/<int:id>', escalamedicaresultadosanteriores),
    path('escalamedicafiltrada/<int:id>', escalamedicafiltrada),
    path('escalasocial/<int:id>', escalasocial),
    path('escalasocialresultado/<int:id>', escalasocialresultado),
    path('escalasocialresultadosanteriores/<int:id>', escalasocialresultadosanteriores),
    path('escalasocialfiltrada/<int:id>', escalasocialfiltrada),
    path('escalaenfermagem/<int:id>', escalaenfermagem),
    path('escalaenfermagemresultado/<int:id>', escalaenfermagemresultado),
    path('escalaenfermagemresultadosanteriores/<int:id>', escalaenfermagemresultadosanteriores),
    path('escalaenfermagemfiltrada/<int:id>', escalaenfermagemfiltrada),
    path('escalafisioterapia/<int:id>', escalafisioterapia),
    path('escalafisioterapiaresultado/<int:id>', escalafisioterapiaresultado),
    path('escalafisioterapiaresultadosanteriores/<int:id>', escalafisioterapiaresultadosanteriores),
    path('escalafisioterapiafiltrada/<int:id>', escalafisioterapiafiltrada),
    path('resumo/<int:id>', resumo),


]
