from django.contrib import admin
from django.urls import path, include

from .views import OrderByUser
from django.conf.urls.static import static
from ecom_app import settings

urlpatterns = [
    path('orders/', OrderByUser.as_view(), name="user-orders"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)