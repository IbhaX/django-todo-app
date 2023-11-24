# Django Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages


# User imports
from .models import Todo
from .forms import TodoForm
#----------------------------------------------------------

class Homeview(View):
    def get(self, request):
        context = {"todos": Todo.objects.all(), "form": TodoForm}
        return render(request, "app/home.html", context)
    
    def post(self, request):
        
        form = TodoForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Todo saved successfully!!")
            return redirect("app:home")
  


def delete(request, pk):
    if request.method == "POST":
        todo = Todo.objects.filter(id=pk)
        todo.delete()
        messages.success(request, "Todo DELETED Successfully")
        return redirect("app:home")

def complete(request, pk):
    todo = Todo.objects.filter(id=pk).first()
    if request.method == "POST":
        if todo.completed == False:
            todo.completed = True
        else:
            todo.completed = False
        todo.save()
        messages.success(request, "Marked complete")
        return redirect("app:home")