from django.db import models

# Create your models here.


class Posts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    read_counter = models.IntegerField(default=0)
