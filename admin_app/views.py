from django.shortcuts import render
from .models import product_model

# Create your views here.
def product(request):
    item=product_model.objects.all()
    obj={
        'item':item
    }
    return render(request,'product.html',obj)

