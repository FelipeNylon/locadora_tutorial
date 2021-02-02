
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from filmes.api import viewsets as FilmeViewset


route = routers.DefaultRouter()

route.register(r'filmes', FilmeViewset.FilmeViewset, basename="filmes")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls))
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
