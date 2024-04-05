
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('error404/', views.error, name='error'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('extra', views.extra, name='extra'),
    path('intro/', views.intro, name='intro'),
    path('invoice/', views.invoice, name='invoice'),
    path('listing/', views.listing, name='listing'),
    path('listing/<int:id>', views.showcategory, name='listingshow'),
    path('listing1/<int:id>', views.showcategory1, name='listing1'),
    path('showeat/<int:id>', views.showeat, name='showeat'),
    path('showcat/<int:place_id>/<int:cat_id>/', views.detail2, name='showcat'),
    
    path('login/', views.login, name='login'),
    path('offers/', views.offers, name='offers'),
    path('orders/', views.orders, name='orders'),
    path('register/', views.register, name='register'),
    path('thanks/', views.thanks, name='thanks'),
    path('track-order/', views.track_order, name='track_order'),
    path('showcategory/<int:id>', views.showcategory, name='showcategory'),

]
