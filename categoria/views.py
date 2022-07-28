from django.shortcuts import render, redirect
from .forms import CategoriaForm
from .models import Categoria

#Adiciona categoria


def categoria(request):
    return render(request, 'categoria/categoria.html')

''' 
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('categoria/buscar_categoria.html')
            except:
                pass

        else:
            form = CategoriaForm()
        return render(request, 'categoria/criar.html')
'''