from django.shortcuts import render
import datetime
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import logout

prods = Product.objects.all()
def home_view(request):
    try:
        just_logged_out = request.session.get('just_logged_out',False)
    except:
        just_logged_out = False
    profile = User.objects.filter(username = request.user.username).first()
    return render(request, 'core/home.html', context = {"prods": prods, "just_logged_out": just_logged_out})

def about_view(request):
    return render(request, 'core/about.html', context = {"title": "About"})

def logout_view(request):
    logout(request)