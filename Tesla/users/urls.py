from django.urls import path
from . import views as user_views

app_name = 'users'

urlpatterns = [
    path('register/', user_views.register, name='register'),  
    path('profile/', user_views.user_profile, name='userprofile'),
]
