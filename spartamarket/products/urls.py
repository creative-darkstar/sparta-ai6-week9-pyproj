from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.products, name="products"),
    path("<int:product_idx>/", views.product_detail, name="product_detail"),
    path("write/", views.product_write, name="product_write"),
    path("<int:product_idx>/update/", views.product_update, name="product_update"),
    path("<int:product_idx>/delete/", views.product_delete, name="product_delete"),
]