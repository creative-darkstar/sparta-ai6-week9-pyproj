from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("/", views.products, name="products"),
    # path("log-out/", views.log_out, name="log_out"),
    # path("sign-up/", views.sign_up, name="sign_up"),
    # path("<str:username>/", views.user_profile, name="user_profile"),
    # path("edit/", views.user_profile_edit, name="user_profile_edit"),
    # path("delete/", views.user_profile_delete, name="user_profile_delete"),
]