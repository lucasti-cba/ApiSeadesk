
from urllib import request
from rest_framework import viewsets
from .models import *
from .serializers import *
import uuid
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter



class EnvioImagemDetail(viewsets.ModelViewSet):
    queryset = EnvioImagem.objects.all()
    serializer_class = EnvioImagemSerializer
    

class FindCaixaViewSet(viewsets.ModelViewSet):
  queryset = Caixa.objects.all()
  serializer_class = CaixaRelatorioSerializer
  #permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['nome']
  search_fields = ['nome']

class EnvioRelatorioDetail(viewsets.ModelViewSet):
    queryset = EnvioRelatorio.objects.all()
    serializer_class = EnvioRelatorioSerializer




class LogsDetail(viewsets.ModelViewSet):
    log = models.CharField(max_length=5000)
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
      #permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['log']
    search_fields = ['log']
