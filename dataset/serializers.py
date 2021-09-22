from django.contrib import admin
from rest_framework import serializers

from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'
        read_only_fields = ['owner']
        #fields = ['id', 'name', 'description', 'location', 'generated_uid', 'split_seed', 'data_preparation_mlcube', 'owner', 'metadata', 'status', 'created_at', 'modified_at']
