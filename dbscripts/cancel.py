import sys
import csv

lol=list(csv.reader(open(sys.argv[1], 'rb'), delimiter='\t'))

for x in range(0, len(lol)):
	if(re.match(^[A-Z]+\d+$, lol[x][0]), flags=0 )
		item = catalog.objects.get(itemId=lol[x][0])
		item.delete()
		
