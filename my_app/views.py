from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Slider, Category,Places,Product,SubCategory,TypePlaces,Comment
from .forms import ContactForm,AddCommentForm
from .telegram import send_sms
import asyncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .like import Like
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Slider
from django.db.models import Q
from django.contrib import messages
from users.models import User

def index(request):
    search = request.GET.get('q', '')
    products = Product.objects.select_related('category', 'restaurant').all()
    
    if search:
        products = products.filter(
            Q(name__icontains=search) | 
            Q(category__subcat_name__icontains=search)|
            Q(restaurant__name__icontains=search)
        )
        data = {
            'products': products,
        }
        return render(request, 'my_app/showeat.html', context=data)
    slider = Slider.objects.all()
    data = {
        'slider': slider,
        'products': products,
    }
    return render(request, 'my_app/index.html', context=data)


class DetailView(View):
    def get(self, request, id):
        place = get_object_or_404(Places, id=id)
        categories1 = SubCategory.objects.filter(products__restaurant=place).distinct()
        products = Product.objects.filter(restaurant=place).select_related('restaurant')
        formContact = ContactForm()
        formComment = AddCommentForm()
        stars = Comment.objects.filter(places=place)
        star_values = stars.values_list('stars_given', flat=True)
        search=request.GET.get('q','')
        
        if star_values:
            result1 = round(sum(star_values) / len(star_values))
        else:
            result1 = 0
        if search:
            products = products.filter(name__icontains=search)
        data = {
            'place': place,
            'categories1': categories1,
            'products': products,
            'formContact': formContact,
            'formComment': formComment,
            'result1': result1,
        }
        return render(request, 'my_app/detail2.html', context=data)

    def post(self, request, id):
        formContact = ContactForm(request.POST)
        formComment = AddCommentForm(request.POST)
        place = get_object_or_404(Places, id=id)

        if formComment.is_valid():
            if request.user.is_authenticated:
                user = request.user  
            else:
                anonymous_user = User.objects.get_or_create(username='Nomalum Mijoz')[0]
                user = anonymous_user
            
            Comment.objects.create(
                user=user,
                places=place,
                comment=formComment.cleaned_data['comment'],
                stars_given=formComment.cleaned_data['stars_given'],
            )
            messages.success(request, "Sizning sharhingiz qoldirildi")

            return redirect(reverse('detail', kwargs={'id': place.id}))
        
        if formContact.is_valid():
            message = (
                    f"Foydalanuvchi: Ismi={formContact.cleaned_data['fullname']}\n"
                    f"Email={formContact.cleaned_data['email']}\n"
                    f"Telefon={formContact.cleaned_data['phone']}\n"
                    f"Xabar={formContact.cleaned_data['text']}"
                    )
            asyncio.run(send_sms(message))
            messages.success(request, "Sizning xabaringiz yuborildi")
            return redirect('detail', id=place.id)
        
        categories1 = SubCategory.objects.filter(products__restaurant=place).distinct()# Restorandagi mahsulotlar bo'yicha ajratilgan toifalarni takrorlamedi
        products = Product.objects.filter(restaurant=place).select_related('restaurant')
        data = {
            'place': place,
            'categories1': categories1,
            'products': products,
            'formContact': formContact,
        }
        return render(request, 'my_app/detail2.html', context=data)

def detail2(request, place_id, cat_id):
    place = get_object_or_404(Places, id=place_id)
    subcategory = get_object_or_404(SubCategory, id=cat_id)

    products = Product.objects.filter(category=subcategory).prefetch_related(
        'type_place', 'sub', 'category', 'restaurant'
    )

    data = {
        'place': place,
        'categories1': place.subcategory_set.distinct(),
        'products': products,
    }
    return render(request, 'my_app/detail2.html', context=data)

def list_places(request, id):
    type_place = get_object_or_404(TypePlaces, id=id)
    place = Places.objects.filter(type_place=type_place).select_related('type_place')
    return render(request, 'my_app/restoran.html', {'place': place})

def show_category(request, id):
    category = get_object_or_404(Category, id=id)
    subcategories = SubCategory.objects.filter(subcat=category).select_related('subcat')
    products = Product.objects.filter(category__in=subcategories).select_related('category')
    return render(request, 'my_app/showeat.html', {'products': products})



    
def listing(request):
    place=Places.objects.order_by('name').select_related('type_place')
    data={
        'place': place,
    }
    return render(request, 'my_app/restoran.html', context=data)

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







def like_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        liked_products = request.session.get('liked_products', [])
        if product_id and action == 'post':
            product = get_object_or_404(Product, id=product_id)

            liked_products = request.session.get('liked_products', [])

            if product_id not in liked_products:
                liked_products.append(product_id)
                request.session['liked_products'] = liked_products

            like_count = len(liked_products)
            return JsonResponse({"like_count": like_count})

    return JsonResponse({"error": "Invalid request"})