from rest_framework import viewsets
from filmes import models
from filmes.api import serializers


class FilmeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.FilmeSerializer
    queryset = models.Filme.objects.all()