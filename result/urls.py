from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.ModelResultList.as_view()),
   path('<int:pk>/', views.ModelResultDetail.as_view()),
]
