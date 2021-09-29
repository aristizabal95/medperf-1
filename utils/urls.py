from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.User.as_view()),
    path('benchmarks/', views.BenchmarkList.as_view()),
    path('datasets/', views.DatasetList.as_view()),
    path('mlcubes/', views.MlCubeList.as_view()),
    path('results/', views.ModelResultList.as_view()),
]
