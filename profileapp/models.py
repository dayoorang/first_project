from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,
                                related_name='profile') # user 객체에서 profile에 접근하기 위해서 user.profile 이런식으로 접근할수있음.

    image = models.ImageField(upload_to='profile/', null=True) # null = True , 해당 form 에 있어도되고 없어도 됨.
    nickname = models.CharField(max_length=30, unique=True, null = True) # 닉네임이 유일해야한다.
    message = models.CharField(max_length=200, null = True)