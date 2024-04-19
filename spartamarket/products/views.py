from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    render,
    redirect,
)
from django.contrib.auth.models import User
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
)
from django.contrib.auth.decorators import login_required
from .models import ProductInfo, HashtagInfo, CommentInfo
from .forms import ProductInfoModelForm
from datetime import timedelta


@login_required
@require_http_methods(["GET", "POST"])
def products(request):
    context = {"rows": []}
    for row in ProductInfo.objects.filter(is_visible=True).order_by("-create_dt"):
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
        context["rows"].append(temp)
    return render(request, "products/products.html", context=context)


@login_required
@require_http_methods(["GET", "POST"])
def product_detail(request, product_idx):
    row = get_object_or_404(ProductInfo, id=product_idx)
    context = {
        "idx": product_idx,
        "title": row.title,
        "user_username": row.user.username,
        "user_idx": row.user.id,
        "hits": row.hits,
        "content": row.content,
        "image": row.image,
        "create_dt": (row.create_dt + timedelta(hours=9)).strftime("%Y년 %m월 %d일 %I시 %M분 %S초 %p"),
        "update_dt": (row.update_dt + timedelta(hours=9)).strftime("%Y년 %m월 %d일 %I시 %M분 %S초 %p"),
    }
    return render(request, "products/product-detail.html", context=context)


@login_required
@require_http_methods(["GET", "POST"])
def product_write(request):
    if request.method == "POST":
        form = ProductInfoModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect("products:product_detail", new_product.id)
        else:
            return redirect("products:product_write")
    else:
        context = {
            "form": ProductInfoModelForm()
        }
        return render(request, "products/product-write.html", context=context)


@login_required
@require_http_methods(["GET", "POST"])
def product_update(request, product_idx):
    update_row = get_object_or_404(ProductInfo, id=product_idx)

    if request.method == "POST":
        form = ProductInfoModelForm(request.POST, request.FILES, instance=update_row)
        if form.is_valid():
            form.save()
            return redirect("products:product_detail", product_idx)
        else:
            return redirect("products:product_update", product_idx)
    else:
        context = {
            "idx": product_idx,
            "form": ProductInfoModelForm(instance=update_row),
        }
        return render(request, "products/product-update.html", context=context)


@login_required
@require_POST
def product_delete(request, product_idx):
    if request.user.is_authenticated:
        delete_row = get_object_or_404(ProductInfo, id=product_idx)
        delete_row.is_visible = False
        delete_row.save()
        return redirect("products:products")
