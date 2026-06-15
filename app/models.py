from django.db import models


class AccountUser(models.Model):
    user_id = models.CharField(max_length=128, primary_key=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    class Meta:
        db_table = "account_user"


class ShoppingCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = "shopping_category"


class ShoppingItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    manufacturer = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    price = models.IntegerField()
    stock = models.IntegerField()
    recommended = models.BooleanField(default=False)

    category = models.ForeignKey(
        ShoppingCategory,
        on_delete=models.CASCADE,
        db_column="category_id",
    )

    class Meta:
        db_table = "shopping_item"


class ShoppingItemsincart(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    booked_date = models.DateField(auto_now_add=True)

    item = models.ForeignKey(
        ShoppingItem,
        on_delete=models.CASCADE,
        db_column="item_id",
    )

    user = models.ForeignKey(
        AccountUser,
        on_delete=models.CASCADE,
        db_column="user_id",
    )

    class Meta:
        db_table = "shopping_itemsincart"


class ShoppingPurchase(models.Model):
    purchase_id = models.IntegerField(primary_key=True)
    destination = models.CharField(max_length=256)
    booked_date = models.DateField(auto_now_add=True)
    cancel = models.BooleanField(default=False)

    user = models.ForeignKey(
        AccountUser,
        on_delete=models.CASCADE,
        db_column="user_id",
    )

    class Meta:
        db_table = "shopping_purchase"


class ShoppingPurchasedetail(models.Model):
    purchase_detail_id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()

    item = models.ForeignKey(
        ShoppingItem,
        on_delete=models.CASCADE,
        db_column="item_id",
    )

    purchase = models.ForeignKey(
        ShoppingPurchase,
        on_delete=models.CASCADE,
        db_column="purchase_id",
    )

    class Meta:
        db_table = "shopping_purchasedetail"


class AdministratorAdmin(models.Model):
    admin_id = models.CharField(max_length=128, primary_key=True)
    password = models.CharField(max_length=256)

    class Meta:
        db_table = "administrator_admin"