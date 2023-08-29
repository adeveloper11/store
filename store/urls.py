from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collection', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
products_router.register('reviews', views.ReviewViewSet, basename="product-review")
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup = 'cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + products_router.urls + carts_router.urls

#if we have any specific url path then we can include in this.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

# urlpatterns = [
#     path('products/', views.ProductList.as_view(), name = "product_list"),
#     path('products/<int:pk>/', views.ProductDetails.as_view(), name = "product_detrails"),
#     path('collection/', views.CollectionList.as_view(), name = "collection_list"),
#     path('collection/<int:pk>/', views.CollectionDetails.as_view(), name = "collection_details"),
#     path('review/', views.ReviewList.as_view(), name = 'reviewlist')

# ]
