from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name = "product_list"),
    path('products/<int:id>/', views.product_details, name = "product_detrails"),
    path('collection/', views.collection_list, name = "collection_list"),
    path('collection/<int:id>/', views.collection_details, name = "collection_details"),

]
