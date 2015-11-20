import csv
import sys
import os

import django
from comicxpress_backend.api.models import *

if __name__ == '__main__':  
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comicxpress_backend.settings')

    	django.setup()

	lol= list(csv.reader(open(sys.argv[1], 'rb'), delimiter='\t'))

#print lol[1][1]

#from ../api/models import catalog

	for x in range(0, len(lol)):
		c = catalog()
		c.name=[x][3]
		c.price=[x][21]
		c.catalogid=[x][0]
		c.itemid=[x][1]
		c.discountcode=[x][2]
		c.categorycode=[x][4]
		c.orderdate=[x][9]
		c.selldate=[x][8]
		c.page=[x][11]
		c.save()

#	c=Catalog(name=[x][3], price=[x][21], catalogid=[x][0], itemid=[x][1], discountcode=[x][2], categorycode=[x][4], orderdate=[x][9], selldate=[x][8], page=[x][11])
#	c.save()
	
