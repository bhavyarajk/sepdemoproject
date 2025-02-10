"""
URL configuration for schools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name="home"),
    path('addschool', views.AddschoolView.as_view(), name="addschool"),
    path('addstudent', views.AddstudentView.as_view(), name="addstudent"),
    path('schoollist', views.SchoollistView.as_view(), name="schoollist"),
    path('schooldetail/<int:pk>', views.SchooldetailView.as_view(), name="schooldetail"),
    path('reg',views.RegisterView.as_view(),name='register'),
    path('login',views.UserLogin.as_view(),name="login"),
    path('logout', views.User_logout.as_view(), name="logout"),
]

