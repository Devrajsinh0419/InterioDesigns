from django.urls import path
from .views import (
    register_user,
    login_user,
    current_user,
    protected_route,
)

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('me/', current_user),
    path('protected/', protected_route),
]