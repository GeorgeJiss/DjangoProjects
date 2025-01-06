from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Task  # Assuming Task is your model

def home(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/todo.html', {})

def register(request):
    return render(request, 'todoapp/register.html', {})

def login(request):
    return render(request, 'todoapp/login.html', {})

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        if task_name:
            Task.objects.create(todo_name=task_name, status=False)
        return redirect('home-page')

def delete_task(request, task_name):
    Task.objects.filter(todo_name=task_name).delete()
    return redirect('home-page')

def update_task(request, task_name):
    task = Task.objects.get(todo_name=task_name)
    task.status = not task.status
    task.save()
    return redirect('home-page')

def logout_user(request):
    logout(request)
    return redirect('home-page')
