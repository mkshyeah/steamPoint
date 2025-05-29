from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.popular_list, name="popular_list"),
    path('shop/', views.saunas_list, name='saunas_list'),
    path('shop/<slug:slug>/',views.sauna_detail,
         name="sauna_detail")
    path('shop/category/<slug:category_slug>',views.saunas_list,
         name='saunas_list_by_category'),
]