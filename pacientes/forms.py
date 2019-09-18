from django.forms import ModelForm, CharField
from .models import Declaracaodesaude, Profile
from django.contrib.auth.models import User
from django import forms


class DeclaracaodesaudeForm(ModelForm):
    ans25 = forms.IntegerField(widget=forms.NumberInput(
        attrs={
        'class':'form-control',
        'placeholder':'Peso',
        'min': '1',
        'max': '400',
        'size': '3',

        }
    ))
    ans26 = forms.IntegerField(widget=forms.NumberInput(
        attrs={
        'class':'form-control',
        'placeholder':'Altura',
        'min': '1',
        'max': '250',
        'size': '3',

        }
    ))
    class Meta:
        model = Declaracaodesaude
        fields = '__all__'
        exclude = ['created_by', 'criado_em']


class UserForm(ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput(), label='Senha', )
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('cpf', 'birth_date', 'empresa', 'sexo', 'data_inclusao')