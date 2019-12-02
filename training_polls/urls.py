from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'training_polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_page/', views.login_page, name='login_page'),
    path('get_enter/<int:language_id>/', views.get_enter, name='get_enter'),
    path('<int:language_id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('get_delete/<int:id_field>/', views.get_delete, name='get_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='training_polls/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='training_polls/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='training_polls/password_reset.html'
         ),
         name='password_reset'),
    path('password_reset_done',
         auth_views.PasswordResetDoneView.as_view(
             template_name='training_polls/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='training_polls/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='training_polls/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
