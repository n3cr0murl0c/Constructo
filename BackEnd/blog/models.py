from django.db import models
from Usuarios.models import User
from django.db.models.query import QuerySet
from django.utils import timezone

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nombre

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
    titulo = models.CharField(max_length=50)
    resumen = models.TextField(null=True, max_length=60)
    caracteristicas = models.TextField()
    ubicacion = models.CharField(max_length=150,blank=True, null=True)
    tipo = models.ForeignKey(TipoTrabajo,on_delete=models.PROTECT,null=True)
    area = models.CharField(max_length=150,blank=True, null=True)
    ano_construccion = models.CharField(max_length=25, blank=True, null=True)
    imagen_principal = models.ImageField(
        upload_to='cards',
        verbose_name='ImagenPrincipalPost',
        null=True, blank=True)
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
        
    @property
    def get_image_url(self) -> str:
        if self.imagen_principal and hasattr(self.imagen_principal, 'url'):
            return f"http://localhost:8000{self.imagen_principal.url}"
        
    def __str__(self):
        return self.titulo