from django.shortcuts import render

from .models import BenchmarkModel
from .serializers import BenchmarkModelSerializer, BenchmarkModelApprovalSerializer, ModelApprovalSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class BenchmarkModel(GenericAPIView):
    serializer_class = BenchmarkModelSerializer
    queryset = ''
    
    #def get(self, request, format=None):
    #    """
    #    List all models associated across benchmarks
    #    """
    #    benchmarkmodels = BenchmarkModel.objects.all()
    #    serializer = BenchmarkModelSerializer(benchmarkmodels, many=True)
    #    return Response(serializer.data)

    def post(self, request, format=None):
        """
        Associate a model to a benchmark
        """
        serializer = BenchmarkModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BenchmarkModelApproval(GenericAPIView):
    serializer_class = BenchmarkModelApprovalSerializer
    queryset = ''
    
    def get_object(self, pk):
        try:
            return BenchmarkModel.objects.filter(mlcube__id=pk)
        except BenchmarkModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve all benchmarks associated with a model
        """
        benchmarkmodel = self.get_object(pk)
        serializer = BenchmarkModelApprovalSerializer(benchmarkmodel, many=True)
        return Response(serializer.data)

    #def put(self, request, pk, format=None):
    #    """
    #    Update the benchmark association with a model
    #    """
    #    benchmarkmodel = self.get_object(pk)
    #    serializer = BenchmarkModelApprovalSerializer(benchmarkmodel, data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request, pk, format=None):
    #    """
    #    Delete a benchmark association with a model
    #    """
    #    benchmarkmodel = self.get_object(pk)
    #    benchmarkmodel.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)

class ModelApproval(GenericAPIView):
    serializer_class = ModelApprovalSerializer
    queryset = ''
    
    def get_object(self, model_id, benchmark_id):
        try:
            return BenchmarkModel.objects.get(mlcube__id=model_id, benchmark__id=benchmark_id)
        except BenchmarkModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, bid, format=None):
        """
        Retrieve approval status of benchmark model association
        """
        benchmarkmodel = self.get_object(pk, bid)
        serializer = ModelApprovalSerializer(benchmarkmodel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update approval status of benchmark model association
        """
        benchmarkmodel = self.get_object(pk, bid)
        serializer = ModelApprovalSerializer(benchmarkmodel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, bid, format=None):
        """
        Delete a benchmark model association
        """
        benchmarkmodel = self.get_object(pk, bid)
        benchmarkmodel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
