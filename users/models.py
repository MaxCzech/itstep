from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER = (
        ('m','Man'),
        ('f','woman'),
    )

    fio = models.CharField('FIO', max_length = 255, default = '')

    # def __str__(self):
    #     return self.username


# class Profile(models.Model):
#     user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio=models.TextField(null=True, blank=True)
#     profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
#     facebook = models.CharField(max_length=50, null=True, blank=True)
#     twitter = models.CharField(max_length=50, null=True, blank=True)
#     instagram = models.CharField(max_length=50, null=True, blank=True)
# def __str__(self):
#     return str(self.user)