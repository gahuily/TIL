# from rest_framework.decorators import api_view
# from .models import Post
# from .serializers import PostSerializer
# from rest_framework.response import Response

# # Create your views here.
# @api_view(['GET'])
# def post_list(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post
from .serializers import PostListSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def article_get_or_create(request):
    if request.method == 'GET':
        articles = Post.objects.all()
        serializer = PostListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def article_detail(request, article_pk):
    article = Post.objects.get(pk=article_pk)
    if request.method == 'GET': # article 객체를 직렬화하여 반환
        serializer = PostListSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = PostListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):  # serializer를 통해 입력 데이터의 유효성 검사
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PostListSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):  # serializer를 통해 입력 데이터의 유효성 검사
            serializer.save(raise_exception=True)
            return Response(serializer.data)