from django.shortcuts import render, redirect
from .forms import DeclaracaodesaudeForm, UserForm, ProfileForm
from .models import Declaracaodesaude
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


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
def hashsenhas(request):
    for user in User.objects.all():
        user.set_password(user.password)
        user.save()

    return redirect('/')




@login_required
def pacientes(request):
    pacientes = User.objects.all()
    pacientes = pacientes.filter(is_staff=False)

    return render(request, 'pacientes.html', {'pacientes': pacientes })