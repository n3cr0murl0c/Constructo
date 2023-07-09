from django.test import TestCase
from Usuarios.models import User
from blog.models import Post, Categoria
# Create your tests here.

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Categoria.objects.create(nombre='PruebaDjango')
        test_user = User.objects.create(
            numero_identificacion='0201986825',first_name='TestUser',
            second_name='TestUser', last_name='UserTest', second_last_name ='LastName',
            email='abd@abc.com', username='testuser123', phone_no ='0123456789',
            genero=User.Genero.NOT_SAY, password='123456789'
        )
        test_post = Post.objects.create(
            categoria_id = 1, titulo ='Test Post TItle',
            excerpt =' Post Test Excerpt', contenido ='Post Contenido Prueba',
            slug='post-test', autor_id =1, estado = 'publicado'
        )
        
        return super().setUpTestData()
    
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Categoria.objects.get(id=1)
        autor = f"{post.autor}"
        excerpt = f"{post.excerpt}"
        titulo = f"{post.titulo}"
        contenido = f"{post.contenido}"
        estado = f"{post.estado}"
        self.assertEqual(autor,'Usuario: testuser123')
        self.assertEqual(titulo,'Test Post TItle')
        self.assertEqual(excerpt,' Post Test Excerpt')
        self.assertEqual(contenido,'Post Contenido Prueba')
        self.assertEqual(estado,'publicado')
        self.assertEqual(str(post), "Test Post TItle")
        self.assertEqual(str(cat), "PruebaDjango")
