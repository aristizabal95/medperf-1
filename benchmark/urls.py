from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BenchmarkList.as_view()),
    path('<int:pk>/', views.BenchmarkDetail.as_view()),
    path('<int:pk>/models/', views.BenchmarkModelList.as_view()),
    path('<int:pk>/datasets/', views.BenchmarkDatasetList.as_view()),
    path('<int:pk>/users/', views.BenchmarkUserList.as_view()),
    path('<int:pk>/results/', views.BenchmarkResultList.as_view()),
]
