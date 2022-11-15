from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView

from .views import SignUp, profile

app_name = 'users'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path('password_reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset_form.html'
         ),
         name='password_reset'
         ),
    path('profile/<str:username>/', profile, name='profile')
]
