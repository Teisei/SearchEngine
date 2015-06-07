import searchengine
from sqlite3 import dbapi2 as sqlite
e=searchengine.searcher('searchindex.db')
print e.getmatchrows('malaysia')

mycon=sqlite.connect('searchindex.db')
sqlstring='select url from urllist '
cur=mycon.execute(sqlstring)

for num in range(0,43):
	res=cur.fetchone()
res=cur.fetchone()
print res
	#res=cur.fetchone()
	#if res==None:
	#	break
	#print res
