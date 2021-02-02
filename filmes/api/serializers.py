from rest_framework import serializers
from filmes import models


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filme
        fields = '__all__'