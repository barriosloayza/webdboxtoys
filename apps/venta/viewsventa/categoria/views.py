from django.shortcuts import render
from apps.venta.models import * 

from django.views.generic import ListView


# Create your views here.


def categorialista(request):
    datos  = {
        'titulo': 'Listado de Categoria',
        'categorias': Categoria.objects.all()
    }
    return render(request, 'venta/categoria/lista.html', datos)


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'venta/categoria/lista.html'
    
    
    #n1 se debe usar esto para adcionar datos extras https://docs.djangoproject.com/en/3.1/ref/class-based-views/mixins-simple/
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categoria'
        return context
        
