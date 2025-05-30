from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('',views.booking_detail, name='booking_detail'),
    path('add/<int:sauna_id>/',views.booking_add, name='booking_add'),
    path('remove/<int:sauna_id>/', views.booking_remove,
         name="booking_remove"),

]
