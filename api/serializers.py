from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from comicxpress_backend.api.models import *

import lxml
from lxml.html.clean import Cleaner

class catalogSerializer(serializers.ModelSerializer):
	class Meta:
		model= catalog
		fields=('id', 'name', 'price','catalogid', 'itemid', 'discountcode', 'categorycode', 'orderdate', 'selldate', 'qty', 'page', 'reoccuring')

	def validate(self, data):	
		cleaner= Cleaner()
                cleaner.javascript = True
                cleaner.scripts = True
                cleaner.frames = True
		cleaner.remove_tags = ['p', 'div', 'a']
		data['name']= cleaner.clean_html(data['name'])
		data['price']= cleaner.clean_html(data['price'])
		data['itemid']= cleaner.clean_html(data['itemid'])
		data['discountcode']= cleaner.clean_html(data['discountcode'])
		data['orderdate']= cleaner.clean_html(data['orderdate'])
		data['selldate']= cleaner.clean_html(data['selldate'])
		data['page']= cleaner.clean_html(data['page'])

		if data[qty] < 0:
                        data[qty]=0

     #           self.name= cleaner.clean_html(self.name)		
		return data

class monthlyorderSerializer(serializers.ModelSerializer):
	class Meta:
		model = monthlyorder
		fields=('id', 'name', 'qty',)

	def validate(self, data):
                cleaner= Cleaner()
                cleaner.javascript = True
                cleaner.scripts = True
                cleaner.frames = True
		cleaner.remove_tags = ['p', 'div', 'a']
		data['name']= cleaner.clean_html(data['name'])

		if data[qty] < 0:
			data[qty]=0
		return data


class previewselectionsSerializer(serializers.ModelSerializer):
	class Meta:
		model=previewselections
		fields=('id', 'name')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields = ('id', 'username', 'storename', 'email')

	def validate(self, value):
                cleaner= Cleaner()
                cleaner.javascript = True
                cleaner.scripts = True
                cleaner.frames = True
		cleaner.remove_tags = ['p', 'div', 'a']
		data['username']= cleaner.clean_html(data['username'])
		data['storename']= cleaner.clean_html(data['storename'])
		data['email']= cleaner.clean_html(data['email'])
		
		return data
