from django.contrib import admin
from blog.models import *
# Register your models here.

@admin.register(Post)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 'id','estado','slug','autor'
    )
admin.site.register(Categoria)