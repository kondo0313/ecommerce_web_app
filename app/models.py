from django.db import models

class AccountUser(models.Model):
    user_id = models.CharField(max_length=128, primary_key=True, null=False)
    password = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=256, null=False)

class ShoppingCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, null=False)

class ShoppingItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    manufacturer = models.CharField(max_length=32, null=False)
    color = models.CharField(max_length=16, null=False)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    recommended = models.BooleanField(default=False)
    category_id = models.ForeignKey(
        ShoppingCategory,
        on_delete=models.CASCADE,
    )


class ShoppingItemsincart(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(null=False)
    booked_date = models.DateField(auto_now_add=True, null=False)
    item_id = models.ForeignKey(
        ShoppingItem,
        on_delete=models.CASCADE,
    )
    user_id = models.ForeignKey(
        AccountUser,
        on_delete=models.CASCADE,
    )