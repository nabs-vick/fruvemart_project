from . import views
from django.urls import path

app_name = 'fruit_app'
urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('shopdetails/',views.shopdetails, name='shopdetails'),
    path('shop/',views.shop, name='shop'),
    path('checkout/',views.checkout, name='checkout'),
    path('testimonials/',views.testimonials, name='testimonials'),
    path('cart/',views.cart, name='cart'),
    path('page404/',views.page404, name='404'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register_user, name='register'),
]
