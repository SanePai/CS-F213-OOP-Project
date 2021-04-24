from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile

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
