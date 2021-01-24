from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('news-list/', views.newsList, name="news-list"),
    path('news-detail/<str:pk>/', views.newsDetail, name="news-detail"),
    path('news-create/', views.newsCreate, name="news-create"),
    path('news-update/<str:pk>/', views.newsUpdate, name="news-update"),
    path('news-delete/<str:pk>/', views.newsDelete, name="news-delete"),
]
