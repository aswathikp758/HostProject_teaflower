from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    Offer = models.BooleanField(default=False)
    # img=models.ImageField(upload_to='pics')
