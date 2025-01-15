from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_student', views.add_student, name='add_student'),
    path('delete_student/<int:id>/', views.delete_student,name='delete_student'),
path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
]
