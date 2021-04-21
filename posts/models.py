from django.db import models


# Create your models here.
from accounts.models import Owner


class Post(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery/", default="")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner
