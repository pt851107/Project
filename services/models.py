from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    fun_activities= models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.title