from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"
