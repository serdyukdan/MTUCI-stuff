from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            # TODO: Coupon
            # if cart.coupon:
            #     order.coupon = cart.coupon
            #     order.discount = cart.coupon.discount
            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()

            # launch asynchronous task
            # TODO: Also not now
            # order_created.delay(order.id)

            # set the order in the session
            # request.session['order_id'] = order.id

            # TODO: redirect for payment
            # return redirect(reverse('payment:process'))
            return render(request, 'orders/order/created.html', {'order': order})

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
