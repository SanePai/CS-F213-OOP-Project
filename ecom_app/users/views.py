from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile
from django.views.generic import ListView
from core.models import Order, Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get('username'))
            form2 = request.POST
            profile = Profile.objects.create(user_type=form.cleaned_data.get('user_type'), user=user, location=form2.get('location'))
            profile.save()
            user.profile = profile
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class OrderByUser(LoginRequiredMixin, ListView):
        model = Order
        template_name = 'users/user_orders.html'
        context_object_name = 'prods'
        paginate_by = 20

        def get_queryset(self):
            user = get_object_or_404(User, username=self.kwargs.get('username'))
            return Order.objects.filter(customer=user, complete=True)
        
        def get_context_data(self, **kwargs):
            url = self.request.get_full_path()
            username = url.split("/")[-3]
            context = super().get_context_data(**kwargs)
            context['username'] = username
            return context
