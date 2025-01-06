from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name = 'register'),      
    path('login/', views.login, name = 'login'),
    path('add/', views.add_task, name='add-task'),       
    path('delete/<str:task_name>/', views.delete_task, name='delete-task'),
    path('update/<str:task_name>/', views.update_task, name='update-task'),
    path('logout/', views.logout_user, name='logout'),
]
