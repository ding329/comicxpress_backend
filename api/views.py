from django.shortcuts import render

# Create your views here
	
# Import models
from django.db import models
from django.contrib.auth.models import *
from myapp.api.models import *

#REST API
from rest_framework import viewsets
from myapp.api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class catalogList(APIView):
"""
hopefully this will list an entire catalog and not all the catalogs
'"""
	def get(self, request, format=None):
		entries= catalog.objects.all()
		serializer=catalogSerializer(entries, many=True, context={'request':request})
		return Response(serializer.data)
"""
add an item to the catalog  I dont know if this is required because a user should never updated the catalog, but we have to load new ones somehow
"""
	def post(self, request, format=None):
		serializer= catalogSerializer(data=request.data, context={'request':request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

class monthlyorderList(APIView):
"""
get the list of monthlyorders
"""
	def get(self, request, format=None):
		items= monthlyorder.objects.all()
		serializer=monthlyorderSerializer(items, many=True, context={'request': request})
		return Response(serializer.data)
"""
add an item to monthlyorder
"""
	def post(self, request, format=None):
		serializer = monthlyorderSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED) 
	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class previewselectionsList(APIView):
	def get(self, request, format=None):
		catalogId= previewselections.objects.all()
		serializer = previewselectionsSerializer(catalogId, many=True, context={'request': request})
		return Response(serializer.data)

class monthlyorderDetail(APIView):
"""
Update or delete a single 
"""
	def put(self, request, pk, format=None):
		item = self.get_object(pk)
		serializer = monthlyorderSerializer(item, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		item= self.get_object(pk)
		item.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class userViewSet(viewsets.ModelViewSet):
	queryset = user.objects.all()
    	serializer_class = UserSerializer
