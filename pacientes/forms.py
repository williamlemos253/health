from django.forms import ModelForm
from .models import Declaracaodesaude

class DeclaracaodesaudeForm(ModelForm):
    class Meta:
        model = Declaracaodesaude
        fields = '__all__'
        exclude = ['created_by', 'criado_em']