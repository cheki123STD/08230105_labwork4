from django.db import models

# Create your models here.
from django.db import models

class Milestone(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
