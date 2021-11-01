"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter


from users.views import BooKAPIView1, BookAPIView2, BookModelViewSet

router = DefaultRouter()
router.register(r'apibook5', BookModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apibook1/', BooKAPIView1.as_view(), name="book1"),
    path('apibook2/', BookAPIView2.as_view(), name="book2"),
    path('', include(router.urls)),
    path('drf/', include("drf_token.urls"))
]
