from django.db import models

class Media(models.Model):    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    photo = models.FileField(upload_to='media/')
    video = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title
