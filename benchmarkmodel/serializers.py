from django.contrib import admin
from rest_framework import serializers

from .models import BenchmarkModel

class BenchmarkModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkModel
        read_only_fields = ['approved_at']
        fields = ['model_mlcube', 'benchmark', 'approval_status', 'approved_at', 'created_at', 'modified_at']

class BenchmarkModelApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkModel
        read_only_fields = ['approved_at']
        fields = ['benchmark', 'approval_status', 'approved_at', 'created_at', 'modified_at']
 
class ModelApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkModel
        read_only_fields = ['approved_at']
        fields = ['approval_status', 'approved_at', 'created_at', 'modified_at']
 
