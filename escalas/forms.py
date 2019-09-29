from django.forms import ModelForm, CharField, CheckboxInput, ChoiceField
from .models import Escalamedica
from django.contrib.auth.models import User
from django import forms
from bootstrap4.widgets import RadioSelectButtonGroup


class EscalaMedicaForm(ModelForm):
    class Meta:
        model = Escalamedica
        fields = '__all__'
        exclude = ['paciente', 'medico', 'medico_id','datareg','numcatclass', 'pontuacao', 
        'indgravidade', 'numcatsev0', 'numcatsev1', 'numcatsev2', 'numcatsev3', 'numcatsev4']