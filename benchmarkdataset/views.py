from django.shortcuts import render

from .models import BenchmarkDataset
from .serializers import BenchmarkDatasetSerializer, BenchmarkDatasetApprovalSerializer, DatasetApprovalSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class BenchmarkDataset(GenericAPIView):
    serializer_class = BenchmarkDatasetSerializer
    queryset = ''

    def get(self, request, format=None):
        """
        List all datasets associated across benchmarks
        """
        benchmarkdatasets = BenchmarkDataset.objects.all()
        serializer = BenchmarkDatasetSerializer(benchmarkdatasets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Associate a dataset to a benchmark
        """
        serializer = BenchmarkDatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BenchmarkDatasetApproval(GenericAPIView):
    serializer_class = BenchmarkDatasetApprovalSerializer
    queryset = ''
    
    def get_object(self, pk):
        try:
            return BenchmarkDataset.objects.filter(dataset__id=pk)
        except BenchmarkDataset.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve all benchmarks associated with a dataset
        """
        benchmarkdataset = self.get_object(pk)
        serializer = BenchmarkDatasetApprovalSerializer(benchmarkdataset, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update the benchmark association with a dataset
        """
        benchmarkdataset = self.get_object(pk)
        serializer = BenchmarkDatasetApprovalSerializer(benchmarkdataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete a benchmark association with a dataset
        """
        benchmarkdataset = self.get_object(pk)
        benchmarkdataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DatasetApproval(GenericAPIView):
    serializer_class = DatasetApprovalSerializer
    queryset = ''
    
    def get_object(self, dataset_id, benchmark_id):
        try:
            return BenchmarkDataset.objects.get(dataset__id=dataset_id, benchmark__id=benchmark_id)
        except BenchmarkDataset.DoesNotExist:
            raise Http404

    def get(self, request, pk, bid, format=None):
        """
        Retrieve approval status of benchmark dataset association
        """
        benchmarkdataset = self.get_object(pk, bid)
        serializer = DatasetApprovalSerializer(benchmarkdataset)
        return Response(serializer.data)

    def put(self, request, pk, bid, format=None):
        """
        Update approval status of benchmark dataset association
        """
        benchmarkdataset = self.get_object(pk, bid)
        serializer = DatasetApprovalSerializer(benchmarkdataset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, bid, format=None):
        """
        Delete a benchmark dataset association
        """
        benchmarkdataset = self.get_object(pk, bid)
        benchmarkdataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)