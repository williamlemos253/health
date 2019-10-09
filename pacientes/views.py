from django.shortcuts import render, redirect
from .forms import DeclaracaodesaudeForm, UserForm, ProfileForm
from .models import Declaracaodesaude, Profile
from escalas.models import Escalamedica
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test




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
                print('formulario valido')
                declaracao = form.save(commit=False)
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
@group_required('admins', 'colaborador')
def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            usuario = user_form.save(commit=False)
            perfil = profile_form.save(commit=False)
            usuario.username = perfil.cpf
            if not user_form.cleaned_data['password'] == user_form.cleaned_data['password1']:
                messages.error(request, 'Os campos de senha não são iguais.')
                return redirect('/criarusuario')
            usuario.password = make_password(user_form.cleaned_data['password'])
            usuario.save()
            perfil.user = usuario
            perfil.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('/')
        else:
            messages.error(request, 'Por favor corrija os erros.')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




# criptografa as senhas importados direto no banco de dados 
@login_required
@group_required('admins', 'colaborador')
def hashsenhas(request):
    for user in User.objects.all():
        user.set_password(user.password)
        user.save()

    return redirect('/')




@login_required
@group_required('admins', 'colaborador')
def pacientes(request):
    pacientes = Profile.objects.all()
    pacientes = pacientes.filter(user__is_staff=False)


    return render(request, 'pacientes.html', {'pacientes': pacientes })


@login_required
@group_required('admins', 'colaborador')
def jsonPacientes(request):
    pacientes = Profile.objects.filter(user__is_staff=False).values('user__last_name','sexo','birth_date','data_inclusao','cpf', 'user__id')



    pacientes_list = list(pacientes)  # important: convert the QuerySet to a list object


    return JsonResponse(pacientes_list, safe=False)



@login_required
def jsonEscalamedica(request, id):

    escalas = Escalamedica.objects.filter(paciente=id).order_by('datareg').reverse()

    escalas = escalas.values('pontuacao')



    print ("vera aqui", escalas)


    escalas_list = list(escalas)  # important: convert the QuerySet to a list object


    return JsonResponse(escalas_list[0], safe=False)


