from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#define as funcoes de cadastro do medico para o cirs-g
class Escalamedica(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    medico =  models.CharField(max_length=150, verbose_name=("Médico"), blank=False)
    medico_id = models.IntegerField(verbose_name=("Médico ID"), blank=False)
    datareg = models.DateTimeField(auto_now_add=True)
    coracao = models.PositiveSmallIntegerField()
    vascular = models.PositiveSmallIntegerField()
    hematopoietico = models.PositiveSmallIntegerField()
    respiratorio = models.PositiveSmallIntegerField()
    otorrino = models.PositiveSmallIntegerField()
    gastrointestinalsup = models.PositiveSmallIntegerField()
    gastrointestinalinf = models.PositiveSmallIntegerField()
    figado = models.PositiveSmallIntegerField()
    renal = models.PositiveSmallIntegerField()
    genitourinario = models.PositiveSmallIntegerField()
    musculosqueletico = models.PositiveSmallIntegerField()
    neurologico = models.PositiveSmallIntegerField()
    endocrino = models.PositiveSmallIntegerField()
    psiquiatrica = models.PositiveSmallIntegerField()
    numcatclass = models.PositiveSmallIntegerField()
    pontuacao = models.PositiveSmallIntegerField()
    indgravidade = models.FloatField()
    numcatsev3 = models.PositiveSmallIntegerField()
    numcatsev4 = models.PositiveSmallIntegerField()