from django.db import models

# Create your models here.

#define as funcoes de cadastro do medico para o cirs-g
class Acirsg(models.Model):
    datareg = models.PositiveSmallIntegerField()
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
    neurologico = models.PositiveSmallIntegerField()
    endocrino = models.PositiveSmallIntegerField()
    psiquiatrica = models.PositiveSmallIntegerField()
    numcatclass = models.PositiveSmallIntegerField()
    pontuacao = models.PositiveSmallIntegerField()
    indgravidade = models.PositiveSmallIntegerField()
    numcatsev3 = models.PositiveSmallIntegerField()
    numcatsev4 = models.PositiveSmallIntegerField()
