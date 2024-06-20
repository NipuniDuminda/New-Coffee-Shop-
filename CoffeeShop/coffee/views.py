from django.shortcuts import render
from .models import Coffee

def home_view(request):
    coffees = Coffee.objects.all()
    context = {'coffee_list': coffees}
    return render(request, 'home.html', context)  