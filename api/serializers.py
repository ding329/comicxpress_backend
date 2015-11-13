from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from comicxpress_backend.api.models import *

class catalogSerializer(serializers.ModelSerializer):
	class Meta:
		model= catalog
		fields=('id', 'name', 'price','catalogId', 'itemId', 'discountCode', 'categoryCode', 'orderDate', 'orderDate', 'qty', 'page', 'reoccuring')

class monthlyorderSerializer(serializers.ModelSerializer):
	class Meta:
		model = monthlyorder
		fields=('id', 'name', 'qty',)

class previewselectionsSerializer(serializers.ModelSerializer):
	class Meta:
		model=previewselections
		fields=('id', 'name')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields = ('id', 'username', 'storeName', 'email')
