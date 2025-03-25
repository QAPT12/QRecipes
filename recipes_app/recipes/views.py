from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipes_index(request):
    return render(request, "recipes.html")