from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.response import Response

from .serializers import StocksSerializer
from .models import Stocks
# from rest_framework import

class StocksView(viewsets.ViewSet):
	
	def list(self, request):
		queryset = Stocks.objects.all()
		serializer = StocksSerializer(queryset, many=True)
		return Response(serializer.data)
	def create(self, request):
		serializer = StocksSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status= status.HTTP_201_CREATED)