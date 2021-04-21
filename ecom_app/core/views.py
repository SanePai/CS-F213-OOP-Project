from django.shortcuts import render
import datetime
from django.contrib.auth.models import User
prods = [
    {
        "seller": "Seller1",
        "date_posted": datetime.datetime.now(),
        "title": "Book1",
        "content": "This is a book. Book1 asfbkjabsfjk vadvdnkvaknsbjvb a,fjvbk nbjak xnvjbs nafvcjna sfmnvacx kavmsfdvbnc kxhcnvamsnvdkbc sdvafndvkbs damfdnc ",
        "img_src": "https://specials-images.forbesimg.com/imageserve/5f85be4ed0acaafe77436710/960x0.jpg?fit=scale",

    },
    {
        "seller": "Seller1",
        "date_posted": datetime.datetime.now(),
        "title": "Book1",
        "content": "This is a book. Book1 asfbkjabsfjk vadvdnkvaknsbjvb a,fjvbk nbjak xnvjbs nafvcjna sfmnvacx kavmsfdvbnc kxhcnvamsnvdkbc sdvafndvkbs damfdnc ",
        "img_src": "https://specials-images.forbesimg.com/imageserve/5f85be4ed0acaafe77436710/960x0.jpg?fit=scale",

    },
    {
        "seller": "Seller1",
        "date_posted": datetime.datetime.now(),
        "title": "Book1",
        "content": "This is a book. Book1 asfbkjabsfjk vadvdnkvaknsbjvb a,fjvbk nbjak xnvjbs nafvcjna sfmnvacx kavmsfdvbnc kxhcnvamsnvdkbc sdvafndvkbs damfdnc ",
        "img_src": "https://specials-images.forbesimg.com/imageserve/5f85be4ed0acaafe77436710/960x0.jpg?fit=scale",

    },
]


def home_view(request):
    profile = User.objects.filter(username = request.user.username).first()
    return render(request, 'core/home.html', context = {"prods": prods, "profile": profile})

def about_view(request):
    return render(request, 'core/about.html', context = {"title": "About"})