from .filters import ProductFilter
from .models import Product, Collection, Review, Cart, CartItem
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from django.shortcuts import get_object_or_404, render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin  
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
#####################################################################################3
class ProductViewSet(ModelViewSet): #generic viewset 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  
    filterset_class = ProductFilter #waht fields we want to filter
    pagination_class = PageNumberPagination
    search_fields = ['title',] #search fields with text data
    ordering_fields = ['unit_price',]

    
    def get_serializer_context(self):
        return {'request': self.request}
# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.all() 
#     serializer_class = ProductSerializer
#     def get_serializer_context(self):
#         return {'request': self.request}

    # def get(self, request):
    #     queryset = Product.objects.select_related('collection').all() 
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)
    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)

# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all() 
#     serializer_class = ProductSerializer
    
# class ProductDetails(APIView):
#     def get(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     def put(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def patch(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product, data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
####################################################################################3
class CollectioViewSet(ModelViewSet): #generic viewset 
    queryset = Collection.objects.all() 
    serializer_class =CollectionSerializer
# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.all() 
#     serializer_class =CollectionSerializer

# class CollectionList(APIView):
#     def get(self, request):
#         queryset = Collection.objects.all() 
#         serializer =CollectionSerializer(queryset, many = True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid()
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class CollectionDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.all() 
#     serializer_class = CollectionSerializer       
    
# @api_view(['GET', 'PUT','PATCH', 'DELETE'])
# def collection_details(request, id):
#     collection = get_object_or_404(Collection, pk=id)
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method =="PUT":
#         serializer = CollectionSerializer(collection, data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method =="PATCH":
#         serializer = CollectionSerializer(collection, data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
###########################################################################################################
class ReviewViewSet(ModelViewSet): #generic viewset 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id', 'name']
    # def get_serializer_context(self):
    #     return {'request': self.request}
    # def get_queryset(self):  #custum queryset for selecting product automatically
    #     return Review.objects.filter(product_id = self.kwargs['product_pk'])
    # serializer_class = ReviewSerializer
    
    # def get_serializer_context(self):
    #     return {"product_id" : self.kwargs['product_pk']}

# class CartViewSet(ModelViewSet): #using cutome method
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

#IN CART WE DONT HAVE TO PERFORM THAT MUCH OF OPERATION LIKE UPDATING TO WE ARE NOT USING MODELVIEWSET
class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin, GenericViewSet): #using custum method
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet): #using cutome method
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])


# class ReviewList(ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class ReviewDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
        
