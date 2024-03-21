from django.db import models

# Create your models here.

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()


class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(auto_now_add=True)


class Purchase(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')

