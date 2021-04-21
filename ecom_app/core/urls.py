from django.urls import path, include
from .views import home_view, about_view
from ecom_app import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name = "app-home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)