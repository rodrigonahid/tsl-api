from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  author_username = models.CharField(max_length=255, null=True)

  def __str__(self):
      return self.content