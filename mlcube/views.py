from django.shortcuts import render

from .models import MlCube
from .serializers import MlCubeSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class MlCubeList(GenericAPIView):
    serializer_class = MlCubeSerializer
    queryset = ''
    
    def get(self, request, format=None):
        """
        List all mlcubes
        """
        mlcubes = MlCube.objects.all()
        serializer = MlCubeSerializer(mlcubes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Creates a new mlcube
        """
        serializer = MlCubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MlCubeDetail(GenericAPIView):
    serializer_class = MlCubeSerializer
    queryset = ''
    
    def get_object(self, pk):
        try:
            return MlCube.objects.get(pk=pk)
        except MlCube.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a mlcube instance.
        """
        mlcube = self.get_object(pk)
        serializer = MlCubeSerializer(mlcube)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update a mlcube instance.
        """
        mlcube = self.get_object(pk)
        serializer = MlCubeSerializer(mlcube, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a mlcube instance.
        """
        mlcube = self.get_object(pk)
        mlcube.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
