import csv
import sys

lol= list(csv.reader(open(sys.argv[1], 'rb'), delimiter='\t'))

#print lol[1][1]

from ../api/models import catalog

for x in range(0, len(lol)):
	c=Catalog(name=[x][3], price=[x][21], catalogId=[x][0], itemId=[x][1], discountCode=[x][2], categoryCode=[x][4], orderDate=[x][9], sellDate=[x][8], page=[x][11])
	c.save()
	
