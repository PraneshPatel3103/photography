from django.db import models

class DateLink(models.Model):
    date = models.DateField(unique=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.date}: {self.url}"
