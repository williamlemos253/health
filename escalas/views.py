from django.shortcuts import render, redirect
from .forms import EscalaMedicaForm, EscalaSocialForm
from .models import Escalamedica, Escalasocial
from pacientes.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .funcoes import calculate_age
from django.contrib import messages

# Create your views here.

def escalamedica(request, id_paciente):

    paciente = User.objects.get(id=id_paciente)
    
    if request.method == 'POST':
        form = EscalaMedicaForm(request.POST)
        if form.is_valid():
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
            contnumcatsev0 = 0
            contnumcatsev1 = 0
            contnumcatsev2 = 0
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


            if int(escala.coracao) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.vascular) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.hematopoietico) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.respiratorio) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.otorrino) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.gastrointestinalsup) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.gastrointestinalinf) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.figado) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.renal) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.genitourinario) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.musculosqueletico) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.neurologico) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.endocrino) == 0:
                contnumcatsev0 = contnumcatsev0 + 1
            if int(escala.psiquiatrica) == 0:
                contnumcatsev0 = contnumcatsev0 + 1

            escala.numcatsev0 = contnumcatsev0

            if int(escala.coracao) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.vascular) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.hematopoietico) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.respiratorio) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.otorrino) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.gastrointestinalsup) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.gastrointestinalinf) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.figado) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.renal) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.genitourinario) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.musculosqueletico) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.neurologico) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.endocrino) == 1:
                contnumcatsev1 = contnumcatsev1 + 1
            if int(escala.psiquiatrica) == 1:
                contnumcatsev1 = contnumcatsev1 + 1

            escala.numcatsev1 = contnumcatsev1

            if int(escala.coracao) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.vascular) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.hematopoietico) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.respiratorio) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.otorrino) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.gastrointestinalsup) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.gastrointestinalinf) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.figado) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.renal) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.genitourinario) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.musculosqueletico) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.neurologico) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.endocrino) == 2:
                contnumcatsev2 = contnumcatsev2 + 1
            if int(escala.psiquiatrica) == 2:
                contnumcatsev2 = contnumcatsev2 + 1

            escala.numcatsev2 = contnumcatsev2


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
            messages.success(request, 'Escala Médica cadastrada com sucesso!')
            
            return redirect("/escalamedicaresultado/"+str(id_paciente))
            
        else:
            messages.alert(request, 'Valores inválidos detectados!')

    else:
        form = EscalaMedicaForm()


    return render (request, 'escalamedica.html', {'form':form})



@login_required
def escalamedicaresultado(request, id_paciente):
    paciente = Profile.objects.get(user=id_paciente)
    idade = calculate_age(paciente.birth_date)
    print (idade)
    resultado = Escalamedica.objects.filter(paciente=id_paciente).order_by('datareg').last()


    
    return render (request, 'escalamedicaresultado.html', { 'resultados':resultado, 'idade':idade})

@login_required
def escalamedicaresultadosanteriores(request, id):
    resultado = Escalamedica.objects.filter(paciente=id).order_by('datareg').reverse()
    return render (request, 'escalamedicaresultadosanteriores.html', {'resultados':resultado})


@login_required
def escalamedicafiltrada(request, id):
    resultado = Escalamedica.objects.get(id=id)
    return render (request, 'escalamedica.html', {'resultados':resultado})


@login_required
def escalasocial(request, id):
    form = EscalaSocialForm()
    nomepaciente = Profile.objects.get(user=id)

    pontuacao = 0
    if form.is_valid():
        escala =  form.save(commit=False)
        if escala.acamado == True:
            pontuacao = pontuacao + 3
        if escala.deficienciafisica == True:
            pontuacao = pontuacao + 3
        if escala.deficienciamental == True:
            pontuacao = pontuacao + 3
        if escala.saneamento == True:
            pontuacao = pontuacao + 3
        if escala.desnutricao == True:
            pontuacao = pontuacao + 3
        if escala.drogadicao == True:
            pontuacao = pontuacao + 2
        if escala.desempregado == True:
            pontuacao = pontuacao + 2
        if escala.analfabetismo == True:
            pontuacao = pontuacao + 1
        if  escala.menor == True:
            pontuacao = pontuacao + 1
        if  escala.maior == True:
            pontuacao = pontuacao + 1
        if  escala.hipertensao == True:
            pontuacao = pontuacao + 1
            
        pontuacao = pontuacao + int(moradores)

        escala.save()
        

        messages.success(request, 'Dados da escala de coelho cadastrados com sucesso')
        return redirect("/escaladecoelhoresultado/"+str(id))

    return render (request, 'escalasocial.html', {'paciente':nomepaciente.user.last_name, 'form':form})