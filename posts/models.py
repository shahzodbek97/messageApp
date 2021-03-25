from django.db import models
class Post(models.Model):
    text = models.TextField(default='post kiriting:')

    def __str__(self):
        return self.text[:50]

