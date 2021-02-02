from django.db import models
from uuid import uuid4



def upload(instance,filename):
    return f"{instance.id_filme}-{filename}"


class Filme(models.Model):
    id_filme = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    data_lancamento = models.IntegerField()
    arte = models.ImageField(upload_to=upload, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)


    


