from django.urls import path
from .views import PostList, PostDetail


app_name = 'blog_api'

urlpatterns = [
    #two endpoints, uno para detalles de post y otro para mostrar todos los post
    path("<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("", PostList.as_view(), name="listcreate"),
]
