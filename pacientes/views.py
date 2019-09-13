from django.shortcuts import render
from .forms import DeclaracaodesaudeForm
from .models import Declaracaodesaude


# Create your views here.
def home(request):
      
    return render(request ,'home.html')


def declaracaodesaude(request):

    try:
        obj = Declaracaodesaude.objects.get(user=request.user)
        form = DeclaracaodesaudeForm(request.POST or None, instance=obj)
        if request.method == "POST":
            declaracao = form.save()
    
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
        else:
            form = DeclaracaodesaudeForm()
            

    return render(request, 'declaracaodesaude.html', {'form' : form})
