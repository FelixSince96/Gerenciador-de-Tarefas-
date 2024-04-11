from .models import todo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = todo  

class TodoCreateView(CreateView):
    model = todo
    fields = ["title", "deadline"] 
    success_url = reverse_lazy("todo_list")
    