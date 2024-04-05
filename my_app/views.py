from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Slider, Category,Places,Product,SubCategory
def index(request):
    slider=Slider.objects.all()
    places=Places.objects.all()
    data={
        'slider': slider,
        'places': places,
    }
    return render(request, 'my_app/index.html', context=data)


def detail(request, id):    #restoran ichidagi malumotlarni korish uchun 
    place = Places.objects.get(id=id)
    categories1 = SubCategory.objects.filter(products__restaurant=place).distinct()
    products = Product.objects.filter(restaurant=place)
    data = {
        'place': place,
        'categories1': categories1,
        'products': products,
    }
    return render(request, 'my_app/detail2.html', context=data)

def detail2(request, place_id, cat_id):    #restoran ichidagi categorylar malumotini korish uchun 
    place = get_object_or_404(Places, id=place_id)
    subcategory = get_object_or_404(SubCategory, id=cat_id)
    category = subcategory.subcat
    categories1 = SubCategory.objects.filter(products__restaurant=place).distinct()
    products = Product.objects.filter(category=subcategory)
    data = {
        'place': place,
        'categories1': categories1,
        'products': products,
    }
    return render(request, 'my_app/detail2.html', context=data)



def error(request):
    return render(request, 'my_app/404.html')

def checkout(request):
    return render(request, 'my_app/checkout.html')




def showeat(request, id):

    subcategory = get_object_or_404(SubCategory, id=id)
    category = subcategory.subcat
    products = Product.objects.filter(category=subcategory)
    data = {
        'products': products,
    }
    return render(request, 'my_app/showeat1.html', context=data)

def extra(request):
    return render(request, 'my_app/extra.html')

def intro(request):
    return render(request, 'my_app/intro.html')

def invoice(request):
    return render(request, 'my_app/invoice.html')


def listing(request):
    place=Places.objects.order_by('name')
    data={
        'place': place,
    }
    return render(request, 'my_app/restoran.html', context=data)

def listingshow(request,id):
    place=Places.objects.filter(id=id)
    data={
        'place': place,
    }
    return render(request, 'my_app/restoran.html', context=data)


def showcategory(request, id):
    subcategory = get_object_or_404(SubCategory, id=id)
    category = subcategory.subcat
    products = Product.objects.filter(category=subcategory)
    data = {
        'products': products,
    }
    return render(request, 'my_app/showeat.html', context=data)
def showcategory1(request, id):
    category = get_object_or_404(Category, id=id)
    subcategories = SubCategory.objects.filter(subcat=category)
    products = Product.objects.filter(category__in=subcategories)
    data = {
        'products': products,
    }
    return render(request, 'my_app/showeat.html', context=data)

def login(request):
    return render(request, 'my_app/login.html')

def offers(request):
    return render(request, 'my_app/offers.html')

def orders(request):
    return render(request, 'my_app/orders.html')

def register(request):
    return render(request, 'my_app/register.html')

def thanks(request):
    return render(request, 'my_app/thanks.html')

def track_order(request):
    return render(request, 'my_app/track-order.html')