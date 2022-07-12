"""FamilyProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from FamilyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FMmember, name='FMmember'),
    path('addFM', views.addFM, name='addFM'),
    path('updateFM/<int:id>', views.updateFM, name='updateFM'),
    path('deleteFM/<int:id>', views.deleteFM, name='deleteFM'),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    
    path('', include('FriendApp.urls'))
     
]
