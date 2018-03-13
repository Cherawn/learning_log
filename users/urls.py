"""为应用程序users定义URL模式"""

from django.urls import path
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登录页面
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),

    # 注销
    path('logout/', views.logout_view, name='logout'),

    # 注册页面
    path('register/', views.register, name='register'),

]