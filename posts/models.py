from django.db import models


class Post(models.Model):
    text = models.TextField()


    def _str__(self):
        return self.text[:50]
