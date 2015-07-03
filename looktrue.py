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
#dictcount = []

def build_dataset(filtered_words):
  #check if word is in dictionary
  Matrixx=['?'] * 3206
#649
#720
#780
#591
#1081
  Matrixx[0] = year
  for wd in filtered_words:
    indexx = -1
    for wrd in new_dict:
      if wd == wrd:
        indexx = new_dict.index(wrd)

    if indexx != -1: # if word is in dicionary then add a value to the corresponding matrix
      Matrixx[indexx] = 't'

    else: # add word to dictionary then add corresponding value to the matrix
        new_dict.append(wd)  
        Matrixx[new_dict.index(wd)] = 't'
  #print Matrixx
  MatrixAll.append(Matrixx)

def count_pattern(word1, word2):
  dictcount = {2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0, 2011: 0};
  pattern_counter = 0
  indexx1 = -1
  indexx2 = -1
  for wrd in new_dict:
    if word1 == wrd:
      indexx1 = new_dict.index(word1)
    if word2 == wrd:
      indexx2 = new_dict.index(word2)


  if indexx1 != -1 and indexx2 != -1: # if word is in dicionary then add a value to the corresponding matrix
    for line in MatrixAll:
      if line[indexx1] == 't' and line[indexx2] == 't':
        key = line[0] 
        #if dictcount.has_key(key):
        dictcount[key] = dictcount[key] + 1
 # return pattern_counter
  print dictcount.values()



def count_patternn(word1, word2, word3):
  dictcount = {2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0, 2011: 0};
  pattern_counter = 0
  indexx1 = -1
  indexx2 = -1
  indexx3 = -1

  for wrd in new_dict:
    if word1 == wrd:
      indexx1 = new_dict.index(word1)
    if word2 == wrd:
      indexx2 = new_dict.index(word2)
    if word3 == wrd:
      indexx3 = new_dict.index(word3)

  if indexx1 != -1 and indexx2 != -1 and indexx3 != -1: # if the combination of words are in dicionary then add a value to the corresponding matrix
    for line in MatrixAll:
      if line[indexx1] == 't' and line[indexx2] == 't' and line[indexx3] == 't':
        key = line[0] 
          #if dictcount.has_key(key):
        dictcount[key] = dictcount[key] + 1

  print dictcount.values()




def normalize_text(seis):
  #Normalizing to lower
  looper = 0
  for token in seis:
    seis[looper] = token.lower()
    seis[looper] = seis[looper].replace("'", "")
    seis[looper] = seis[looper].replace(",", "")
    looper += 1
  #filtered_words = [w for w in seis if not w in stopwords.words('english')]
  minlength = 2
  filtered_words = [token for token in seis if (not token in stopwords.words('english')) and len(token) >= minlength]
  #print stopwords.words('english')
 
  #Stemming
  porter = nltk.PorterStemmer()
  looper = 0
  for token in filtered_words:
    filtered_words[looper] = porter.stem(token)
    looper += 1
   #Lemmatization
  lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
  looper = 0
  for token in filtered_words:
    filtered_words[looper] = lmtzr.lemmatize(token)
    looper += 1
  #print "***before removing the stopwords***"
  #print seis
  #print "***after removing the stopwords***"
  #print filtered_words
  build_dataset(filtered_words)

def process_url(url):
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
  num_articles = 0
  #print 'huevonllege'
  algo = tablita.findAll('tr') 
  for num in algo:
    #print num
    #print "antes"
    uno = num.find('a', {'href' : re.compile(r"citation.cfm*")})
    if uno != None:
      tres = str(uno.get_text(strip=True))
      cinco = nltk.word_tokenize(tres)
      normalize_text(cinco)

    dos = num.find('span', {'id' : re.compile(r"toHide*")})
    if dos != None:
      cuatro = str(dos.div.get_text(strip=True))
      num_articles = num_articles + 1
      transaction = nltk.sent_tokenize(cuatro)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        normalize_text(seis)
  #print num_articles

def process_url2009(url):
  '''hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

  req = urllib2.Request(url, headers=hdr)
  content = urllib2.urlopen(req).read()'''
  fh = open("/Users/josehurtado/2009.html","r")
  soup = BeautifulSoup(fh)
  tablita = soup.find('table', {'class': 'text12' , 'border': '0'})
  #for tabli in tablita:
  num_articles = 0
  #print 'huevonllege'
  algo = tablita.findAll('tr') 
  #print algo
  for num in algo:
    checker = 0 # not necessary
    uno = num.find('a', {'href' : re.compile(r"citation.cfm*")})
    if uno != None and str(uno.get_text(strip=True)) not in ['Cover', 'Title page', 'Copyright page', 'Foreword'] :
      tres = str(uno.get_text(strip=True))
      cinco = nltk.word_tokenize(tres)
      normalize_text(cinco)
      checker = 1
    dos = num.find('span', {'id' : re.compile(r"toHide*")})
    if dos != None and checker == 1:
      cuatro = str(dos.div.get_text(strip=True))
      num_articles = num_articles + 1
      transaction = nltk.sent_tokenize(cuatro)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        normalize_text(seis)
  #print num_articles

def process_xml(xmlo):
  
  tree = ET.parse(xmlo)
  root = tree.getroot()
  checker = 0
  for country in root.findall('document'):
    title = country.find('title').text
    if title != None:
      cinco = nltk.word_tokenize(title)
      normalize_text(cinco)
      checker = 1
    abstract = country.find('abstract').text
    if abstract != None and checker == 1:
      transaction = nltk.sent_tokenize(abstract)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        normalize_text(seis)

def process_url1(url):
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
  num_articles = 0
  #print 'huevonllege'
  algo = tablita.findAll('tr') 
  for num in algo:
    #print num
    #print "antes"
    uno = num.find('a', {'href' : re.compile(r"citation.cfm*")})
    if uno != None:
      tres = str(uno.get_text(strip=True))
      cinco = nltk.word_tokenize(tres)
      print(cinco)

    dos = num.find('span', {'id' : re.compile(r"toHide*")})
    if dos != None:
      cuatro = str(dos.div.get_text(strip=True))
      num_articles = num_articles + 1
      transaction = nltk.sent_tokenize(cuatro)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        print(seis)
  #print num_articles

def process_url20091(url):
  '''hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

  req = urllib2.Request(url, headers=hdr)
  content = urllib2.urlopen(req).read()'''
  fh = open("/Users/josehurtado/2009.html","r")
  soup = BeautifulSoup(fh)
  tablita = soup.find('table', {'class': 'text12' , 'border': '0'})
  #for tabli in tablita:
  num_articles = 0
  #print 'huevonllege'
  algo = tablita.findAll('tr') 
  #print algo
  for num in algo:
    checker = 0 # not necessary
    uno = num.find('a', {'href' : re.compile(r"citation.cfm*")})
    if uno != None and str(uno.get_text(strip=True)) not in ['Cover', 'Title page', 'Copyright page', 'Foreword'] :
      tres = str(uno.get_text(strip=True))
      cinco = nltk.word_tokenize(tres)
      print(cinco)
      checker = 1
    dos = num.find('span', {'id' : re.compile(r"toHide*")})
    if dos != None and checker == 1:
      cuatro = str(dos.div.get_text(strip=True))
      num_articles = num_articles + 1
      transaction = nltk.sent_tokenize(cuatro)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        print(seis)
  #print num_articles

def process_xml1(xmlo):
  
  tree = ET.parse(xmlo)
  root = tree.getroot()
  checker = 0
  for country in root.findall('document'):
    title = country.find('title').text
    if title != None:
      cinco = nltk.word_tokenize(title)
      print(cinco)
      checker = 1
    abstract = country.find('abstract').text
    if abstract != None and checker == 1:
      transaction = nltk.sent_tokenize(abstract)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        print(seis)

def process_datamining():
  file = open('/Users/josehurtado/Downloads/DBLP-citation-Feb21.txt', 'r')
  year_l =''
  title = ''
  conf = ''
  abstract = ''
  for line in file:
    if(line.startswith( '#*' )):
      title = line[2:] 
      title = title.strip()
    if(line.startswith( '#year' )):
      year_l = line[5:]
      year_l = year.strip()
      #print year
    if(line.startswith( '#conf' )):
      conf = line[5:]
      conf = conf.strip() 
    if(line.startswith( '#!' )):
      abstract = line[2:]
      abstract = abstract.strip()
    if year_l in ['2006', '2007', '2008', '2009', '2010', '2011'] and conf in ['KDD', 'ICDM', 'SDM'] and abstract != '':
      print "**title**"
      print title
      print "**conf**"
      print conf
      print "**year**"
      print year_l
      print '**abstract**'
      print abstract
      year = int(year_l)
      
      cinco = nltk.word_tokenize(title)
      print(cinco)
      transaction = nltk.sent_tokenize(abstract)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        print(seis)
    abstract = ''
  #print num_articles
url = "http://dl.acm.org/citation.cfm?id=1137677&preflayout=flat#prox"
url1 = "http://dl.acm.org/citation.cfm?id=1270237&preflayout=flat"
url2 = "http://dl.acm.org/citation.cfm?id=1370018&preflayout=flat"
url3 = "http://dl.acm.org/citation.cfm?id=1586616&preflayout=flat" # does not work 
url4 = "http://dl.acm.org/citation.cfm?id=1808984&preflayout=flat#prox"
url5 = "http://dl.acm.org/citation.cfm?id=1988008&preflayout=flat"


icac2009 = "http://dl.acm.org/citation.cfm?id=1555312&picked=prox&preflayout=flat"
icac2010 = "http://dl.acm.org/citation.cfm?id=1809049&preflayout=flat"
icac2011 = "http://dl.acm.org/citation.cfm?id=1998582&preflayout=flat"


xml1 = "/Users/josehurtado/icac2006.xml"
xml2 = "/Users/josehurtado/icac2007.xml"
xml3 = "/Users/josehurtado/icac2008.xml"


wdd1 = 'adapt'
wdd2 = 'paper'

year = 2006
process_url1(url)
process_xml1(xml1)
#firstnum = count_pattern(wdd1, wdd2)

year = 2007
process_url1(url1)
process_xml1(xml2)
#secondnum = count_pattern(wdd1, wdd2) - firstnum

year = 2008
process_url1(url2)
process_xml1(xml3)
#thirdnum = count_pattern(wdd1, wdd2)- secondnum - firstnum

year = 2009
process_url20091(url3)
process_url1(icac2009)
#fourthnum = count_pattern(wdd1, wdd2) - thirdnum - secondnum - firstnum

year = 2010
process_url1(url4)
process_url1(icac2010)
#fithnum = count_pattern(wdd1, wdd2) - fourthnum -thirdnum  - secondnum - firstnum

year = 2011
process_url1(url5)
process_url1(icac2011)
#sixnum = count_pattern(wdd1, wdd2) - fithnum - fourthnum -thirdnum  - secondnum - firstnum

#print firstnum , " " ,secondnum, " " , thirdnum, " ", fourthnum, " ", fithnum, " ",  sixnum
'''count_patternn('manag','center','data')
count_patternn('center','power','data')
count_patternn('workload','center','data')
count_patternn('autonom','center','data')
count_patternn('applic','center','data')
count_patternn('use','studi','case')
count_patternn('virtual','center','data')
count_patternn('effici','center','data')
count_patternn('system','center','data')
count_patternn('oper','center','data')
count_patternn('machin','vm','virtual')
count_pattern('center','data')
count_patternn('data','power','center')
count_patternn('use','center','data')
count_patternn('data','virtual','center')
count_pattern('solv','problem')
count_patternn('applic','alloc','resourc')
count_pattern('especi','system')
count_pattern('record','proceed')
count_pattern('mix','workload')
count_patternn('virtual','vm','machin')
count_pattern('composit','servic')
count_patternn('adapt','present','paper')
count_patternn('self-adapt','softwar','system')
count_patternn('autonom','distribut','system')
count_patternn('softwar','complex','system')
count_patternn('applic','provis','resourc')
count_patternn('self-adapt','paper','system')
count_pattern('secur','system')
count_pattern('alloc','resourc')
count_patternn('use','case','studi')
count_patternn('manag','distribut','system')
count_patternn('dynam','control','system')
count_patternn('adapt','properti','system')
count_patternn('manag','present','paper')
count_patternn('adapt','behavior','system')
count_patternn('autonom','adapt','system')
count_patternn('data','workload','center')
count_pattern('administr','system')
count_patternn('self-adapt','approach','system')
count_patternn('manag','control','system')
count_pattern('increasingli','system')
count_patternn('data','oper','center')
count_pattern('consumpt','power')
count_patternn('manag','data','center')
count_patternn('comput','manag','system')
count_patternn('paper','distribut','system')
count_patternn('data','effici','center')
count_patternn('manag','approach','system')
count_patternn('base','control','system')
count_patternn('dynam','provis','resourc')
count_patternn('perform','base','model')
count_pattern('host','applic')
count_patternn('autonom','data','center')
count_patternn('autonom','polici','system')
count_pattern('case','studi')
count_patternn('comput','control','system')
count_pattern('share','resourc')
count_pattern('distribut','system')
count_pattern('workshop','softwar')
count_patternn('autonom','present','system')
count_patternn('comput','adapt','system')
count_patternn('comput','perform','system')
count_pattern('oper','system')
count_pattern('consolid','virtual')
count_pattern('save','energi')
count_patternn('data','monitor','system')
count_pattern('self-adapt','system')
count_patternn('applic','data','center')
count_patternn('comput','distribut','system')
count_patternn('paper','softwar','system')
count_patternn('softwar','chang','system')
count_patternn('approach','present','paper')
count_pattern('condit','system')
count_pattern('emerg','system')
count_patternn('manag','perform','system')
count_patternn('adapt','requir','system')
count_pattern('loop','system')
count_pattern('loop','control')
count_patternn('manag','model','system')
count_pattern('web','servic')
count_patternn('system','properti','adapt')
count_patternn('use','present','system')
count_pattern('must','system')
count_pattern('proceed','confer')
count_patternn('comput','dynam','system')
count_patternn('model','control','system')
count_pattern('element','autonom')
count_pattern('sensor','network')
count_patternn('comput','applic','system')
count_patternn('manag','dynam','system')
count_patternn('approach','softwar','system')
count_patternn('resourc','control','manag')
count_patternn('paper','control','system')
count_pattern('structur','system')
count_pattern('behavior','system')
count_patternn('autonom','architectur','system')
count_pattern('continu','system')
count_pattern('self-heal','system')
count_patternn('adapt','dynam','system')'''

def print_arff_file():
  print '@relation icayseams'
  
  for pal in new_dict:
    print '@attribute '+ pal + ' {t}'
  print len(new_dict)

  print '@data'

  for line in MatrixAll:
    print ", ".join(str(e) for e in line)
    #print '\n'

#print_arff_file()

'''
=== Run information ===

Scheme:       weka.associations.Apriori -N 10 -T 0 -C 0.3 -D 0.05 -U 1.0 -M 0.025 -S -1.0 -c -1
Relation:     todoicaseam
Instances:    2101
Attributes:   3205
[list of attributes omitted]
=== Associator model (full training set) ===


Apriori
=======

Minimum support: 0.03 (53 instances)
Minimum metric <confidence>: 0.3
Number of cycles performed: 20

Generated sets of large itemsets:

Size of set of large itemsets L(1): 81

Size of set of large itemsets L(2): 21

Best rules found:

 1. center=t 83 ==> data=t 82    conf:(0.99)
 2. distribut=t 105 ==> system=t 65    conf:(0.62)
 3. self-adapt=t 100 ==> system=t 61    conf:(0.61)
 4. control=t 153 ==> system=t 74    conf:(0.48)
 5. softwar=t 170 ==> system=t 80    conf:(0.47)
 6. data=t 177 ==> center=t 82    conf:(0.46)
 7. present=t 127 ==> paper=t 58    conf:(0.46)
 8. autonom=t 250 ==> system=t 114    conf:(0.46)
 9. manag=t 220 ==> system=t 91    conf:(0.41)
10. adapt=t 322 ==> system=t 132    conf:(0.41)

Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
13   12   11   6   22   18
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
24   9   5   1   11   15
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
2   6   9   0   13   31
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
13   16   11   0   13   21
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
11   8   13   3   15   30
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
13   12   11   6   22   18
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
14   10   8   1   8   17
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
10   4   3   1   5   7
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
6   6   6   1   5   8
Jose-Hurtados-MacBook-Pro:~ josehurtado$ python looktrue.py
13   7   5   0   9   15
Jose-Hurtados-MacBook-Pro:~ josehurtado$ 



1350
Apriori
=======

Minimum support: 0.01 (11 instances)
Minimum metric <confidence>: 0.4
Number of cycles performed: 2

Generated sets of large itemsets:

Size of set of large itemsets L(1): 513

Size of set of large itemsets L(2): 820

Size of set of large itemsets L(3): 121

Best rules found:

  1. manag=t center=t 27 ==> data=t 27    conf:(1)
  2. center=t power=t 19 ==> data=t 19    conf:(1)
  3. workload=t center=t 15 ==> data=t 15    conf:(1)
  4. autonom=t center=t 14 ==> data=t 14    conf:(1)
  5. applic=t center=t 14 ==> data=t 14    conf:(1)
  6. use=t studi=t 13 ==> case=t 13    conf:(1)
  7. virtual=t center=t 13 ==> data=t 13    conf:(1)
  8. effici=t center=t 13 ==> data=t 13    conf:(1)
  9. system=t center=t 12 ==> data=t 12    conf:(1)
 10. oper=t center=t 11 ==> data=t 11    conf:(1)
 11. machin=t vm=t 11 ==> virtual=t 11    conf:(1)
 12. center=t 83 ==> data=t 82    conf:(0.99)
 13. data=t power=t 20 ==> center=t 19    conf:(0.95)
 14. use=t center=t 12 ==> data=t 11    conf:(0.92)
 15. data=t virtual=t 15 ==> center=t 13    conf:(0.87)
 16. solv=t 14 ==> problem=t 12    conf:(0.86)
 17. applic=t alloc=t 20 ==> resourc=t 17    conf:(0.85)
 18. especi=t 13 ==> system=t 11    conf:(0.85)
 19. record=t 13 ==> proceed=t 11    conf:(0.85)
 20. mix=t 13 ==> workload=t 11    conf:(0.85)
 21. virtual=t vm=t 13 ==> machin=t 11    conf:(0.85)
 22. composit=t 30 ==> servic=t 25    conf:(0.83)
 23. adapt=t present=t 18 ==> paper=t 15    conf:(0.83)
 24. self-adapt=t softwar=t 27 ==> system=t 22    conf:(0.81)
 25. autonom=t distribut=t 16 ==> system=t 13    conf:(0.81)
 26. softwar=t complex=t 16 ==> system=t 13    conf:(0.81)
 27. applic=t provis=t 16 ==> resourc=t 13    conf:(0.81)
 28. self-adapt=t paper=t 19 ==> system=t 15    conf:(0.79)
 29. secur=t 14 ==> system=t 11    conf:(0.79)
 30. alloc=t 57 ==> resourc=t 44    conf:(0.77)
 31. use=t case=t 17 ==> studi=t 13    conf:(0.76)
 32. manag=t distribut=t 24 ==> system=t 18    conf:(0.75)
 33. dynam=t control=t 16 ==> system=t 12    conf:(0.75)
 34. adapt=t properti=t 15 ==> system=t 11    conf:(0.73)
 35. manag=t present=t 15 ==> paper=t 11    conf:(0.73)
 36. adapt=t behavior=t 18 ==> system=t 13    conf:(0.72)
 37. autonom=t adapt=t 35 ==> system=t 25    conf:(0.71)
 38. data=t workload=t 21 ==> center=t 15    conf:(0.71)
 39. administr=t 24 ==> system=t 17    conf:(0.71)
 40. self-adapt=t approach=t 17 ==> system=t 12    conf:(0.71)
 41. manag=t control=t 30 ==> system=t 21    conf:(0.7)
 42. increasingli=t 20 ==> system=t 14    conf:(0.7)
 43. data=t oper=t 16 ==> center=t 11    conf:(0.69)
 44. consumpt=t 25 ==> power=t 17    conf:(0.68)
 45. manag=t data=t 40 ==> center=t 27    conf:(0.68)
 46. comput=t manag=t 27 ==> system=t 18    conf:(0.67)
 47. paper=t distribut=t 21 ==> system=t 14    conf:(0.67)
 48. data=t effici=t 20 ==> center=t 13    conf:(0.65)
 49. manag=t approach=t 17 ==> system=t 11    conf:(0.65)
 50. base=t control=t 17 ==> system=t 11    conf:(0.65)
 51. dynam=t provis=t 17 ==> resourc=t 11    conf:(0.65)
 52. perform=t base=t 17 ==> model=t 11    conf:(0.65)
 53. host=t 22 ==> applic=t 14    conf:(0.64)
 54. autonom=t data=t 22 ==> center=t 14    conf:(0.64)
 55. autonom=t polici=t 19 ==> system=t 12    conf:(0.63)
 56. case=t 46 ==> studi=t 29    conf:(0.63)
 57. comput=t control=t 24 ==> system=t 15    conf:(0.63)
 58. share=t 29 ==> resourc=t 18    conf:(0.62)
 59. distribut=t 105 ==> system=t 65    conf:(0.62)
 60. workshop=t 21 ==> softwar=t 13    conf:(0.62)
 61. autonom=t present=t 21 ==> system=t 13    conf:(0.62)
 62. comput=t adapt=t 21 ==> system=t 13    conf:(0.62)
 63. comput=t perform=t 21 ==> system=t 13    conf:(0.62)
 64. oper=t 78 ==> system=t 48    conf:(0.62)
 65. consolid=t 18 ==> virtual=t 11    conf:(0.61)
 66. save=t 18 ==> energi=t 11    conf:(0.61)
 67. data=t monitor=t 18 ==> system=t 11    conf:(0.61)
 68. self-adapt=t 100 ==> system=t 61    conf:(0.61)
 69. applic=t data=t 23 ==> center=t 14    conf:(0.61)
 70. comput=t distribut=t 20 ==> system=t 12    conf:(0.6)
 71. paper=t softwar=t 20 ==> system=t 12    conf:(0.6)
 72. softwar=t chang=t 20 ==> system=t 12    conf:(0.6)
 73. approach=t present=t 20 ==> paper=t 12    conf:(0.6)
 74. condit=t 27 ==> system=t 16    conf:(0.59)
 75. emerg=t 22 ==> system=t 13    conf:(0.59)
 76. manag=t perform=t 34 ==> system=t 20    conf:(0.59)
 77. adapt=t requir=t 34 ==> system=t 20    conf:(0.59)
 78. loop=t 24 ==> system=t 14    conf:(0.58)
 79. loop=t 24 ==> control=t 14    conf:(0.58)
 80. manag=t model=t 24 ==> system=t 14    conf:(0.58)
 81. web=t 43 ==> servic=t 25    conf:(0.58)
 82. system=t properti=t 19 ==> adapt=t 11    conf:(0.58)
 83. use=t present=t 19 ==> system=t 11    conf:(0.58)
 84. must=t 28 ==> system=t 16    conf:(0.57)
 85. proceed=t 21 ==> confer=t 12    conf:(0.57)
 86. comput=t dynam=t 21 ==> system=t 12    conf:(0.57)
 87. model=t control=t 21 ==> system=t 12    conf:(0.57)
 88. element=t 23 ==> autonom=t 13    conf:(0.57)
 89. sensor=t 23 ==> network=t 13    conf:(0.57)
 90. comput=t applic=t 23 ==> system=t 13    conf:(0.57)
 91. manag=t dynam=t 23 ==> system=t 13    conf:(0.57)
 92. approach=t softwar=t 23 ==> system=t 13    conf:(0.57)
 93. resourc=t control=t 23 ==> manag=t 13    conf:(0.57)
 94. paper=t control=t 25 ==> system=t 14    conf:(0.56)
 95. structur=t 43 ==> system=t 24    conf:(0.56)
 96. behavior=t 65 ==> system=t 36    conf:(0.55)
 97. autonom=t architectur=t 20 ==> system=t 11    conf:(0.55)
 98. continu=t 31 ==> system=t 17    conf:(0.55)
 99. self-heal=t 31 ==> system=t 17    conf:(0.55)
100. adapt=t dynam=t 44 ==> system=t 24    conf:(0.55)

I am done bitches


      
'''


