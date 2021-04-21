from django.shortcuts import render
import datetime
from .models import Product
from django.contrib.auth.models import User
prods = Product.objects.all()
def home_view(request):
    profile = User.objects.filter(username = request.user.username).first()
    return render(request, 'core/home.html', context = {"prods": prods})

def about_view(request):
    return render(request, 'core/about.html', context = {"title": "About"})