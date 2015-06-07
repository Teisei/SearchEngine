rows=[('teisei',1,2,3),('shuntian',2,3,4),('xutao',3,4,5)]
locations=dict([(row[0],1000000) for row in rows])
print locations
for row in rows:
	print row[1:]
	loc=sum(row[1:])
	print loc
	if loc<locations[row[0]]:
		locations[row[0]]=loc