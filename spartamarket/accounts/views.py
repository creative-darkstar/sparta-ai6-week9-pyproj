from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    render,
    redirect,
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    get_user_model,
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
)
from .forms import CustomUserCreationForm
from products.models import ProductInfo
from datetime import timedelta


def index(request):
    return render(request, "accounts/index.html")


@require_http_methods(["GET", "POST"])
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "products:products"
            return redirect(next_url)
        else:
            return redirect("accounts:log_in")
    else:
        return render(request, "accounts/log-in.html", context={"form": AuthenticationForm()})


@require_POST
def log_out(request):
    auth_logout(request)
    return redirect("index")


@require_http_methods(["GET", "POST"])
def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return redirect("accounts:sign_up")
    else:
        return render(request, "accounts/sign-up.html", context={"form": CustomUserCreationForm()})


def user_profile(request, user_idx):
    user_row = get_object_or_404(get_user_model(), id=user_idx)
    context = {
        "create_dt": (user_row.date_joined + timedelta(hours=9)).strftime("%Y년 %m월 %d일"),
        "user_row": user_row,
    }
    if user_idx == request.user.id:
        add_context = {"products_rows": []}
        for row in user_row.carts.order_by("-create_dt"):
            temp = {
                "idx": row.id,
                "title": row.title,
                "user_username": row.user.username,
                "user_idx": row.user.id,
                "carts": row.cart_users.count,
                "hits": row.hits,
                "create_dt": (row.create_dt + timedelta(hours=9)).strftime("%Y년 %m월 %d일 %I시 %M분 %S초 %p"),
                "update_dt": (row.update_dt + timedelta(hours=9)).strftime("%Y년 %m월 %d일 %I시 %M분 %S초 %p"),
            }
            add_context["products_rows"].append(temp)
        context.update(add_context)
    return render(request, "accounts/user-profile.html", context=context)


@require_POST
def follow(request, user_idx):
    if request.user.is_authenticated:
        me = request.user
        target = get_user_model().objects.get(id=user_idx)
        if me != target:
            if target.followers.filter(id=me.id).exists():
                target.followers.remove(me)
            else:
                target.followers.add(me)
        return redirect('accounts:user_profile', target.id)
    else:
        return redirect('accounts:log_in')


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
