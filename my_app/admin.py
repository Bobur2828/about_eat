from django.contrib import admin
from .models import Slider,Product,Category,Places,TypePlaces,SubCategory

admin.site.register([Slider,SubCategory])
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',  'cat_photo','data_created')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price')

@admin.register(Places)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','description','address')


@admin.register(TypePlaces)
class TypePlacesAdmin(admin.ModelAdmin):
    list_display = ('name',)

