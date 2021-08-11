from django.db import models

class By_date(models.Model):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
