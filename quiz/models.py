from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    value_in_text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='frontend/static/img/')

    def __str__(self):
        return self.name