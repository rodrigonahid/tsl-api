
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
  def get(self, request):
    post = Post.objects.all()
    postSerialized = PostSerializer(post, many=True)
    return Response(postSerialized.data)

  def post(self, request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(
      author = request.user
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
  
