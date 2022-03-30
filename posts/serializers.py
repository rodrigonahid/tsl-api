
from rest_framework import serializers
from django.contrib.auth.models import User

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):   
  class Meta:
    model = Post
    fields = ['title', 'content', 'created_at', 'author' ]

  def create(self, validated_data):
    return Post.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.content = validated_data.get('content', instance.content)
    return instance

  def validate(self, attrs):
    return super().validate(attrs)

  def save(self, **kwargs):
    return super().save(**kwargs)