file = open('/Users/josehurtado/Downloads/DBLP-citation-Feb21.txt', 'r')

year =''
title = ''
conf = ''
abstract = ''
for line in file:
   if(line.startswith( '#*' )):
   	title = line[2:] 
   	title = title.strip()
   if(line.startswith( '#year' )):
   	year = line[5:]
   	year = year.strip()
   	#print year
   if(line.startswith( '#conf' )):
   	conf = line[5:]
   	conf = conf.strip() 
   if(line.startswith( '#!' )):
   	abstract = line[2:]
   	abstract = abstract.strip()
   if year in ['2006', '2007', '2008', '2009', '2010', '2011'] and conf in ['KDD', 'ICDM', 'SDM'] and abstract != '':
   	print "**title**"
   	print title
   	print "**conf**"
   	print conf
   	print "**year**"
   	print year
   	print '**abstract**'
   	print abstract
   abstract = ''

