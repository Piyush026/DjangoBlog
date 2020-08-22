from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    timstamp  = models.DateTimeField(blank=True)

    def __str__(self):
        return self.tittle + " by " + self.author 

class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

