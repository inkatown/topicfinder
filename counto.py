from bs4 import BeautifulSoup
import urllib2, re, nltk
import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
#Matrix = [[0 for x in xrange(1000)] for x in xrange(1000)] 
new_dict = []
MatrixAll = []
new_dict.append('year-regi') 
year = None
abstract_counter = 0
def process_datamining():
  global year
  global abstract_counter
  conf_ count = {2002: 0,2003: 0,2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0};

  file = open('/Users/josehurtado/Downloads/DBLP-citation-Feb21.txt', 'r')
  year_l =''
  title = ''
  conf = ''
  counto = 0
  abstract = ''
  for line in file:
    if(line.startswith( '#*' )):
      title = line[2:] 
      title = title.strip()
    if(line.startswith( '#year' )):
      year_l = line[5:]
      year_l = year_l.strip()
      
      #print year
    if(line.startswith( '#conf' )):
      conf = line[5:]
      conf = conf.strip() 
    if(line.startswith( '#!' )):
      abstract = line[2:]
      abstract = abstract.strip()
      if(year_l == '2004'):
        counto = counto + 1
    if year_l in ['2002','2003','2004', '2005', '2006', '2007', '2008', '2009', '2010'] and conf in ['KDD', 'ICDM', 'SDM','ICML'] and abstract != '': # '2007', '2008', '2009', '2010', '2011']
      '''print "**title**"
      print title
      print "**conf**"
      print conf
      print "**year**"
      print year_l
      print '**abstract**'
      print abstract'''
      year = int(year_l)
      #abstract_counter = abstract_counter + 1
      
  print counto   
        #print seis
process_datamining()

