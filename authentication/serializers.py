from rest_framework import serializers
from authentication.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']