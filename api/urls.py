from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.getTasks),
    path('tasks/<int:pk>/', views.getTask),
    path('tasks/create/', views.createTask),
    path('tasks/update/<int:pk>/', views.updateTask),
    path('tasks/delete/<int:pk>/', views.deleteTask),
    
]   