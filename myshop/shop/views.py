from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product


# Create your views here.
def product_list(request, category_slug=None):

    search_query = request.GET.get('se', '')#

    category = None
    categories = Category.objects.all()

    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    # Cart
    cart_product_form = CartAddProductForm()

    #  Recs ar not working
    # r = Recommender()
    # recommended_products = r.suggest_products_for([product], 4)
    #recommended_products = []

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form})
                  #'recommended_products': recommended_products})
