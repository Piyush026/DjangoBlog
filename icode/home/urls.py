from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about,name='about'),
    path('search/',views.search,name="search"),
    path('signup/',views.signup,name="signup"),
    path('login',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    
    
    
    

]