from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# urlpatterns = [path('', views.lista_pendientes, name = 'pendientes')]
urlpatterns = [path('login', views.Logueo.as_view(), name = 'login'),
               path('logout', LogoutView.as_view(next_page = 'login'), name = 'logout'),
               path('registro', views.CrearCuenta.as_view(), name = 'registro'),
               path('', views.ListaTareas.as_view(), name = 'tareas'),
               path('tarea/<int:pk>', views.DetalleTarea.as_view(), name = 'tarea'),
               path('crear-tarea', views.CrearTarea.as_view(), name = 'crear-tarea'),
               path('editar-tarea/<int:pk>', views.EditarTarea.as_view(), name = 'editar-tarea'),
               path('eliminar-tarea/<int:pk>', views.EliminarTarea.as_view(), name = 'eliminar-tarea')]
