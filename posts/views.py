from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view()
def post_list(request):
  post = Post.objects.all()
  postSerialized = PostSerializer(post, many=True)
  return Response(postSerialized.data)

@api_view()
def post_detail(request, title):
  post = Post.objects.all().filter(title="teste")
  postSerialized = PostSerializer(post, many=False)
  return Response(postSerialized.data)