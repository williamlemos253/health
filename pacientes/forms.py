from django.forms import ModelForm, CharField, CheckboxInput
from .models import Declaracaodesaude, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS


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
        exclude = ['created_by', 'criado_em', 'pontuacao']


class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(label='Nome Completo', required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('last_name','email')


class UserUpdateForm(UserCreationForm):
    password1 = forms.CharField(label=("Senha"), required=False,
                            widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Confirmação de"),
                            widget=forms.PasswordInput, required=False)
    class Meta:
        model = User
        fields = ('last_name', 'username', 'email')




class ProfileForm(ModelForm):
    sexo = forms.ChoiceField(
        label ="sexo",
        required=True,
        choices=(('M', 'Masculino'), ('F', 'Feminino')),
        initial=1,
    )
    class Meta:
        model = Profile
        fields = ('cpf', 'birth_date', 'empresa', 'sexo', 'data_inclusao')
        error_messages = {
                NON_FIELD_ERRORS: {
                    'unique_together':"Esse usuário já está cadastrado, por favor verifique",
                },
            }