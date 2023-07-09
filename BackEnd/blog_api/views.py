from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from blog_api.serializers import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#Generic Views para usar:
"""
generics.CreateAPIView: usado solamente para crear puntos.
generics.ListAPIView: usado para solamente leer punto para representar
una coleccion de las instancias del modelo
generics.DestroyAPIView: solamente para borrar de un solo modelo.
generics.UpdateAPIView: solamente para actualizar un solo modelo
generics.ListCreateAPIView: lectura y escritrura de una coleccion de modelos
generics.RetrieveUpdateAPIView: lectura o actualizacion de un solo modelo
generics.RetrieveDestroyAPIView: lectura o borrado de un solo modelo
generics.RetrieveUpdateDestroyAPIView:, lecutra, escritura y borrado de un solo modelo.
"""