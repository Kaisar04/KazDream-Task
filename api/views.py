from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NewsSerializer
from .models import News


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/news-list/',
        'Detail View':'/news-detail/<str:pk>/',
        'Create':'/news-create/',
        'Update':'/news-update/<str:pk>/',
        'Delete':'/news-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def newsList(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def newsDetail(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializer(news, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def newsCreate(request):
    serializer = NewsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def newsUpdate(request, pk):
    new = News.objects.get(id=pk)
    serializer = NewsSerializer(instance=new, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def newsDelete(request, pk):
    news = News.objects.get(id=pk)
    news.delete()

    return Response("Item was successfully deleted")
