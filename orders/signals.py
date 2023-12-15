from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order, OrderItem
from shop.models import Product
from codes.models import Codes
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from pprint import pprint
from django.core.mail import send_mail


@receiver(post_save, sender=Order)
def send_message(sender, instance, **kwargs):
    #  orders payed but not sent
    unsend_orders = Order.objects.filter(paid=True, code_send=False).values('id')

    subject_email = 'Subscriptions shop. Order:'
    # email body message
    message_email = 'Hello.\n Your sudscription pass is:\n'

    # unsend orders iteration
    for unsend_order in unsend_orders:
        unsend_order_id = unsend_order['id']
        subject_email = subject_email + str(unsend_order_id)
        unsend_order_ob = get_object_or_404(Order, pk=unsend_order_id)
        unsend_order_email = unsend_order_ob.email
        # qty and product ID
        unsend_products_id_qty = OrderItem.objects.filter(order_id=unsend_order_id).values('product_id', 'quantity')
        # iteration by products in order
        for unsend_product in unsend_products_id_qty:
            unsend_product_id = unsend_product['product_id']
            unsend_product_qty = unsend_product['quantity']
            product_name = get_object_or_404(Product, pk=unsend_product_id).name

            # selecting passwords for product
            for step in range(unsend_product_qty):
                pass_to_send = Codes.objects.filter(prod_id=unsend_product_id, sold=False, ignor=False).order_by(
                    'id').first()
                message_email = message_email + ' ' + str(product_name) + '-password is-' + str(pass_to_send) + '\n'

                #  change  password as sold
                pass_to_send.sold = True
                pass_to_send.order_id = unsend_order_id
                pass_to_send.save()

                #  mark order as code_send True
                order_change = Order.objects.get(pk=unsend_order_id)
                order_change.code_send = True
                order_change.save()

        send_mail(
            subject_email,
            message_email,
            "postmaster@chitramtv.cz",
            [unsend_order_email],
            fail_silently=False, )
