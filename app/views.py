# Django Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages

# User imports

#----------------------------------------------------------

class Homeview(View):
    def get(self, request):
        return render(request, "app/home.html")

