from rest_framework import serializers

from .models import Category, Product, ProductImage, Review, ProductType, ProductSpecification,ProductSpecificationValue


class SpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationValue
        fields = ['value','product_id','id','specification_id']

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
    
class ParentParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','slug','id','parent')

class ParentSerializer(serializers.ModelSerializer):
    parent = ParentParentSerializer()
    class Meta:
        model = Category
        fields = ('name','slug','id','parent')

class ProductSpecificationSerializer(serializers.ModelSerializer):
    specificationValue = SpecificationValueSerializer(many=True)
    class Meta:
        model = ProductSpecification
        fields = '__all__'


class ProducTypeSerializer(serializers.ModelSerializer):
    specifications = ProductSpecificationSerializer(many=True)
    class Meta:
        model = ProductType
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    parent = ParentSerializer()
    class Meta:
        model = Category
        fields=['id', 'name', 'children', 'slug','parent']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    product_type = ProducTypeSerializer()
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = ["id", "category", "title", "reviews", "description","product_type","slug","regular_price","price", "product_image"]


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["name", "slug", "id","children"]