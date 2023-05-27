from django.contrib import admin
from django.urls import path
from .views import ArticuloListView, ArticuloCreateView, ArticuloDetailView,  ArticuloDeleteView, ArticuloUpdateView, buscar_articulo_title, buscar_articulo_autor, sobre_autor, agregar_imagen, ArticuloSectionListView


urlpatterns = [
path("list/", ArticuloListView.as_view(), name="lista_articulos"),
path("about/", sobre_autor, name="sobre_autor"),
path("create-article/", ArticuloCreateView.as_view(), name="crear_articulo"),
path("search-page-title/", buscar_articulo_title, name="buscar_articulo_title"),
path("search-page-author/", buscar_articulo_autor, name="buscar_articulo_autor"),
path("section/<str:seccion>/", ArticuloSectionListView.as_view(), name="articulos_seccion"),
path("page/<int:pk>/", ArticuloDetailView.as_view(), name="ver_articulo"),
path("delete-page/<int:pk>/", ArticuloDeleteView.as_view(), name="eliminar_articulo"),
path("edit-page/<int:pk>/", ArticuloUpdateView.as_view(), name="editar_articulo"),
path('agregar-imagen/', agregar_imagen, name="agregar_imagen"),
]