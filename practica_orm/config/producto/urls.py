from django.urls import path
from . import views
from .views import listar, crear, iniciar_sesion, home_page, cerrar_sesion, registro, editar, eliminar

urlpatterns = [
    path ('listar/', listar, name = 'listar'),
    path ('crear/', crear, name = 'crear'),
    path('registro/', registro, name='registro'), 
    path('login/', iniciar_sesion, name='login'), 
    path('home/', home_page, name='home'), 
    path('logout/', cerrar_sesion, name='logout'),
    path('', home_page, name='home'),  # Ruta para el path vacío
    path('index/', home_page, name='index'),  # Ruta para 'index'
    path('editar/<int:producto_id>/', editar, name='editar'), 
    path('delete/<int:producto_id>/', eliminar, name='eliminar'),   
]
