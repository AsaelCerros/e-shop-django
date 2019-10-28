from django.shortcuts import render
# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
 
# Create your views here.
from shop.models import Product
 
# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'product_list'
    template_name = 'shop/index.html'
 
    def get_queryset(self):
        return Product.objects.all()
 
# view for the product entry page
class ProductEntry(CreateView):
    model = Product
    # the fields mentioned below become the entry rows in the generated form
    fields = ['product_title', 'product_price', 'product_desc', 'product_image']
 
# view for the product update page
class ProductUpdate(UpdateView):
    model = Product
    # the fields mentioned below become the entyr rows in the update form
    fields = ['product_title', 'product_price', 'product_desc', 'product_image']
 
# view for deleting a product entry
class ProductDelete(DeleteView):
    model = Product
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('shop:index')