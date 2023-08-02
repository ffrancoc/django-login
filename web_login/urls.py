from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.default_view),
    path('login/', views.login_view, name='login'),    
    path('index/', views.index_view, name='index'),    
]
