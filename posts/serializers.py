
from rest_framework import serializers

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):   
  class Meta:
    model = Post
    fields = ['content', 'created_at', 'author', 'author_username' ]

  def create(self, validated_data):
    return Post.objects.create(**validated_data)

  def validate(self, attrs):
    return super().validate(attrs)

  def save(self, **kwargs):
    return super().save(**kwargs)