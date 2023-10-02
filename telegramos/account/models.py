from django.db import models


class Profile(models.Model):
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=64, null=True, blank=True)
    user_name = models.CharField(max_length=32, null=True)
    registration_date = models.DateField(auto_now_add=True, null=True)
