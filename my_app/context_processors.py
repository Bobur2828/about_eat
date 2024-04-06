from . models import Category,Product,Places,SubCategory,TypePlaces


def categories(request):
    categories=Category.objects.order_by('cat_name')

    return {'categories': categories}

def random_restaurants(request):
    random_restaurants = Places.objects.order_by('?')[:4].select_related('type_place')
    return {'random_restaurants': random_restaurants}


def restaurants(request):
    restaurants=Places.objects.order_by(('name')).select_related('type_place')
    return {'restaurants': restaurants}

def subcategories(request):
    subcategories=SubCategory.objects.all().select_related('subcat')
    return {'subcategories': subcategories}

def typeplaces(request):
    typeplaces=TypePlaces.objects.order_by('name')
    return {'typeplaces': typeplaces}

def view_liked(request):
    liked_product_ids = request.session.get('liked_products', [])
    liked_products = Product.objects.filter(id__in=liked_product_ids)
    total_price = 0
    for product in liked_products:
        total_price += product.price
    context = {
        'liked_products': liked_products,
        'total_price': total_price
    }
    return context

