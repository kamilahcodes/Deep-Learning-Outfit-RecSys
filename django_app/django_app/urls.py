"""django_app URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from fyp.views import queryimage
# from store.import views


from store.views import product_list_view, product_detail_view, product_cat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', queryimage, name='outrecsys'),
    re_path(r'^products/$', product_list_view, name='products'),
    re_path(r'^products/(?P<pk>\d+)/$', product_detail_view, name='product_detail'),
    re_path(r'^products/(?P<category>[\w\-]+)/$', product_cat_view, name='product_cat'),

 


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)




'''from fyp.views import EndpointViewSet
from fyp.views import OutfitRecViewSet
from fyp.views import RequestViewSet
router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"outfitrec", OutfitRecViewSet, basename="outfitrec")
router.register(r"requests", RequestViewSet, basename="request")'''