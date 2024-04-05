from django.db import models

class BaseModel(models.Model):
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True 

class Slider(models.Model):
    text1=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='Slider/photo')

    def  __str__(self):
        return self.text1
    
class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Mahsulot nomini kiriting')
    description = models.TextField(max_length=1500,verbose_name='Mahsulotga batafsil tarif')
    price = models.DecimalField(max_digits=10, decimal_places=0,default='0',verbose_name='Narxni belgilang')
    photo = models.ImageField(upload_to="product/photo",   verbose_name='Tovar fotosini kiriting')
    category = models.ForeignKey('SubCategory', verbose_name='Kategoriyani tanlang', on_delete=models.CASCADE,related_name="products")
    photo = models.ImageField(upload_to="product/photo",   verbose_name='Tovar fotosini kiriting')
    restaurant=models.ForeignKey('Places', verbose_name='Restoranni tanlang', on_delete=models.CASCADE,related_name="products1")


class Places(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='place_images/')
    type_place = models.ForeignKey('TypePlaces', verbose_name='Ovqatlanish maskani turini tanlang', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Category(BaseModel):
    cat_name = models.CharField(max_length=100, verbose_name='Kategoriya nomini kiriting')
    cat_photo = models.ImageField(upload_to="category/photo", blank=True, default=None,null=True,  verbose_name='Categoriya uchun foto 370x240 olchamda')
    def __str__(self):
        return self.cat_name
class SubCategory(BaseModel):
    subcat_name = models.CharField(max_length=100, verbose_name='Kategoriya nomini kiriting')
    subcat_photo = models.ImageField(upload_to="category/photo", blank=True, default=None,null=True,  verbose_name='Categoriya uchun foto 370x240 olchamda')
    subcat = models.ForeignKey('Category', verbose_name='Ovqatlanish maskani turini tanlang', on_delete=models.CASCADE, related_name='subcategory')
    def __str__(self):
        return self.subcat_name
class TypePlaces(BaseModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name



