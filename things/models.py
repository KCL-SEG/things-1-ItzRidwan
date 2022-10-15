from django.db import models

class Things(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    quantity = models.IntegerField()
