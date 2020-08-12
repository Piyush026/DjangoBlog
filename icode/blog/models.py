from django.db import models

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
    