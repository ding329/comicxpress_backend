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
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from comicxpress_backend.rest_framework_config import * 

class Registration(APIView):
    permission_classes = (AllowAny,)
    def form_response(self, username, password, storename, email, error=""):
	data= {
	    'username': username,
	    'password': password,
	    'storename': storename,
	    'email': email,
	}
	if error:
	    data['message'] = error
	
	return Response(data)

    def post(self, request, *args, **kwargs):
	username = request.POST.get('username')
	password = request.POST.get('password')
	storename = request.POST.get('storename')
	email = request.POST.get('email')

class Session(APIView):
    permission_classes = (AllowAny,)
    def form_response(self, isauthenticated, userid, username, error=""):
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return self.form_response(True, request.user.id, request.user.username)
        return self.form_response(False, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.form_response(True, user.id, user.username)
            return self.form_response(False, None, None, "Account is suspended")
        return self.form_response(False, None, None, "Invalid username or password")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


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

	def delete(self, request, pk, format=None):
                item= get_object_or_404(monthlyorder, pk=pk)
                item.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)


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
#	authenication_classes = (CsrfExemptSessionAuthentication,) 
#	permission_classes = (AllowAny,)
	def put(self, request, pk, format=None):
		item= get_object_or_404(monthlyorder, pk=pk)
		serializer = monthlyorderSerializer(item, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		item= get_object_or_404(monthlyorder, pk=pk)
		item.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class userViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
    	serializer_class = UserSerializer
