from sqlite3 import dbapi2 as sqlite

class dbconnector:
	def __init__(self,dbname):
		self.con=sqlite.connect(dbname)
	def __del__(self):
		self.con.close()
	def dbcommit(self):
		self.con.commit()

	def createindextable(self):
	    self.con.execute('create table wordlocation(urlid,wordid,location)')
	    
	    self.con.execute('create index wordurlidx on wordlocation(wordid)')
	    self.dbcommit()
	
	def createtable(self,table,field):
		sqlstring='create table %s(%s)' % (table,field)
		print sqlstring
		self.con.execute(sqlstring)

	def insert(self,table,field,value,createnew=True):
		sqlstring="insert into %s (%s) values (%s)" % (table,field,value)
		print sqlstring
		self.con.execute(sqlstring)

	def search(self,table,field,condition,createnew=True):
		sqlstring='select %s from %s' % (field,table)
		if condition!=None:
			sqlstring+='where '+condition
		print sqlstring
		cur=self.con.execute(sqlstring)
		while 1:
			res=cur.fetchone()
			if res==None:
				break
			print res


