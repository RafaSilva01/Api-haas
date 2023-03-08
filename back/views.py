from django.shortcuts import render
from rest_framework import viewsets

from .models import ItemConfiguracao
from .serializer import ItemConfiguracaoSerializer

class ItemConfigurcaoViewSet(viewsets.ModelViewSet):
    queryset = ItemConfiguracao.objects.all()
    serializer_class = ItemConfiguracaoSerializer

