from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name = 'register'),      
    path('login/', views.loginpage, name = 'login'),
    # path('add/', views.add_task, name='add-task'),       
    path('delete/<str:task_name>/', views.delete, name='delete'),
    path('update/<str:task_name>/', views.update, name='update'),
    path('logout/', views.logout_user, name='logout'),
]
