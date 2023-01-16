from django.db import models
import uuid
from django.contrib.auth.models import User
# from django.dispatch import reciever
from django.db.models.signals import post_save


class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length= 200,null=True,blank=True)
    email=models.CharField(max_length= 200,null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,default="user-default.png")
    Id = models.UUIDField(default = uuid.uuid4,unique = True,primary_key=True,editable=False)

    def __str__(self):
        return self.username
    # @reciever(post_save,sender=User)
    def createprofile(sender,instance,created,**kwargs):
        if created:
            user = instance
            profile =Profile.objects.create(
                user= user, 
                username = user.username
            )
    post_save.connect(createprofile,sender=User)

class Uploads(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    featured_image = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
  

    def __str__(self):
        return str(self.owner)

    


