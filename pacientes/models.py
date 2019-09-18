from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Declaracaodesaude(models.Model):
    created_by = models.OneToOneField(User, verbose_name=("Usuário"), on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=("Cadastrado em"))
    ans01 = models.BooleanField(default=True)
    ans02 = models.BooleanField(default=True)
    ans03 = models.BooleanField(default=True)
    ans04 = models.BooleanField(default=True)
    ans05 = models.BooleanField(default=True)
    ans06 = models.BooleanField(default=True)
    ans07 = models.BooleanField(default=True)
    ans08 = models.BooleanField(default=True)
    ans09 = models.BooleanField(default=True)
    ans10 = models.BooleanField(default=True)
    ans11 = models.BooleanField(default=True)
    ans12 = models.BooleanField(default=True)
    ans13 = models.BooleanField(default=True)
    ans14 = models.BooleanField(default=True)
    ans15 = models.BooleanField(default=True)
    ans16 = models.BooleanField(default=True)
    ans17 = models.BooleanField(default=True)
    ans18 = models.BooleanField(default=True)
    ans19 = models.BooleanField(default=True)
    ans20 = models.BooleanField(default=True)
    ans21 = models.BooleanField(default=True)
    ans22 = models.BooleanField(default=True)
    ans23 = models.BooleanField(default=True)
    ans24 = models.BooleanField(default=True)
    ans25 = models.BooleanField(default=True)
    ans26 = models.BooleanField(default=True)
    ans27 = models.PositiveSmallIntegerField()
    ans28 = models.PositiveSmallIntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=30, blank=True, unique=True)
    empresa = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name=("Data de Nascimento") )
    sexo = models.CharField(max_length=15, blank=True)
    data_inclusao = models.DateField(null=True, blank=True, verbose_name=("Data de inclusão no plano"))
