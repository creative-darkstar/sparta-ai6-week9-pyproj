from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("log-in/", views.log_in, name="log_in"),
    path("log-out/", views.log_out, name="log_out"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("<int:user_idx>/", views.user_profile, name="user_profile"),
    path('<int:user_idx>/follow/', views.follow, name='follow'),
    path("edit/", views.user_profile_edit, name="user_profile_edit"),
    path("delete/", views.user_profile_delete, name="user_profile_delete"),
]