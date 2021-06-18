from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<int:apply_id>', views.detail, name='detail'),
    path('create',views.create,name='create'),
    path('update/<int:apply_id>/', views.update, name='update'),
    path('delete/<int:apply_id>/', views.delete, name='delete'),
]