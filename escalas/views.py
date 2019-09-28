from django.shortcuts import render
from .forms import EscalaMedicaForm
from django.contrib.auth.models import User

# Create your views here.

def escalamedica(request, id_paciente):

    paciente = User.objects.get(id=id_paciente)
    
    if request.method == 'POST':
        form = EscalaMedicaForm(request.POST)
        print (request.POST)
        if form.is_valid():
            print ('é válido')
            escala = form.save(commit=False)
            escala.paciente = paciente
            escala.medico = request.user.last_name
            escala.medico_id = request.user.id

            #soma todos os valores para fazer a classificacao
            escala.pontuacao = escala.coracao + escala.vascular + escala.hematopoietico \
            + escala.respiratorio + escala.otorrino + escala.gastrointestinalsup \
                + escala.gastrointestinalinf + escala.figado + escala.renal + escala.genitourinario \
                  + escala.musculosqueletico  + escala.neurologico + escala.endocrino + escala.psiquiatrica
            
            contadorcatclass = 0
            contnumcatsev3 = 0
            contnumcatsev4 = 0

            #conta quantas categorias foram classificadas
            if int(escala.coracao) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.vascular) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.hematopoietico) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.respiratorio) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.otorrino) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.gastrointestinalsup) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.gastrointestinalinf) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.figado) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.renal) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.genitourinario) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.musculosqueletico) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.neurologico) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.endocrino) >= 1:
                contadorcatclass = contadorcatclass + 1
            if int(escala.psiquiatrica) >= 1:
                contadorcatclass = contadorcatclass + 1

            escala.numcatclass = contadorcatclass

            #calcula o indice de gravidade do paciente
            escala.indgravidade = escala.pontuacao / contadorcatclass

            if int(escala.coracao) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.vascular) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.hematopoietico) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.respiratorio) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.otorrino) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.gastrointestinalsup) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.gastrointestinalinf) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.figado) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.renal) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.genitourinario) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.musculosqueletico) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.neurologico) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.endocrino) == 3:
                contnumcatsev3 = contnumcatsev3 + 1
            if int(escala.psiquiatrica) == 3:
                contnumcatsev3 = contnumcatsev3 + 1

            escala.numcatsev3 = contnumcatsev3
                
            if int(escala.coracao) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.vascular) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.hematopoietico) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.respiratorio) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.otorrino) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.gastrointestinalsup) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.gastrointestinalinf) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.figado) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.renal) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.genitourinario) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.musculosqueletico) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.neurologico) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.endocrino) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            if int(escala.psiquiatrica) == 4:
                contnumcatsev4 = contnumcatsev4 + 1
            
            escala.numcatsev4 = contnumcatsev4

            escala.save()
    else:
        escala = EscalaMedicaForm()



    return render (request, 'escalamedica.html', {'form':escala})
