from django.urls import path
from todolist.views import create_task_ajax, show_json, show_todolist, register, login_user, logout_user, create_task, delete_task, update_task

app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete/<int:pk>', delete_task, name='delete_task'),
    path('update/<int:pk>', update_task, name='update_task'),
    path('json/', show_json, name='show_json'),
    path('add/', create_task_ajax, name='create_task_ajax'),
]