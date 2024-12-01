"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1:8000/ => index.html
# http://127.0.0.1:8000/index => index.html
# http://127.0.0.1:8000/blogs => blogs.html
# http://127.0.0.1:8000/blogs/3 => blog-details.html

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")) # Blog uygulamasındaki urls.py dosyasını include ettik.
    # Yani projenin ana uygulaması olan buradaki urls'e bunu tanıttık.
    
    # path("user/", include("blog.urls"))
    # Yukarıdaki gibi "user" yazarsak artık url'miz http://127.0.0.1:8000/ değil
    # http://127.0.0.1:8000/user olur. Diğerleri de buna göre değişir.
]
