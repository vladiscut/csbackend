from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from import_export.admin import ImportExportModelAdmin

from .models import (Category, Product, Review, ProductImage, ProductSpecification, ProductSpecificationValue, ProductType, Discount)




class MPTTModelAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name","parent")}

admin.site.register(Category, MPTTModelAdmin)
# Register your models here.

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review

class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]