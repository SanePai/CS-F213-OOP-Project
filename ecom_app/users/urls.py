from django.contrib import admin
from django.urls import path, include
from .views import updateProfile
from django.conf.urls.static import static
from ecom_app import settings
urlpatterns = [
    path('', updateProfile, name="profile-update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)