from django.urls import path
from . import views


app_name='registration'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
]
