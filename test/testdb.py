import database
def list2str(mylist):
	mystr=mylist[0]
	if len(mylist)>1:
		for num in range(1,len(mylist)):
			mystr+=','+mylist[num]
	return mystr
def list2str2(mylist):
	mystr='\''+mylist[0]+'\''
	if len(mylist)>1:
		for num in range(1,len(mylist)):
			mystr+=',\''+mylist[num]+'\''
	return mystr

mydbcon=database.dbconnector('mydb.db')
table='person'

field=['id','name','age']
fieldstr=list2str(field)
#mydbcon.createtable(table,fieldstr)

value=['001','teisei','18']
valuestr=list2str2(value)
mydbcon.insert(table,fieldstr,valuestr)


mydbcon.search(table,'name',None)