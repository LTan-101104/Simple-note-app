"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf, (urls define in sub-apps)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #!pre-built view for access token and refresh token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name = "register"), #always include a / in path
    path("api/token/", TokenObtainPairView.as_view(), name = "get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name = "refresh"),
    path("api-auth/", include("rest_framework.urls")), #import all necessary views from rest_framework
    path("api/", include("api.urls")),
]
#TODO: after set this up, make migration
'''
to migrate:
1. Run python manage.py makemigrations; this is for creating a file specifying what migrations need to be performed
2.Run python manage.py migrate; this will migrate the database
'''