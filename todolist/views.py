from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from todolist.models import ToDoList
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_data = ToDoList.objects.filter(user=request.user)

    context = {
        "list_of_todos" : todolist_data,
        "username": request.user.username,
    }
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# Code reference: https://docs.djangoproject.com/en/4.1/topics/forms/
@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user

        ToDoList.objects.create(user=user, title=title, description=description)        
        return HttpResponseRedirect('/todolist/')
    
    return render(request, 'create-task.html', {})

@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user

        ToDoList.objects.create(user=user, title=title, description=description)
        return JsonResponse({'error': False})

@login_required(login_url='/todolist/login/')
@csrf_exempt
def update_task(request, pk):
    task_update = ToDoList.objects.get(user=request.user, pk=pk)
    task_update.status = not (task_update.status)
    task_update.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_task(request, pk):
    ToDoList.objects.get(user=request.user,pk=pk).delete()
    return redirect('todolist:show_todolist')
    
@login_required(login_url='/todolist/login/')
def show_json(request):
    data = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')