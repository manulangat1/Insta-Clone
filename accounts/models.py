from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField()
    friends = models.ManyToManyField("Profile",blank=True)

    def __str__(self):
        return self.user.username
def post_save_user_model_receiver(sender,instance,created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_receiver,sender=User)

class FriendRequest(models.Model):
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} to {}".format(self.from_user.username,self.to_user.username)