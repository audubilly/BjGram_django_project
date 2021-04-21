from django.db import models


# Create your models here.
class Owner(models.Model):
    username = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='gallery/', default="")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
