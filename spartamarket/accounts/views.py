from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    render,
    redirect,
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
)
# from .forms import CustomUserChangeForm


def index(request):
    return render(request, "accounts/index.html")


@require_http_methods(["GET", "POST"])
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "index"
            return redirect(next_url)
        else:
            return redirect("accounts:login")
    else:
        return render(request, "accounts/log-in.html", context={"form": AuthenticationForm()})


@require_POST
def log_out(request):
    auth_logout(request)
    return redirect("index")


@require_http_methods(["GET", "POST"])
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return redirect("accounts:signup")
    else:
        return render(request, "accounts/sign-up.html", context={"form": UserCreationForm()})


def user_profile(request, username):
    return render(request, "accounts/user-profile.html")


def user_profile_edit(request):
    return render(request, "accounts/user-profile-edit.html")


@require_POST
def user_profile_delete(request):
    if request.user.is_authenticated:
        user_row = get_object_or_404(User, id=request.user.id)
        user_row.is_active = 0
        user_row.save()
        auth_logout(request)
        return redirect("index")
