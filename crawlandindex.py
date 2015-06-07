import searchengine
pagelist=['file:///C:/CodeSpace/Programming%20Collective%20Intelligence/PCI_Code/chapter4/pages/index.html']
#pagelist=['http://nlp.stanford.edu/IR-book/html/htmledition/irbook.html']
crawler=searchengine.crawler('searchindex.db')
crawler.createindextables()
crawler.crawl(pagelist)

crawler.calculatepagerank()
print [row for row in crawler.con.execute('select rowid from wordlist')]
