from http.client import HTTPResponse
from typing import overload
from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import *
from ipware import get_client_ip
from django.template import Library
from rest_framework import viewsets
from .serializers import *
import base64
from PIL import Image
import io


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class FindCaixa(viewsets.ViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    serializers = CaixaRelatorioSerializer
    authentication_classes = [authentication.TokenAuthentication]


    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        caixas = [Caixa.nome for nome in Caixa.objects.all()]
        return Response(caixas)  
    
    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        caixas = [Caixa.nome for nome in Caixa.objects.filter(nome=request.data.busca)]
        return Response(caixas)



def index(request):
    images = Envio.objects.all()
    lista = []
    for image in images:
        temp =  image.imagem
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(temp, "utf-8"))))
        img.save(image.nome)
    return HTTPResponse('ok')
 

