from django.db import models

# Create your models here.

class Update(models.Model):
    name = models.CharField(max_length = 100)
    Content = models.TextField()
    Phone = models.IntegerField()

    def __str__(self):
        return self.name
