from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


# ── AUTORES ────────────────────────────────────────────────────────────────────

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_autores')
    return render(request, 'gestion/autor_form.html', {'form': form, 'titulo': 'Nuevo Autor'})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('lista_autores')
    return render(request, 'gestion/autor_form.html', {'form': form, 'titulo': 'Editar Autor'})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'gestion/autor_confirm_delete.html', {'objeto': autor, 'nombre': autor.nombre})


# ── LIBROS ─────────────────────────────────────────────────────────────────────

def lista_libros(request):
    libros = Libro.objects.select_related('autor').all()
    return render(request, 'gestion/lista_libros.html', {'libros': libros})


def crear_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'gestion/libro_form.html', {'form': form, 'titulo': 'Nuevo Libro'})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'gestion/libro_form.html', {'form': form, 'titulo': 'Editar Libro'})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'gestion/libro_confirm_delete.html', {'objeto': libro, 'nombre': libro.titulo})
