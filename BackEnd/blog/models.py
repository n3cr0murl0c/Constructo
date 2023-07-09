from django.db import models
from Usuarios.models import User
from django.db.models.query import QuerySet
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Opciones(models.TextChoices):
    PUBLICADO = 'publicado', 'Publicado'
    BORRADOR = 'borrador', 'Borrador'


class Post(models.Model):

    
    class PostObjects(models.Manager):
        """
        Custom manager, para obtener PostObjects con filtro default
        """
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(estado="publicado")
        
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    contenido = models.TextField()
    slug = models.SlugField(max_length=250,unique_for_date='publicado')
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    estado = models.CharField(
        max_length=10, choices=Opciones.choices, default='borrador'
    )

    objects = models.Manager()
    postobjects =PostObjects()

    class Meta:
        ordering = ['-publicado']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        
    def __str__(self):
        return self.titulo