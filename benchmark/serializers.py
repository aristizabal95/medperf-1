from django.contrib import admin
from rest_framework import serializers
from .models import Benchmark

class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        fields = '__all__'
        read_only_fields = ['owner']
        #fields = ['id', 'name', 'description', 'docs_url', 'owner', 'data_preparation_mlcube', 'reference_model_mlcube','data_evaluator_mlcube', 'created_at', 'modified_at']

