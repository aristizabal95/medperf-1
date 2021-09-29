from django.contrib import admin
from rest_framework import serializers
from django.utils import timezone
from .models import BenchmarkDataset

class BenchmarkDatasetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkDataset
        read_only_fields = ['approved_at', 'approval_status']
        fields = ['dataset', 'benchmark', 'approval_status', 'approved_at', 'created_at', 'modified_at']

class BenchmarkDatasetApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkDataset
        read_only_fields = ['approved_at', 'approval_status']
        fields = ['benchmark', 'approval_status', 'approved_at', 'created_at', 'modified_at']

class DatasetApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenchmarkDataset
        read_only_fields = ['approved_at']
        fields = ['approval_status', 'approved_at', 'created_at', 'modified_at']

    def update(self, instance, validated_data):
        instance.approval_status = validated_data['approval_status']
        if instance.approval_status == "APPROVED":
            instance.approved_at = timezone.now()
        return instance
