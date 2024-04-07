
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>', views.DetailView.as_view(), name='detail'),
    path('listing/', views.listing, name='listing'),
    path('listing/<int:id>', views.showcategory, name='listingshow'),
    path('listing1/<int:id>', views.showcategory1, name='listing1'),
    path('showeat/<int:id>', views.showeat, name='showeat'),
    path('showeats/', views.showeat, name='showeats'),
    path('showcat/<int:place_id>/<int:cat_id>/', views.detail2, name='showcat'),
    path('listplace/<int:id>', views.list_places, name='listplace'),
    path('showcat/<int:id>', views.show_category, name='showcat'),
    path('showcategory/<int:id>', views.showcategory, name='showcategory'),
    path('like_add/',views.like_add,name='like_add'),
]
