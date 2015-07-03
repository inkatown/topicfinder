from bs4 import BeautifulSoup
import urllib2, re, nltk
from nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
url = "http://dl.acm.org/citation.cfm?id=1137677&preflayout=flat#prox"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=hdr)
content = urllib2.urlopen(req).read()
soup = BeautifulSoup(content)
tablita = soup.find('table', {'class': 'text12' , 'border': '0'})
#for tabli in tablita:
#print 'huevonllege'
algo = tablita.findAll('tr') 
for num in algo:
  #print num
  #print "antes"
  uno = num.find('a', {'href' : re.compile(r"citation.cfm*")})
  if uno != None:
    print str(uno.contents[0])
  dos = num.find('span', {'id' : re.compile(r"toHide*")})
  if dos != None:
    vamos = nltk.word_tokenize(str(dos.div.contents[0]))
    finder = BigramCollocationFinder.from_words(vamos)
    print finder.nbest(bigram_measures.pmi, 10)  

  #print num.findNext('span', {'id' : re.compile(r"toHide*")})
  #if num.find("toHide") != :
#result = []
#allrows = soup.findAll('tr')
#for row in allrows:
#  result.append([])
#  allcols = row.findAll('td')
#  for col in allcols:
#    thestrings = [unicode(s) for s in col.findAll(text=True)]
#    thetext = ''.join(thestrings)
#    result[-1].append(thetext)


