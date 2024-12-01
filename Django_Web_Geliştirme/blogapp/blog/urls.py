from django.urls import path
from . import views # . (nokta) ile views.py içerisindeki tüm fonksiyonları import ettik.

# http://127.0.0.1:8000/ => index.html
# http://127.0.0.1:8000/index => index.html
# http://127.0.0.1:8000/blogs => blogs.html
# http://127.0.0.1:8000/blogs/3 => blog-details.html

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("blogs", views.blogs),
    path("blogs/<int:id>", views.blog_details)
]
