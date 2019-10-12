from django.shortcuts import render, redirect
from .forms import EscalaMedicaForm, EscalaSocialForm, EscalaEnfermagemForm
from .models import Escalamedica, Escalasocial, Escalaenfermagem
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
            if int(escala.pontuacao) > 0:
                escala.indgravidade = escala.pontuacao / contadorcatclass
            else:
                escala.indgravidade = 0


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
    resultado = Escalamedica.objects.filter(paciente=id_paciente).order_by('datareg').last()
    if resultado is None:
        return render (request, 'embranco.html')


    
    return render (request, 'escalamedicaresultado.html', { 'resultados':resultado, 'idade':idade})


@login_required
def escalamedicaresultadosanteriores(request, id):
    resultado = Escalamedica.objects.filter(paciente=id).order_by('datareg').reverse()
    return render (request, 'escalamedicaresultadosanteriores.html', {'resultados':resultado})

@login_required
def escalaenfermagemresultadosanteriores(request, id):
    resultado = Escalaenfermagem.objects.filter(paciente=id).order_by('datareg').reverse()
    return render (request, 'escalaenfermagemresultadosanteriores.html', {'resultados':resultado})


@login_required
def escalasocialresultadosanteriores(request, id):
    resultado = Escalasocial.objects.filter(paciente=id).order_by('datareg').reverse()
    return render (request, 'escalasocialresultadosanteriores.html', {'resultados':resultado})


@login_required
def escalamedicafiltrada(request, id):
    resultado = Escalamedica.objects.get(id=id)
    return render (request, 'escalamedicaresultado.html', {'resultados':resultado})

@login_required
def escalaenfermagemfiltrada(request, id):
    resultado = Escalaenfermagem.objects.get(id=id)
    return render (request, 'escalaenfermagemresultado.html', {'resultados':resultado})

@login_required
def escalasocialfiltrada(request, id):
    resultado = Escalasocial.objects.get(id=id)
    return render (request, 'escalasocialresultado.html', {'resultado':resultado})


@login_required
def escalasocial(request, id):

    nomepaciente = Profile.objects.get(user=id)

    pontuacao = 0
    total = 0

    if request.method =='POST':
        form = EscalaSocialForm(request.POST)
        if form.is_valid():
            print("é valido")
            escala =  form.save(commit=False)
            
            escala.paciente = nomepaciente.user
            escala.medico = request.user.last_name
            escala.medico_id = request.user.id


            if escala.acamado == True:
                pontuacao = pontuacao + 3
                total = total +1
            if escala.deficienciafisica == True:
                pontuacao = pontuacao + 3
                total = total +1
            if escala.deficienciamental == True:
                pontuacao = pontuacao + 3
                total = total +1
            if escala.saneamento == True:
                pontuacao = pontuacao + 3
                total = total +1
            if escala.desnutricao == True:
                pontuacao = pontuacao + 3
                total = total +1
            if escala.drogadicao == True:
                pontuacao = pontuacao + 2
                total = total +1
            if escala.desempregado == True:
                pontuacao = pontuacao + 2
                total = total +1
            if escala.analfabetismo == True:
                pontuacao = pontuacao + 1
                total = total +1
            if  escala.menor == True:
                pontuacao = pontuacao + 1
                total = total +1
            if  escala.maior == True:
                pontuacao = pontuacao + 1
                total = total +1
            if  escala.hipertensao == True:
                pontuacao = pontuacao + 1
                total = total +1

            totalemrisco = total

            if escala.moradores > 1:
                totalemrisco = totalemrisco + 1

            totalforaderisco = 12 - totalemrisco 
                
            pontuacao = pontuacao + int(escala.moradores)


            escala.totalemrisco = totalemrisco
            escala.totalforaderisco = totalforaderisco
            escala.pontuacao = pontuacao

            escala.save()

            messages.success(request, 'Dados da escala Psicosocial cadastrados com sucesso')
            return redirect("/escalasocialresultado/"+str(id))

    else:
        form = EscalaSocialForm()   

            

    return render (request, 'escalasocial.html', {'paciente':nomepaciente.user.last_name, 'form':form})


@login_required
def escalasocialresultado(request, id):
    resultado = Escalasocial.objects.filter(paciente=id).last()
    usuario = Profile.objects.get(id=id)
    if resultado is None:
        return render (request, 'embranco.html')

    idade = calculate_age(usuario.birth_date)

    return render (request, 'escalasocialresultado.html', {'resultado': resultado, 'idade':idade})


@login_required
def resumo(request, id):
    resultados = Escalamedica.objects.filter(paciente=id).last()
    resultadosocial = Escalasocial.objects.filter(paciente=id).last()
    resultadoenfermagem = Escalaenfermagem.objects.filter(paciente=id).last()
    usuario = Profile.objects.get(id=id)

    sexo = usuario.sexo
    idade = calculate_age(usuario.birth_date)

    return render (request, 'resumo.html', {'resultadoenfermagem':resultadoenfermagem,'resultadosocial':resultadosocial, 'resultados': resultados, 'idade':idade, 'sexo': sexo })



@login_required
def escalaenfermagem(request, id):
    nomepaciente = Profile.objects.get(id=id)



    if request.method =='POST':
        form = EscalaEnfermagemForm(request.POST)
        print ('chegou aqui', form.errors)
        if form.is_valid():
            escala = form.save(commit=False)
            soma1 = 0
            soma2 = 0
            soma3 = 0
            soma4 = 0
            somatotal = 0

            
            escala.somatotal = escala.estadomental + escala.oxigenacao + escala.sinaisvitais + escala.motibilidade \
            + escala.deambulacao + escala.alimentacao + escala.cuidadocorporal + escala.eliminacao + escala.terapeutica

            escala.paciente = nomepaciente.user
            escala.medico = request.user.last_name
            escala.medico_id = request.user.id
            
            #soma1
            if int(escala.estadomental) == 1:
                soma1 = soma1 + 1
            if int(escala.oxigenacao) == 1:
                soma1 = soma1 + 1
            if int(escala.sinaisvitais) == 1:
                soma1 = soma1 + 1
            if int(escala.motibilidade) == 1:
                soma1 = soma1 + 1
            if int(escala.deambulacao) == 1:
                soma1 = soma1 + 1
            if int(escala.alimentacao) == 1:
                soma1 = soma1 + 1
            if int(escala.cuidadocorporal) == 1:
                soma1 = soma1 + 1
            if int(escala.eliminacao) == 1:
                soma1 = soma1 + 1
            if int(escala.terapeutica) == 1:
                soma1 = soma1 + 1
            
            #soma2
            if int(escala.estadomental) == 2:
                soma2 = soma2 + 1
            if int(escala.oxigenacao) == 2:
                soma2 = soma2 + 1
            if int(escala.sinaisvitais) == 2:
                soma2 = soma2 + 1
            if int(escala.motibilidade) == 2:
                soma2 = soma2 + 1
            if int(escala.deambulacao) == 2:
                soma2 = soma2 + 1
            if int(escala.alimentacao) == 2:
                soma2 = soma2 + 1
            if int(escala.cuidadocorporal) == 2:
                soma2 = soma2 + 1
            if int(escala.eliminacao) == 2:
                soma2 = soma2 + 1
            if int(escala.terapeutica) == 2:
                soma2 = soma2 + 1
                
            #soma3
            if int(escala.estadomental) == 3:
                soma3 = soma3 + 1
            if int(escala.oxigenacao) == 3:
                soma3 = soma3 + 1
            if int(escala.sinaisvitais) == 3:
                soma3 = soma3 + 1
            if int(escala.motibilidade) == 3:
                soma3 = soma3 + 1
            if int(escala.deambulacao) == 3:
                soma3 = soma3 + 1
            if int(escala.alimentacao) == 3:
                soma3 = soma3 + 1
            if int(escala.cuidadocorporal) == 3:
                soma3 = soma3 + 1
            if int(escala.eliminacao) == 3:
                soma3 = soma3 + 1
            if int(escala.terapeutica) == 3:
                soma3 = soma3 + 1
                
            #soma4
            if int(escala.estadomental) == 4:
                soma4 = soma4 + 1
            if int(escala.oxigenacao) == 4:
                soma4 = soma4 + 1
            if int(escala.sinaisvitais) == 4:
                soma4 = soma4 + 1
            if int(escala.motibilidade) == 4:
                soma4 = soma4 + 1
            if int(escala.deambulacao) == 4:
                soma4 = soma4 + 1
            if int(escala.alimentacao) == 4:
                soma4 = soma4 + 1
            if int(escala.cuidadocorporal) == 3:
                soma4 = soma4 + 1
            if int(escala.eliminacao) == 4:
                soma4 = soma4 + 1
            if int(escala.terapeutica) == 4:
                soma4 = soma4 + 1

            escala.soma1 = soma1
            escala.soma2 = soma2
            escala.soma3= soma3
            escala.soma4 = soma4

            escala.save()
                
     
            messages.success(request, 'Dados da escala de enfermagem cadastrados com sucesso')
            return redirect('/escalaenfermagemresultado/'+str(id))

    else:
        form = EscalaEnfermagemForm()

    return render (request, 'escalaenfermagem.html', { 'form':form, 'paciente':nomepaciente})


@login_required
def escalaenfermagemresultado(request, id):
    resultado = Escalaenfermagem.objects.filter(paciente=id).order_by('datareg').last()
    if resultado is None:
        return render (request, 'embranco.html')
    usuario = Profile.objects.get(user=id)
    idade = calculate_age(usuario.birth_date)
    return render (request, 'escalaenfermagemresultado.html', {'resultados':resultado, 'idade':idade})