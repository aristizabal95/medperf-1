from django.contrib import admin
from rest_framework import serializers

from .models import BenchmarkDataset

class BenchmarkDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkDataset
        read_only_fields = ['approved_at']
        fields = ['dataset', 'benchmark', 'approval_status', 'approved_at', 'created_at', 'modified_at']

class BenchmarkDatasetApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkDataset
        read_only_fields = ['approved_at']
        fields = ['benchmark', 'approval_status', 'approved_at', 'created_at', 'modified_at']

class DatasetApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkDataset
        read_only_fields = ['approved_at']
        fields = ['approval_status', 'approved_at', 'created_at', 'modified_at']
