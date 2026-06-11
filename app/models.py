from django.db import models

class AccountUser(models.Model):
    user_id = models.CharField(max_length=128, primary_key=True, null=False)
    password = models.CharField(max_length=256, null=False)
    name = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=256, null=False)
