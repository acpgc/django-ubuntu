from django.contrib import admin
from django.urls import path, include
from .view import StocksView


urlpatterns = [
    path('get_data/', StocksView.as_view({
        "get" : "list",
        "post": "create"
    })),
]
