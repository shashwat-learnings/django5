from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('product.add_product',raise_exception=True)
def product_add(request):
    print()
# Create your views here.
