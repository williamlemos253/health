from django.forms import ModelForm, CharField, CheckboxInput, ChoiceField
from .models import Escalamedica
from django.contrib.auth.models import User
from django import forms
from bootstrap4.widgets import RadioSelectButtonGroup


class EscalaMedicaForm(ModelForm):
    coracao = forms.ChoiceField(
        required=True,
        widget=RadioSelectButtonGroup
        (
            attrs={
            'class':'btn-info btn-lg collapsed',
            },
        ),
        choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')),
        initial=0,
        
    )
    class Meta:
        model = Escalamedica
        fields = '__all__'
        exclude = ['paciente', 'medico', 'medico_id','datareg','numcatclass', 'pontuacao', 
        'indgravidade', 'numcatsev3', 'numcatsev4']