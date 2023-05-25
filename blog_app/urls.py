from django.contrib import admin
from django.urls import path
from .views import ArticuloListView, ArticuloCreateView, ArticuloDetailView,  ArticuloDeleteView, ArticuloUpdateView, buscar_articulo_autor, buscar_articulo_title, sobre_autor, agregar_imagen, ArticuloSectionListView


urlpatterns = [
path("list/", ArticuloListView.as_view(), name="lista_articulos"),
path("about/", sobre_autor, name="sobre_autor"),
path("create-page/", ArticuloCreateView.as_view(), name="crear_articulo"),
path("search-page/<str:autor>/", buscar_articulo_autor, name="buscar_articulos_autor"),
path("search-page-title/", buscar_articulo_title, name="buscar_articulostitle"),
path("section/<str:seccion>/", ArticuloSectionListView.as_view(), name="articulos_seccion"),
path("page/<int:pk>/", ArticuloDetailView.as_view(), name="ver_articulo"),
path("delete-page/<int:pk>/", ArticuloDeleteView.as_view(), name="eliminar_articulo"),
path("edit-page/<int:pk>/", ArticuloUpdateView.as_view(), name="editar_articulo"),
path('agregar-imagen/', agregar_imagen, name="agregar_imagen"),
]