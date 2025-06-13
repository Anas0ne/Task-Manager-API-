from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns = [
    path('', views.getRoutes),
    path('tasks/', views.getTasks),
    path('tasks/<int:pk>/', views.getTask),
    path('tasks/create/', views.createTask),
    path('tasks/update/<int:pk>/', views.updateTask),
    path('tasks/delete/<int:pk>/', views.deleteTask),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]   