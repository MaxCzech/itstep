# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Codes_load
from codes.models import Codes


@receiver(post_save, sender=Codes_load)
def your_model_post_save(sender, instance, **kwargs):
    textcode = str(instance).split('\r\n')
    list = []
    for i in textcode:
        i = i.split(' ', 1)
        print(i)
        fa = Codes
        fa.objects.create(prod=instance.prod, serialNum=i[0], code=i[1])
        list.append(i)

    # Выполните здесь свои действия после сохранения объекта
    print(f'Объект {instance} был сохранен!')
