from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=1000,default='')

    

    video = models.FileField(upload_to='videos/')
    
    

    class Meta:
        ordering = ['title']

    def __str__(self):

        return self.title

    