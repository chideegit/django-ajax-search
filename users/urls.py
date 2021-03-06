from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, ValidateUsername

urlpatterns = [
    path('register/', RegisterUserView, name='register'),
    path('login/', LoginUserView, name='login'),
    path('logout/', LogoutUserView, name='logout'),
    path('validate-username/', ValidateUsername, name='validate-username')
]