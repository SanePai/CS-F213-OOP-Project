from django.shortcuts import render
from django.http import JsonResponse
import datetime
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from core.models import Feedback, Order, OrderItem
import json
from .forms import FeedbackForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied

class ProductListView(ListView):
    model = Product
    template_name = 'core/home.html'
    context_object_name = 'prods'
    ordering = ['-date_posted']
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        customer = self.request.user
        if self.request.user.is_authenticated:
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cartItems = order.get_cart_items
            context['cartItems'] = cartItems
        return context

class home_view(ListView):
    model = Product
    template_name = 'core/home.html'
    context_object_name = 'prods'
    paginate_by = 20

    def get_queryset(self):
        tags = self.kwargs['tags']
        print(tags)
        return Product.objects.filter(tags=tags).order_by('-date_posted')
 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        customer = self.request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        context['cartItems'] = cartItems
        return context

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

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        customer = self.request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        context['cartItems'] = cartItems
        return context


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'content', 'img', 'stock', 'tags', 'measurment_unit', 'price_per_unit']
    template_name = 'core/prod_update.html'
    context_object_name = 'prod'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return (self.request.user == product.seller)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        customer = self.request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        context['cartItems'] = cartItems
        return context

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        return (self.request.user == product.seller)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        customer = self.request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        context['cartItems'] = cartItems
        return context

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
        customer = self.request.user
        if self.request.user.is_authenticated:
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cartItems = order.get_cart_items
            context['cartItems'] = cartItems
        return context

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        customer = self.request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
        context['cartItems'] = cartItems
        return context

def search(request):
    if request.method == 'POST':
        form = request.POST
        search_q = form.get('search').lower()
        results = Product.objects.filter(Q(title__icontains=search_q) | Q(content__icontains=search_q) | Q(tags__icontains=search_q))
        return render(request, 'core/home.html', context = {"prods": results})

@login_required
def checkout(request):
    if request.method == 'GET':
        order = Order.objects.filter(customer = request.user, complete=False).first()
        orderitem = order.orderitem_set.all()
        cartItems = order.get_cart_items
        order_total = order.get_cart_total
        return render(request, 'core/checkout.html', context={"cartItems": cartItems, "order_total": order_total, "orderitem":orderitem})
    
    if request.method == 'POST':
        form = request.POST
        order = Order.objects.filter(customer = request.user, complete=False).first()
        order.complete = True
        order.allow_review = True
        order.save()
        
        return render(request, 'core/order_successful.html', context = {"order": order})

def address_helper(request):
    if request.method == 'GET':
        return HttpResponse('Hey')

    if request.method == 'POST':
        countryArr = {"United States":["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
, "India":["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]}
        req_country = request.POST.get("country")
        response = "<label>State</label><select name=\"state\" class=\"custom-select d-block w-100\" id=\"state\" name=\"state\">"
        for x in countryArr[req_country]:
            response += "<option>" + x + "</option>"
        response += "</select>"
        return HttpResponse(response)

@login_required
def cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer = customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    return render(request, 'core/cart.html', {"items": items, "order": order, "cartItems": cartItems})

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Action: ", action)
    print("productId: ", productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse({"Data": " "})


@login_required
def add_feedback(request, pk1, pk2):
    form = FeedbackForm()
    order = Order.objects.get(id=pk1)
    product = Product.objects.get(id=pk2)
    if order.customer != request.user:
        raise PermissionDenied()
    feedback, created = Feedback.objects.get_or_create(order=order, product=product, user=request.user)
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback.stars = form.cleaned_data.get('stars')
            feedback.review = form.cleaned_data.get('review')
            feedback.save()
            messages.success(request, f"Thank you for providing feedback")
            return redirect('user-orders', feedback.user.username)
        return render(request, 'core/prod_review.html', {"form": form, "created": created, "feedback": feedback, "cartItems": cartItems})

    else:
        form = FeedbackForm()
        return render(request, 'core/prod_review.html', {"form": form, "created": created, "feedback": feedback, "cartItems": cartItems})

@login_required
def order_details(request, pk):
    order_items = Order.objects.get(id=pk).orderitem_set.all()
    order = order_items[0].order
    # prods = [item.product for item in order_items]
    feedback_list = Feedback.objects.filter(order=order)
    if order.customer != request.user:
        raise PermissionDenied()
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items
    context = {
        "order_items": order_items,
        "order": order,
        "feedback_list": feedback_list
    }
    context['cartItems'] = cartItems

    return render(request, 'core/order_detail.html', context = context)