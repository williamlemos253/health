from django.forms import ModelForm, CharField, CheckboxInput, ChoiceField
from .models import Escalamedica, Escalasocial, Escalaenfermagem, Escalafisioterapia
from django.contrib.auth.models import User
from django import forms
from bootstrap4.widgets import RadioSelectButtonGroup


class EscalaMedicaForm(ModelForm):
    class Meta:
        model = Escalamedica
        fields = '__all__'
        exclude = ['paciente', 'medico', 'medico_id','datareg','numcatclass', 'pontuacao', 
        'indgravidade', 'numcatsev0', 'numcatsev1', 'numcatsev2', 'numcatsev3', 'numcatsev4']


class EscalaSocialForm(ModelForm):
    moradores = forms.ChoiceField(
        help_text="",
        required=True,
        label="",
        widget=RadioSelectButtonGroup,
        choices=((1, '1'), (2, '2'), (3, '>3')),
        initial=1,
    )
    class Meta:
        model = Escalasocial
        fields = '__all__'
        exclude = ['paciente', 'medico', 'medico_id','datareg', 'pontuacao', 'totalemrisco', 'totalforaderisco']


class EscalaEnfermagemForm(ModelForm):
    class Meta:
        model = Escalaenfermagem
        fields = '__all__'
        exclude = ['paciente', 'medico', 'medico_id','datareg', 'soma1', 'soma2', 'soma3', 'soma4','somatotal' ]


class EscalaFisioterapiaForm(ModelForm):
    niveldor  = forms.ChoiceField(
        help_text="",
        required=True,
        label="",
        widget=RadioSelectButtonGroup,
        choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')),
        initial=1,
    )
    class Meta:
        model = Escalafisioterapia
        fields = '__all__'
        exclude = ['paciente', 'medico', 'medico_id','datareg', 'pontuacao']

    

    