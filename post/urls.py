from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('detail/<int:apply_id>', views.detail, name='detail'),
    path('create',views.create,name='create'),
    path('update/<int:apply_id>/', views.update, name='update'),
    path('delete/<int:apply_id>/', views.delete, name='delete'),
]