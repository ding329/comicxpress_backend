from django.shortcuts import *

# Create your views here
	
# Import models
from django.db import models
from django.contrib.auth.models import *
from comicxpress_backend.api.models import *

#REST API
from rest_framework import viewsets
from comicxpress_backend.api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def home(request):
  	"""
  	Send requests to / to the ember.js clientside app  """
  
  	return render_to_response('index.html',
                {}, RequestContext(request))

class catalogList(APIView):
	def get(self, request, format=None):
		entries= catalog.objects.all()
		serializer=catalogSerializer(entries, many=True, context={'request':request})
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer= catalogSerializer(data=request.data, context={'request':request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class monthlyorderList(APIView):
	def get(self, request, format=None):
		items= monthlyorder.objects.all()
		serializer=monthlyorderSerializer(items, many=True, context={'request': request})
		return Response(serializer.data)
	
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
	queryset = User.objects.all()
    	serializer_class = UserSerializer
