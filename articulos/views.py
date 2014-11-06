from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Articulo

# Create your views here.

@login_required
def listar_articulos(request):
	articulos = Articulo.objects.all()
	return render(request, 'articulos/listar_articulos.html', {'articulos': articulos})

	