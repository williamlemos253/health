from django.db import models
from django.contrib.auth.models import User
from .funcoes import valida0entre4

# Create your models here.

#define as funcoes de cadastro do medico para o cirs-g
class Escalamedica(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    medico =  models.CharField(max_length=150, verbose_name=("Médico"), blank=False)
    medico_id = models.IntegerField(verbose_name=("Médico ID"), blank=False)
    datareg = models.DateTimeField(auto_now_add=True)
    coracao = models.PositiveSmallIntegerField(validators=[valida0entre4])
    vascular = models.PositiveSmallIntegerField(validators=[valida0entre4])
    hematopoietico = models.PositiveSmallIntegerField(validators=[valida0entre4])
    respiratorio = models.PositiveSmallIntegerField(validators=[valida0entre4])
    otorrino = models.PositiveSmallIntegerField(validators=[valida0entre4])
    gastrointestinalsup = models.PositiveSmallIntegerField(validators=[valida0entre4])
    gastrointestinalinf = models.PositiveSmallIntegerField(validators=[valida0entre4])
    figado = models.PositiveSmallIntegerField(validators=[valida0entre4])
    renal = models.PositiveSmallIntegerField(validators=[valida0entre4])
    genitourinario = models.PositiveSmallIntegerField(validators=[valida0entre4])
    musculosqueletico = models.PositiveSmallIntegerField(validators=[valida0entre4])
    neurologico = models.PositiveSmallIntegerField(validators=[valida0entre4])
    endocrino = models.PositiveSmallIntegerField(validators=[valida0entre4])
    psiquiatrica = models.PositiveSmallIntegerField(validators=[valida0entre4])
    numcatclass = models.PositiveSmallIntegerField()
    pontuacao = models.PositiveSmallIntegerField()
    indgravidade = models.FloatField()
    numcatsev0 = models.PositiveSmallIntegerField()
    numcatsev1 = models.PositiveSmallIntegerField()
    numcatsev2 = models.PositiveSmallIntegerField()
    numcatsev3 = models.PositiveSmallIntegerField()
    numcatsev4 = models.PositiveSmallIntegerField()


class Escalasocial(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    medico =  models.CharField(max_length=150, verbose_name=("Médico"), blank=False)
    medico_id = models.IntegerField(verbose_name=("Médico ID"), blank=False)
    datareg = models.DateTimeField(auto_now_add=True)
    acamado = models.BooleanField()
    deficienciafisica = models.BooleanField()
    deficienciamental = models.BooleanField()
    saneamento = models.BooleanField()
    desnutricao = models.BooleanField()
    drogadicao = models.BooleanField()
    desempregado = models.BooleanField()
    analfabetismo = models.BooleanField()
    menor = models.BooleanField()
    maior = models.BooleanField()
    hipertensao = models.BooleanField()
    moradores = models.PositiveSmallIntegerField()
    pontuacao = models.PositiveSmallIntegerField()