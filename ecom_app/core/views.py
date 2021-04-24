from django.shortcuts import render
import datetime
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

prods = Product.objects.all()
class ProductListView(ListView):
    model = Product
    template_name = 'core/home.html'
    context_object_name = 'prods'
    ordering = ['-date_posted']
    paginate_by = 20

def home_view(request):
    profile = User.objects.filter(username = request.user.username).first()
    return render(request, 'core/home.html', context = {"prods": prods})

def logout_view(request):
    logout(request)

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ['title', 'content', 'img', 'stock', 'tags', 'measurment_unit', 'price_per_unit']
    success_url = "/"

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return (self.request.user.profile.user_type == "WHOLESALER") or (self.request.user.profile.user_type == "RETAILER")

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'content', 'stock']
    template_name = 'core/prod_update.html'
    context_object_name = 'prod'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return (self.request.user == product.seller)



class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        return (self.request.user == product.seller)

class SellerProductListView(ListView):
    model = Product
    template_name = 'core/seller_prods.html'
    context_object_name = 'prods'
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(seller=user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context = super().get_context_data(**kwargs)
        context['seller'] = user
        return context

class ProductDetailView(DetailView):
    model = Product

def search(request):
    if request.method == 'POST':
        form = request.POST
        search_q = form.get('search')
        results = Product.objects.filter(Q(title__icontains=search_q) | Q(content__icontains=search_q))
        return render(request, 'core/home.html', context = {"prods": results})

@login_required
def cart(request):
    return render(request, 'core/cart.html', {})
