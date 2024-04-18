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


def products(request):
    return render(request, "products/products.html")
# Create your views here.
