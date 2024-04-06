from django.urls import path
from users.views import user_login,user_register,user_logout, ProfileUpdateView,Profile,index

app_name = 'users'

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', Profile.as_view(), name='profile'),
    path('changepassword/', Profile.as_view(), name='profile'),
    path('profile', index, name='profile'),







]