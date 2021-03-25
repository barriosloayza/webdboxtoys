from django.urls import  path

from .views import *
from .viewsventa.categoria.views import * 


urlpatterns = [
    
    path('venta/',venta,name='ventas'),    
    
    #n1 esta sintaxis se usa si la vista se usa como funcion
    #n1 path('categoria/lista/',categorialista,name='categorialista'),
    
    #n2 esta sintaxis se usa si la vista es basada en una clase
    path('categoria/lista/',CategoriaListView.as_view(),name='categorialista'),
]