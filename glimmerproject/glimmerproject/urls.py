"""
URL configuration for glimmerproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from glimmerapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path("bag/",views.bag, name="bag"),
    path("movetobag/<int:product_id>",views.movetobag, name="movetobag"),
    path("removefrombag/<int:product_id>",views.removefrombag, name="removefrombag"),
    path("updateqty/<qv>/<product_id>", views.updateqty, name="updateqty"),
    path("makeup/",views.makeup, name="makeup"),
    path("haircare/",views.haircare, name="haircare"),
    path("skincare/",views.skincare, name="skincare"),
    path("appliances/",views.appliances, name="appliances"),
    path("searchcosmetic/",views.searchcosmetic, name="searchcosmetic"),
    path("register/",views.register, name="register"),
    path("signin/",views.signin, name="signin"),
    path("signout/",views.signout, name="signout"),
    path("wishlist/",views.wishlist, name="wishlist"),
    path("addtowishlist/<int:product_id>",views.addtowishlist, name="addtowishlist"),
    path("removefromwishlist/<int:product_id>",views.removefromwishlist, name="removefromwishlist"),
    path("blog/",views.blog, name="blog"),
    path("registerblog/",views.registerblog,name="registerblog"),
    path("delete/<id>",views.deleteblogs,name="deleteblogs"),
    path('myorder/',views.myorder,name='myorder'),
    path("removefromorder/<int:product_id>",views.removefromorder,name="removefromorder"),
    path('payment/',views.payment,name='payment'),
    path('userorders/',views.userorders,name='userorders'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
