from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PostSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=255)
  content = serializers.CharField()
  created_at = serializers.DateTimeField()
  author = serializers.CharField()