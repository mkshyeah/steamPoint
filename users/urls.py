from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.popular_list, name="popular_list"),
    path('<slug:slug>/',views.sauna_detail, name="sauna_detail")
]