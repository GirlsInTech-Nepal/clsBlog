from django.db import models
#inheritted from django.db.models.Model
class Blog(models.Model):
    content = models.TextField()
