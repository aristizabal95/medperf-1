from django.contrib import admin
from rest_framework import serializers

from .models import MlCube

class MlCubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlCube
        fields = '__all__'
        read_only_fields = ['owner']
        #fields = ['id', 'name', 'git_url', 'tarball_url', 'tarball_hash', 'owner', 'metadata', 'status', 'created_at', 'modified_at']

