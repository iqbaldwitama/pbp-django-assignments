from django.forms import ModelForm
from todolist.models import ToDoList

class ToDoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ["title", "description"]