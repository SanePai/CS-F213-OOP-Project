from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'user_type']
# Create your views here.
    
def updateProfile(request, username):
    user = request.user
    if request.method == 'POST':
        form = request.POST
        user.first_name = form.get('first_name')
        user.last_name = form.get('last_name')
        user.email = form.get('email')
        p = user.profile
        p.location = form.get('location')
        p.state = form.get('state')
        p.country = form.get('country')
        p.save()
        user.profile = p
        user.save()
        update_session_auth_hash(request, user)
        print("Saved user profile!")
        messages.success(request, f'Profile updated succesfully!')
        return render(request, 'users/update_profile.html', {'user': user})

    return render(request, 'users/update_profile.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data.get('username'))
            form2 = request.POST
            profile = Profile.objects.create(user_type=form.cleaned_data.get('user_type'), user=user, location=form2.get('location'), state=form2.get('state'), country=form2.get('country'))
            profile.save()
            user.profile = profile
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
