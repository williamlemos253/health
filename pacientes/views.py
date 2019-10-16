from django.shortcuts import render, redirect
from .forms import DeclaracaodesaudeForm, ProfileForm, CustomUserCreationForm, UserUpdateForm
from .models import Declaracaodesaude, Profile
from escalas.models import Escalamedica
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required



def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)

# Create your views here.
@login_required
def home(request):
      
    return render(request ,'home.html')



@login_required
def declaracaodesaude(request):

    try:
        obj = Declaracaodesaude.objects.get(created_by=request.user)
            
        if obj is not None:
            return render (request, 'declaracaodesaude_resultado.html', {'resultado' : obj})
    except:
        if request.method == "POST":
            form = DeclaracaodesaudeForm(request.POST)
            print (request.POST)
            print ("passou por aqui")
            if form.is_valid():
                declaracao = form.save(commit=False)

                pontuacao = 0

                if declaracao.ans01 == True:
                    pontuacao = pontuacao + 2
                
                if declaracao.ans02 == True:
                    pontuacao = pontuacao + 2

                if declaracao.ans03 == True:
                    pontuacao = pontuacao + 2

                if declaracao.ans04 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans05 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans06 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans07 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans08 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans09 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans10 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans11 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans12 == True:
                    pontuacao = pontuacao + 2

                if declaracao.ans13 == True:
                    pontuacao = pontuacao + 4

                if declaracao.ans14 == True:
                    pontuacao = pontuacao + 4
                
                if declaracao.ans15 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans16 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans17 == True:
                    pontuacao = pontuacao + 1

                if declaracao.ans18 == True:
                    pontuacao = pontuacao + 2
                
                if declaracao.ans19 == True:
                    pontuacao = pontuacao + 3
                
                if declaracao.ans20 == True:
                    pontuacao = pontuacao + 4

                if declaracao.ans21 == True:
                    pontuacao = pontuacao + 4
                
                if declaracao.ans22 == True:
                    pontuacao = pontuacao + 4

                if declaracao.ans23 == True:
                    pontuacao = pontuacao + 2

                if declaracao.ans24 == True:
                    pontuacao = pontuacao + 3

                if declaracao.outradoenca == True:
                    pontuacao = pontuacao + 1

                

                declaracao.pontuacao = pontuacao


                declaracao.created_by = request.user
                declaracao.save()
                return redirect('/declaracaodesaude')
        else:
            form = DeclaracaodesaudeForm()
            
    return render(request, 'declaracaodesaude.html', {'form' : form})



@login_required
def consultadeclaracaodesaude(request, id):
    try:
        obj = Declaracaodesaude.objects.get(created_by=id)
            
        if obj is not None:
            return render (request, 'declaracaodesaude_resultado.html', {'resultado' : obj})
    except:
            return render (request, 'embranco.html')


@login_required
@staff_member_required
def create_profile(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            usuario = user_form.save(commit=False)
            perfil = profile_form.save(commit=False)
            usuario.save()
            perfil.user = usuario
            perfil.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('/')
      
            
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



@login_required
@staff_member_required
def update_profile(request, id):
    usuario = User.objects.get(id=id)
    try:
        profile = Profile.objects.get(user=id)
        profile_form = ProfileForm(instance=profile)
    except:
        user_form = CustomUserCreationForm(request.POST, instance=usuario)
        profile_form = ProfileForm()
        profile = None

    if request.method == 'POST':
        if profile is None:
            perfil = profile_form.save(commit=False)
            perfil.user = usuario
            perfil.save()
            profile = Profile.objects.get(user=id)
        user_form = UserUpdateForm(request.POST, instance=usuario) 
        profile_form = ProfileForm(request.POST, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            usuario.save()
            profile.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('/pacientes')
        else:
            messages.error(request, 'Por favor corrija os erros.')
    else:
        user_form = UserUpdateForm(instance=usuario)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })





# criptografa as senhas importados direto no banco de dados 
@login_required
@staff_member_required
def hashsenhas(request):
    for user in User.objects.all():
        user.set_password(user.password)
        user.save()

    return redirect('/')




@login_required
@staff_member_required
def pacientes(request):
    pacientes = Profile.objects.all()
    pacientes = pacientes.filter(user__is_staff=False)


    return render(request, 'pacientes.html', {'pacientes': pacientes })


@login_required
@staff_member_required
def jsonPacientes(request):
    pacientes = Profile.objects.filter(user__is_staff=False).values('user__last_name','sexo','birth_date','data_inclusao','cpf', 'user__id')



    pacientes_list = list(pacientes)  # important: convert the QuerySet to a list object


    return JsonResponse(pacientes_list, safe=False)



@login_required
@staff_member_required
def jsonEscalamedica(request):

    pacientes = User.objects.filter(is_staff=False).prefetch_related('id').distinct('id')


    pacientes = pacientes.values('last_name','profile__sexo','profile__birth_date','profile__data_inclusao','profile__cpf', \
     'id','declaracaodesaude__pontuacao','escalamedica__pontuacao','escalasocial__pontuacao', 'escalaenfermagem__somatotal').iterator()

    

 # important: convert the QuerySet to a list object
    pacientes_list = list(pacientes)


    return JsonResponse(pacientes_list, safe=False)