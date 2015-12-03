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

		#(lxml.html.document_fromstring(cleaner.clean_html(self.name))).text_content()
		data['name']= (lxml.html.document_fromstring(cleaner.clean_html(data['name']))).text_content()
		data['price']= (lxml.html.document_fromstring(cleaner.clean_html(data['price']))).text_content()
		data['itemid']= (lxml.html.document_fromstring(cleaner.clean_html(data['itemid']))).text_content()
		data['discountcode']= (lxml.html.document_fromstring(cleaner.clean_html(data['discountcode']))).text_content()
		data['orderdate']= (lxml.html.document_fromstring(cleaner.clean_html(data['orderdate']))).text_content()
		data['selldate']= (lxml.html.document_fromstring(cleaner.clean_html(data['selldate']))).text_content()
		data['page']= (lxml.html.document_fromstring(cleaner.clean_html(data['page']))).text_content()

		if data[qty] < 0:
                        data[qty]=0

     #           self.name= cleaner.clean_html(self.name)		
		return data

class monthlyorderSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

	print author

	class Meta:
		model = monthlyorder
		fields=('id', 'name', 'qty', 'author',)

	def validate(self, data):
                cleaner= Cleaner()
                cleaner.javascript = True
                cleaner.scripts = True
                cleaner.frames = True
		cleaner.remove_tags = ['p', 'div', 'a']
		data['name']= (lxml.html.document_fromstring(cleaner.clean_html(data['name']))).text_content()

		if data['qty'] < 0:
			data['qty']=0
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
		data['username']= (lxml.html.document_fromstring(cleaner.clean_html(data['username']))).text_content()
		data['storename']= (lxml.html.document_fromstring(cleaner.clean_html(data['storename']))).text_content()
		data['email']= (lxml.html.document_fromstring(cleaner.clean_html(data['email']))).text_content()

#		data['username']=  cleaner.clean_html(data['username'])
 #               data['storename']= cleaner.clean_html(data['storename'])
  #              data['email']= cleaner.clean_html(data['email'])

		
		return data
