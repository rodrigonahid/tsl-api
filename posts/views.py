
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.models import User
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
  permission_classes = [IsAuthenticatedOrReadOnly]
  def get(self, request):
    post = Post.objects.all().order_by('-created_at')
    postSerialized = PostSerializer(post, many=True)
    return Response(postSerialized.data)

  def post(self, request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    serializer.save(
      author = request.user,
      author_username = User.objects.get(email=request.user).username
    )
    
    return Response(
      serializer.data,
      status=status.HTTP_201_CREATED
    )
