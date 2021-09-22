from django.contrib import admin
from .models import MlCube

class MlCubeAdmin(admin.ModelAdmin):
    list_display = ('name', 'git_url', 'tarball_url', 'tarball_hash', 'owner', 'metadata', 'status', 'created_at', 'modified_at')

admin.site.register(MlCube, MlCubeAdmin)