from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Categoria
from Usuarios.models import User


# Create your tests here.

class PostTest(APITestCase):
    """
    Probar capacidad de GET y POST de la API
    """
    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_create_post(self):
        self.test_category = Categoria.objects.create(nombre='DjangoTest')
        self.testuser = User.objects.create(
            numero_identificacion='0201986825',first_name='TestUser',
            second_name='TestUser', last_name='UserTest', second_last_name ='LastName',
            email='abd@abc.com', username='testuser123', phone_no ='0123456789',
            genero=User.Genero.NOT_SAY, password='123456789'
        )
        data = {
            'titulo':"new", "autor":1,"excerpt":"new",
            "contenido":"new",
        }
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data,format='json')
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)