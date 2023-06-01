from django.shortcuts import render
# to display lists and details
from django.views.generic import ListView, DetailView
from .models import Recipe  # to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


def welcome(request):
    return render(request, 'recipes/recipes_home.html')


class RecipeListView(LoginRequiredMixin, ListView):  # class-based 'protected' view
    model = Recipe  # specify model
    template_name = 'recipes/main.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based 'protected' view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'  # specify template
