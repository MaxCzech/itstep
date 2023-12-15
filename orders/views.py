from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            email_order = order.email
            total = 0
            message = 'Hello.\nThank you for your order.\nYour order number' + str(
                order) + ' \nContents of the order: \n'

            for item in cart:
                message = message + '\n' + 'Product:' + str(item['product']) + ' X ' + str(
                    item['price']) + 'USD' + ' Qty:' + str(item['quantity'])
                total = total + item['price'] * item['quantity']
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            subject_email = 'Subscription shop. Order number-' + str(order)
            message_email = message + '\n\n' + 'TOTAL :' + str(
                total) + ' USD \n\nPlease pay for your order to account 123456.\nAfter receiving payment, data for accessing the service will be sent immediately.'
            send_mail(
                subject_email,
                message_email,
                "postmaster@chitramtv.cz",
                # email,
                [email_order],
                fail_silently=False, )
            # очистка корзины
            cart.clear()

            return render(request, 'orders/order/created.html',
                          {'order': order})

    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
