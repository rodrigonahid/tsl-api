from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.models import User

class PostSerializer(serializers.Serializer): 
  id = serializers.IntegerField()
  title = serializers.CharField(max_length=255)
  content = serializers.CharField()
  created_at = serializers.DateTimeField()
  author = serializers.PrimaryKeyRelatedField(
    queryset = User.objects.all()
  )