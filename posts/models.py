from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  author = models.TextField()
  def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)
  class Meta:
    ordering = ['created_on']

    def __unicode__(self):
        return self.title