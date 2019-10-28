from django.conf.urls import url
 
from shop import views
 
app_name = 'shop'
 
urlpatterns = [
 
    # /shop/
    url(r'^$', views.IndexView.as_view(), name='index'),
 
    # shop/product/entry
    url(r'^product/entry/$',views.ProductEntry.as_view(),name='product-entry'),
 
    # shop/product/2
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product-update'),
 
    # shop/product/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.ProductDelete.as_view(), name='product-delete'),
 
]