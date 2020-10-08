"""p666_team URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from members import views
from django.conf.urls import url
import os
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # ex: /members/
    path('', views.MemberListView.as_view(), name="members"),
    # ex: /members/5/
    path('app/members/<str:member_id>/', views.MemberView.as_view(), name="member"),
    url(r'^(.*)$', serve, {'document_root':os.path.join(os.path.dirname(__file__), '../')})
]
