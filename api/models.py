from django.db import models
""" do I need these two below """
from django.contrib.auth.models import User
from django.contrib import admin
from comicxpress_backend.api.validators import *

import lxml
from lxml.html.clean import Cleaner

# Create your models here.

"""
class cart (models.Model):
	name = models.CharField(max_length=50, blank=False)
	price = models.CharField(max_length=10, blank=False)
	catalogID = models.CharField(max_length=7, blank=False)
	itemId = models.CharField(max_length=11, blank=False, unique=True)
	discountCode = models.CharField(max_length=3, blank=False)
	qty = models.IntegerField(default=0)

	def total(self)
		return self.qty * self.price
"""
class catalog(models.Model):
	"""
this is the model for the catalog, holds most of the information for the application
	""" 
	name = models.CharField(max_length=75, blank=False)
	price = models.CharField(max_length=10, blank=False)
#	catalogid = models.CharField(max_length=7, blank=False)
	catalogid = models.IntegerField(blank=False, validators=[validateInterger])
        itemid = models.CharField(max_length=11, blank=False, unique=True)
        discountcode = models.CharField(max_length=3, blank=False)
	categorycode = models.CharField(max_length=3, blank=False)
	orderdate = models.CharField(max_length=11)
	selldate = models.CharField(max_length=11)
	qty = models.IntegerField(default=0, validators=[validateInterger])
	page = models.CharField(max_length=5)
	reoccuring = models.BooleanField(default=False)

	def clean(self):
		cleaner= Cleaner(page_structure=False)
		cleaner.javascript = True
		cleaner.scripts = True
		cleaner.frames = True
		cleaner.allow_tags = []
		cleaner.remove_tags = ['p', 'div', 'a']
		self.name= cleaner.clean_html(self.name)
		self.price = cleaner.clean_html(self.price)
		self.discountcode = cleaner.clean_html(self.discountcode)
		self.categorycode= cleaner.clean_html(self.categorycode)
		self.orderdate= cleaner.clean_html(self.orderdate)
		self.selldate= cleaner.clean_html(self.selldate)
		self.page= cleaner.clean_html(self.page)		


class catalogAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'itemid', 'qty', 'reoccuring')

class monthlyorder(models.Model):
	name = models.CharField(max_length=75, blank=False,) #validators=[removeJavascriptKeyword])
	qty = models.IntegerField(default=0, validators=[validateInterger])

	def clean(self):
                cleaner= Cleaner()
                cleaner.javascript = True
                cleaner.scripts = True
                cleaner.frames = True
		cleaner.remove_tags = ['p', 'div', 'a']
		self.name= cleaner.clean_html(self.name)  #lxml.html.fromstring(self.name) ) 
		

class monthlyorderAdmin(admin.ModelAdmin):
	list_display = ('name', 'qty')

class previewselections(models.Model):
	name = models.CharField(max_length=7, blank=False)

class previewselectionsAdmin(admin.ModelAdmin):
	list_display = ('name',)
