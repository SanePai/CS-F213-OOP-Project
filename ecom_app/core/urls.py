from django.urls import path, include
from ecom_app import settings
from django.conf.urls.static import static
from core.views import (
    cart,
    ProductListView,
    ProductCreateView,
    SellerProductListView,
    ProductDeleteView,
    ProductUpdateView,
    ProductDetailView,
    search,
    checkout,
    address_helper,
    )
urlpatterns = [
    path('', ProductListView.as_view(), name = "app-home"),
    path('cart/', cart, name = "cart"),
    path('vendor/<str:username>', SellerProductListView.as_view(), name='seller-prods'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='prod-detail'),
    path('product/new/', ProductCreateView.as_view(), name='prod-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='prod-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(template_name = 'core/prod_confirm_delete.html'), name='prod-delete'),
    path('search', search),
    path('checkout', checkout),
    path('address_help', address_helper),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)