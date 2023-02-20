from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='media/Blog_pic', blank=True, null=True)
    dsc = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    