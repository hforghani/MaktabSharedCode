from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    task_id = models.CharField(max_length=100)
    sent = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
