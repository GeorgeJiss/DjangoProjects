from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from . models import Task
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = Task(user=request.user, todo_name = task)
        new_todo.save()

    all_todos = Task.objects.filter(user=request.user)
    context = {
        'todos' : all_todos
    }
    return render(request, 'todoapp/todo.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, 'Password must be atleast 3 characterrs')
            return redirect('register')
        
        #If user already exists
        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Error, username already exists')
            return redirect('register')

        new_user = User.object.createuser(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User successfully created, login now!')
    return render(request, 'todoapp/register.html', {})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')

    return render(request, 'todoapp/login.html', {})

def add(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        if task_name:
            Task.objects.create(todo_name=task_name, status=False)
        return redirect('home-page')

@login_required
def delete(request, task_name):
    Task.objects.filter(todo_name=task_name).delete()
    return redirect('home-page')

@login_required
def update(request, task_name):
    task = Task.objects.get(todo_name=task_name)
    task.status = not task.status
    task.save()
    return redirect('home-page')

def logout_user(request):
    logout(request)
    return redirect('login')
