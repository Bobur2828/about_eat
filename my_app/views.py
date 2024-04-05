from django.shortcuts import render
from .models import Slider, Category,Places,Product,SubCategory
def index(request):
    slider=Slider.objects.all()
    places=Places.objects.all()
    data={
        'slider': slider,
        'places': places,
    }
    return render(request, 'my_app/index.html', context=data)

def error(request):
    return render(request, 'my_app/404.html')

def checkout(request):
    return render(request, 'my_app/checkout.html')

def detail(request, id):
    place = Places.objects.get(id=id)
    categories = SubCategory.objects.filter(products__restaurant=place).distinct()
    return render(request, 'my_app/detail2.html', {'place': place, 'categories': categories})



def extra(request):
    return render(request, 'my_app/extra.html')

def intro(request):
    return render(request, 'my_app/intro.html')

def invoice(request):
    return render(request, 'my_app/invoice.html')

def listing(request):
    show='a'
    data={
        'show': show,
    }
    return render(request, 'my_app/listing.html', context=data)

def showcategory(request,id):
    show=Category.objects.filter(id=id)
    data={
        'show': show,
    }
    return render(request, 'my_app/listing.html', context=data)
    

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