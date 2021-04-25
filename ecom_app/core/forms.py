from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Feedback

class FeedbackForm(forms.Form):
    stars = forms.IntegerField(min_value=0, max_value=5, required=False)
    review = forms.CharField(required=False)

    class Meta:
        model = Feedback