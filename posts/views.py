from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND

from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view()
def post_list(request):
  post = Post.objects.all()
  postSerialized = PostSerializer(post, many=True)
  return Response(postSerialized.data)

@api_view()
def post_detail(request, pk):
  post = Post.objects.filter(pk=pk).first()
  if post:
    postSerialized = PostSerializer(post)
    return Response(postSerialized.data)
  else:
    return Response({"details": "Not found"}, status=HTTP_404_NOT_FOUND)