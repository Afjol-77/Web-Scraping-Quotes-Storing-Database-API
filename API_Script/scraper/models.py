from django.db import models

# Create your models here.
class Scrap(models.Model):
    searchKeyword = models.CharField(max_length=50)
    scrapDetail = models.JSONField()
