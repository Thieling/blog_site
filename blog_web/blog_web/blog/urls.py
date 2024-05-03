from django.contrib import admin
from django.urls import path
from .views import (
    view_todos_articulos, 
    view_articulo_detalles, 
    view_crear_usuario_form,
    view_cerrar_sesion,
    view_iniciar_sesion,
    view_buscar_articulo_form,
    view_crear_articulo,
    view_gestionar_articulo,
    view_editar_articulo,
    view_borrar_articulo,
    view_avatar,
    view_about,
    EditarUsuarioView,
)

urlpatterns = [
    path("articulos/lista/", view_todos_articulos, name="todos-articulos"),
    path("articulos/busqueda/", view_buscar_articulo_form, name="buscar-articulos"),
    path("about/", view_about, name="about"),
    path('articulos/detalle/<int:art_id>', view_articulo_detalles, name="detalles-articulo"),
    path("articulos/crear/", view_crear_articulo, name="crear-articulos"),
    path("articulos/editar/<int:id>", view_editar_articulo, name="editar-articulo"),
    path("articulos/borrar/<int:id>", view_borrar_articulo, name="borrar-articulo"),
    path("articulos/gestion/", view_gestionar_articulo, name="gestion-articulos"),
    path("usuario/crear/", view_crear_usuario_form, name="crear-usuario"),
    path('editar-perfil/', EditarUsuarioView.as_view(), name='editar-perfil'),
    path("usuario/iniciar_sesion/", view_iniciar_sesion, name="iniciar-sesion"),
    path("usuario/cerrar_sesion/", view_cerrar_sesion, name="cerrar-sesion"),
    path('avatar/agregar/', view_avatar, name='agregar-avatar'),
    ]