from django.contrib import admin
from django.urls import path,include
from car_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/new/', views.car_new, name='car_new'),
    path('car/<int:pk>/edit/', views.car_edit, name='car_edit'),
    path('car/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('car/addnew', views.car_addnew, name='car_addnew'),   
    path('update_position/', views.update_position, name='update_position'),  
]
