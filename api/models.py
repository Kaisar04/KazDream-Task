from django.db import models
from django.utils import timezone
from django.conf import settings


class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.text
