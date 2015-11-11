from django.db import models
""" do I need these two below """
from django.contrib.auth.models import User
from django.contrib import admin


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
	name = models.CharField(max_length=50, blank=False)
	price = models.CharField(max_length=10, blank=False)
	catalogID = models.CharField(max_length=7, blank=False)
        itemId = models.CharField(max_length=11, blank=False, unique=True)
        discountCode = models.CharField(max_length=3, blank=False)
	categoryCode = models.CharField(max_length=3, blank=False)
	orderDate = models.CharField(max_length=11)
	sellDate = models.CharField(max_length=11)
	qty = models.IntegerField(default=0)
	page = models.CharField(max_length=5)
	reoccuring = models.BooleanField(default=False)

class catalogAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'itemId', 'qty', 'reoccuring')

class monthlyorder(models.Model):
	name = models.CharField(max_length=50, blank=False)
	qty = models.IntegerField(default=0)

class monthlyorderAdmin(admin.ModelAdmin):
	list_display = ('name', 'qty')

class previewselections(models.Model):
	name=models.CharField(max_length=7, blank=False)

class previewselectionsAdmin(admin.ModelAdmin):
	list_display = ('name',)
