from django.urls import path
from django.contrib.auth import views as auth_view

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    # path('login/', views.LoginSave.as_view(template_name='login.html')),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<str:username>', views.perfil, name='profile'),

    path('<int:user_id>', views.user_page, name='user_page')
]
