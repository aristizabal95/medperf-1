"""medperf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#schema_view = get_swagger_view(title='MedPerf API')
schema_view = get_schema_view(
   openapi.Info(
      title="MedPerf API",
      default_version='v1',
      description="MedPerf API description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #url(r'^$', schema_view),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^apidoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    
    path('benchmarks/', include('benchmark.urls')),
    path('mlcubes/', include('mlcube.urls')),
    path('datasets/', include('dataset.urls')),
    path('benchmarkdatasets/', include('benchmarkdataset.urls')),
    path('benchmarkmodels/', include('benchmarkmodel.urls')),
    path('benchmarkusers/', include('benchmarkuser.urls')),
    path('results/', include('result.urls')),
    path('users/', include('user.urls')),
    path('auth-token/', obtain_auth_token, name='auth-token'),
]
