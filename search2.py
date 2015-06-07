import searchengine
crawler=searchengine.crawler('searchindex.db')
#crawler.calculatepagerank()

cur=crawler.con.execute('select * from pagerank order by score desc')
for i in range(3):
	print cur.next()

e=searchengine.searcher('searchindex.db')
e.query('malaysia')
