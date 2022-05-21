from django.urls import path 
from AppWb import views


urlpatterns = [
 
    path('', views.inicio, name='Inicio'),
    path('asociados',views.asociados, name='Asociados'),
    path('equipos', views.equipos, name='Equipos'),
    path('cursos',views.cursos, name='Cursos'),
    path('busquedaSeguidores', views.busquedaSeguidores, name='BusquedaSeguidores'),
    path('buscar/',views.buscar),
    path('leerCursos/', views.lecturaCursos, name='LecturaCursos'),
    path('eliminarCursos/<cursos_nombre>/',views.eliminarCurso,name='EliminarCursos'),
    path('editarCursos/<cursos_nombre>/',views.editarCurso, name='EditarCursos'),

    path('cursos/list', views.CursosList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursosDetalle.as_view(), name='Detail'),
    path(r'^nuevo$',views.CursosCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.CursosUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.CursosDelete.as_view(), name='Delete'),
    ]

