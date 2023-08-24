from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection

        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description","slug","inventory","unit_price", 'price_with_tax','collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax') #created new field , not exist in database
    # collection = serializers.StringRelatedField()  #use default method used in models 
    # collection = CollectionSerializer() # using collectionSerializers class defined above.
    

    # funnction used to create custom data
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']
    # products_count = serializers.IntegerField()