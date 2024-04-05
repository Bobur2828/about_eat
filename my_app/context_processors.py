from . models import Category,Product,Places,SubCategory


def categories(request):
    categories=Category.objects.all()

    return {'categories': categories}

def random_restaurants(request):
    random_restaurants=Places.objects.order_by(('?'))[:4]
    return {'random_restaurants': random_restaurants}

def restaurants(request):
    restaurants=Places.objects.order_by(('name'))
    return {'restaurants': restaurants}

def subcategories(request):
    subcategories=SubCategory.objects.all()
    return {'subcategories': subcategories}

