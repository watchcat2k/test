from django.db import models

# Create your models here.

#用户
class User(models.Model):    
    user_id = models.AutoField(primary_key=True)    
    user_username = models.CharField(max_length=30, default='None', null=True)
    user_password = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30, default='None', null=True)
    user_avatar = models.CharField(max_length=200, default='https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png')