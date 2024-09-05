from django.urls import path
from django.contrib.auth import views as auth_views
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('login/', views.login_request, name="Login"),
  path('signup/', views.register, name="Register"),
  path('logout/', LogoutView.as_view(template_name='users/logout.html', next_page='Inicio'), name="Logout"),

  path('chat/', views.ChatListView.as_view(template_name='users/chat.html'), name="Chat"),

  path('profile/', views.editar_perfil, name="Profile"),
  path('profile/change-pass/', views.PasswordChangeView.as_view(template_name='users/edit-pass.html'), name="ChangePass"),
  path('profile/change-pass/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password-change-done.html'), name='password_change_done'),
]
