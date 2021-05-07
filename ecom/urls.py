"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blogsingle/',views.blogsingle,name='blog-single'),
    path('blog/',views.blog,name='blog'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('productsingle/',views.productsingle,name='productsingle'),
    path('shop/<int:id>',views.shop,name='shop'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('buynow/<int:id>',views.buynow,name='buynow'),
    path('login/',views.login1,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout1,name='logout'),
    path('order/',views.order,name='order'),
    path('thankyou/',views.thankyou,name='thankyou'),
    path('remove_item/',views.remove_item,name='remove_item'),
    path('payment/',views.payment,name='payment'),
    path('plus/',views.plus,name='plus'),
    path('minus/',views.minus,name='minus'),
    path('remove/<int:id>/',views.remove,name='remove'),
    path('success/<oid>/',views.thankyou,name='thankyou'),
    path('trackorder/',views.trackorder,name='trackorder'),
    path('account/', include('allauth.urls')),
    path('s_add_to_cart/',views.s_add_to_cart,name='s_add_to_cart'),
   

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
