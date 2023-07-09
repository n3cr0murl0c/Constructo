from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id','titulo','autor','resumen',
            'caracteristicas','tipo','area','ano_construccion',
            'imagen_principal',
            'estado','categoria',
            )
        # depth =1

    