from io import TextIOWrapper
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.query_utils import PathInfo
# Create your models here.



class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

class Imagem(models.Model):
	imagem = models.ImageField(upload_to='images/', blank=True,null=True)	


class Caixa(models.Model):
    nome = models.CharField(max_length=500)  

class EnvioImagem(models.Model):
    nome = models.CharField(max_length=500, blank=True, null=True)
    hash = models.CharField(max_length=500, blank=True, null=True)
    dir = models.CharField(max_length=500, blank=True, null=True)
    pagina = models.IntegerField(blank=True, null=True)
    caixa = models.CharField(max_length=500, blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)

class EnvioRelatorio(models.Model):
    username = models.CharField(max_length=500)
    dataHora = models.DateTimeField()
    documentoDigitalizado = models.IntegerField()

class Logs(models.Model):
    log = models.CharField(max_length=5000)
    

 