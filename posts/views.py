
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
    post = Post.objects.all()
    print(post)
    postSerialized = PostSerializer(post, many=True)
    return Response(postSerialized.data)

  def post(self, request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print(User.objects.get(email=request.user))
    serializer.save(
      author = request.user,
      author_username = User.objects.get(email=request.user).username
    )
    return Response(
      serializer.validated_data,
      status=status.HTTP_201_CREATED
    )

class PostDetail(APIView):
  def get(self, pk):
    post = Post.objects.filter(pk=pk).first()
    if post:
      postSerialized = PostSerializer(post)
      return Response(postSerialized.data)
    else:
      return Response({"details": "Not found"}, status=status.HTTP_404_NOT_FOUND)
  
