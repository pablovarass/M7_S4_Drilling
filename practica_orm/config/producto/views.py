from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Producto
from .forms import ProductoForm
import datetime


from .forms import ProductoForm

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/listar/')  # Redirige a listar después de iniciar sesión
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')


# Create your views here.


# Vista para la página principal
class IndexPageView(TemplateView):
    template_name = 'index.html'

@login_required
def listar(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

@login_required
def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('listar')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
            return HttpResponseRedirect(reverse('crear'))
    else:
        form = ProductoForm()
        return render(request, 'crear.html', {'form': form})


@login_required
def editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar.html', {
        'form': form,
        'producto_id': producto_id  # Add this line
    })



@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    messages.info(request, 'Producto eliminado correctamente.')
    return redirect('listar')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después del registro
        else:
            return render(request, 'registro.html', {'form': form}) 
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})  # Pasar errores del formulario a la plantilla

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar')
        else:
            messages.error(request, 'Credenciales inválidas.')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html')

def home_page(request):
    return render(request, 'index.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    return render(request, 'index.html')


from django.shortcuts import get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar.html', {'form': form})

def eliminar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar')
    return render(request, 'eliminar.html', {'producto': producto})



