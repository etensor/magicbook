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

    path('resetPassword/',views.ResetPassView.as_view()),

    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),

    path('cambiarContrasena/', views.ChangePassView.as_view(), name='changepass'),

    path('<int:user_id>', views.user_page, name='user_page')
]
