from django.contrib import admin
from rest_framework import serializers

from .models import ModelResult

class ModelResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelResult
        fields = '__all__'
        read_only_fields = ['owner', 'approved_at']
        #fields = ['id', 'name', 'owner', 'benchmark', 'model', 'dataset', 'results', 'metadata', 'approval_status', 'approved_at', 'created_at', 'modified_at']
