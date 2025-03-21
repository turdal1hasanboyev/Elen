from django.urls import path

from .logout import LogOutView
from .login import LogInView
from .register import RegisterView
from .profile import ProfileView


urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
