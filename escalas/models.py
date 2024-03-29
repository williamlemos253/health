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
    deficienciafisica = models.BooleanField(verbose_name=("Deficiência Física"))
    deficienciamental = models.BooleanField(verbose_name=("Deficiência Mental"))
    saneamento = models.BooleanField(verbose_name=("Saneamento precário"))
    desnutricao = models.BooleanField(verbose_name=("Desnutrição(grave)"))
    drogadicao = models.BooleanField(verbose_name=("Drogadição"))
    desempregado = models.BooleanField(verbose_name=("Desempregado"))
    analfabetismo = models.BooleanField(verbose_name=("Analfabetismo"))
    menor = models.BooleanField(verbose_name=("Menor de 6 meses"))
    maior = models.BooleanField(verbose_name=("Maior de 70 anos"))
    hipertensao = models.BooleanField(verbose_name=("Hipertensão A. S."))
    moradores = models.PositiveSmallIntegerField(verbose_name=("Número de moradores por cômodo"))
    pontuacao = models.PositiveSmallIntegerField()
    totalemrisco = models.PositiveSmallIntegerField()
    totalforaderisco = models.PositiveSmallIntegerField()

class Escalaenfermagem(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    medico =  models.CharField(max_length=150, verbose_name=("Médico"), blank=False)
    medico_id = models.IntegerField(verbose_name=("Médico ID"), blank=False)
    datareg = models.DateTimeField(auto_now_add=True)
    estadomental = models.PositiveSmallIntegerField(validators=[valida0entre4])
    oxigenacao = models.PositiveSmallIntegerField(validators=[valida0entre4])
    sinaisvitais = models.PositiveSmallIntegerField(validators=[valida0entre4])
    motibilidade = models.PositiveSmallIntegerField(validators=[valida0entre4])
    deambulacao = models.PositiveSmallIntegerField(validators=[valida0entre4])
    alimentacao = models.PositiveSmallIntegerField(validators=[valida0entre4])
    cuidadocorporal	 = models.PositiveSmallIntegerField(validators=[valida0entre4])
    eliminacao = models.PositiveSmallIntegerField(validators=[valida0entre4])
    terapeutica = models.PositiveSmallIntegerField(validators=[valida0entre4])
    soma1 = models.PositiveSmallIntegerField()
    soma2 = models.PositiveSmallIntegerField()
    soma3 = models.PositiveSmallIntegerField()
    soma4 = models.PositiveSmallIntegerField()
    somatotal = models.PositiveSmallIntegerField()


class Escalafisioterapia(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    medico =  models.CharField(max_length=150, verbose_name=("Fisioterapeuta"), blank=False)
    medico_id = models.IntegerField(verbose_name=("Médico ID"), blank=False)
    datareg = models.DateTimeField(auto_now_add=True)
    banho = models.BooleanField(verbose_name=("Banho"))
    vestir = models.BooleanField(verbose_name=("Vertir-se"))
    higiene = models.BooleanField(verbose_name=("Higiene"))
    transferencia = models.BooleanField(verbose_name=("Transferência"))
    continencia = models.BooleanField(verbose_name=("Continência"))
    alimentacao = models.BooleanField(verbose_name=("Alimentação"))
    niveldor = models.PositiveSmallIntegerField(verbose_name=("Nível de dor"), default=1)
    pontuacao = models.PositiveSmallIntegerField()