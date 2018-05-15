from django.db import models

# Create your models here.


class WorkOrder(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100)
    description = models.TextField()
    creation_dt = models.DateTimeField()

    def __str__(self):
        return self.number
