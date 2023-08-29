from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from .filters import ProductFilter
from .models import Product, Collection, Review, Cart, CartItem, Customer
from .pagination import DefaultPagination
from .permissions import IsAdminOrReadOnly, ViewCustomerHistoryPermissions
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer, CustomerSerializer
# Create your views here.
#####################################################################################3
class ProductViewSet(ModelViewSet): #generic viewset 
    #if we have any logic for the the quertset we can create a function for it and then return 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  
    filterset_class = ProductFilter #add fields we want to filter
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    search_fields = ['title',] #search fields with text data
    ordering_fields = ['unit_price',]
    
    def get_serializer_context(self):
        return {'request': self.request}

####################################################################################
class CollectionViewSet(ModelViewSet): #generic viewset 
    queryset = Collection.objects.all() 
    serializer_class =CollectionSerializer
    
    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response({'error':'collection cannot be deleted'})
        collection.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

###########################################################################################################
class ReviewViewSet(ModelViewSet): #generic viewset 
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_id', 'name']

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])

    def get_serializer_context(self, *args, **kwargs):
        return {'product_id': self.kwargs['product_pk']}
 
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


# class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, permission_classes = ViewCustomerHistoryPermissions)
    def history(self, request, pk):
        return Response('ok')


    @action(detail=False, methods=['GET', 'PUT'], permission_classes = [IsAuthenticated])
    def me(self, request):
        (customer ,created) = Customer.objects.get_or_create(user_id = request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



    

        
