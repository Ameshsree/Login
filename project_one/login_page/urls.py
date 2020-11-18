from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('register2/', views.register2, name='reghister2'),
    # path('home', views.home, name='home'),
    path('logout', views.log_out, name='logout')
]