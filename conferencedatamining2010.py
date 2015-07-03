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
#dictcount = []
removepalabras=['solve','data','algorithm','problem','result','significantly','method','outperform','synthet','real','propos','experiment','show','address','paper','formul']

def build_dataset(filtered_words):
  #check if word is in dictionary
  Matrixx=['?'] * 13270
#649
#720
#780
#591
#1081
  Matrixx[0] = year
  #Matrixx[1] = abstract_counter
  for wd in filtered_words:
    indexx = -1
    for wrd in new_dict:
      if wd == wrd:
        indexx = new_dict.index(wrd)

    if indexx != -1: # if word is in dicionary then add a value to the corresponding matrix
      Matrixx[indexx] = 't'

    else: # add word to dictionary then add corresponding value to the matrix
      if wd not in removepalabras:
        new_dict.append(wd)  
        Matrixx[new_dict.index(wd)] = 't'
  #print Matrixx
  MatrixAll.append(Matrixx)

def count_pattern(word1, word2):
  dictcount = {2002: 0,2003: 0,2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0};
  pattern_counter = 0
  indexx1 = -1
  indexx2 = -1
  for wrd in new_dict:
    if word1 == wrd:
      indexx1 = new_dict.index(word1)
    if word2 == wrd:
      indexx2 = new_dict.index(word2)


  if indexx1 != -1 and indexx2 != -1: # if pattern is found register in corresponding year
  #abs_local_counter = 0 
    for line in MatrixAll:
    #if abs_local_counter != line[1] # if the number changes then count 
      if line[indexx1] == 't' and line[indexx2] == 't':
        key = line[0] 
      #abs_local_counter = line[1]
        #if dictcount.has_key(key):
        dictcount[key] = dictcount[key] + 1
      #abs_local_counter = line[1]
 # return pattern_counter
  print dictcount.values()



def count_patternn(word1, word2, word3):
  dictcount = {2002: 0,2003: 0,2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0};
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

  if indexx1 != -1 and indexx2 != -1 and indexx3 != -1: # if pattern is found register in corresponding year
    for line in MatrixAll:
      if line[indexx1] == 't' and line[indexx2] == 't' and line[indexx3] == 't':
        key = line[0] 
          #if dictcount.has_key(key):
        dictcount[key] = dictcount[key] + 1

  print dictcount.values()


def count_patternnn(word1, word2, word3,word4):
  dictcount = {2002: 0,2003: 0,2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0};
  pattern_counter = 0
  indexx1 = -1
  indexx2 = -1
  indexx3 = -1
  indexx4 = -1


  for wrd in new_dict:
    if word1 == wrd:
      indexx1 = new_dict.index(word1)
    if word2 == wrd:
      indexx2 = new_dict.index(word2)
    if word3 == wrd:
      indexx3 = new_dict.index(word3)
    if word4 == wrd:
      indexx4 = new_dict.index(word4)

  if indexx1 != -1 and indexx2 != -1 and indexx3 != -1 and indexx4 != -1: # if pattern is found register in corresponding year
    for line in MatrixAll:
      if line[indexx1] == 't' and line[indexx2] == 't' and line[indexx3] == 't' and line[indexx4] == 't':
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
    seis[looper] = seis[looper].replace("?", "")
    looper += 1
  #filtered_words = [w for w in seis if not w in stopwords.words('english')]
  minlength = 2
  filtered_words = [token for token in seis if (not token in stopwords.words('english')) and len(token) >= minlength]
  #print stopwords.words('english')
  #print filtered_words
  #filtered verbs using tagger
  paco1 = []
  paco = nltk.pos_tag(filtered_words)
  #print paco
  for token in paco:
    if token[1] not in ['VB', 'VBD', 'VBG', 'VBN', 'VBP','VBZ']: 
      paco1.append(token[0])
  filtered_words = paco1
  #print 'after'
  #print filtered_words
  #end of removing verbs
 
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
  #soup = BeautifulSoup(content)
  soup = BeautifulSoup (content.decode('utf-8'))
  print content

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
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

  global year
  global abstract_counter

  year = 2010

  req = urllib2.Request(url, headers=hdr)
  content = urllib2.urlopen(req).read()
  #soup = BeautifulSoup(content)
  soup = BeautifulSoup (content)

  tablita = soup.find('table', {'class': 'table1'})
  #for tabli in tablita:
  num_articles = 0
  #print 'huevonllege'
  algo = tablita.findAll(True) 
  for num in algo:
    abstract_counter = abstract_counter + 1
    #print num
    #print "antes"
    uno = num.find('h3')
    if uno != None:
      tres = uno.get_text(strip=True).encode('utf-8')
      cinco = nltk.word_tokenize(tres)
      normalize_text(cinco)
    dos = num.find('p', {'class': 'abstracts'})
    if dos != None:
      cuatro = dos.get_text(strip=True).encode('utf-8')
      num_articles = num_articles + 1
      transaction = nltk.sent_tokenize(cuatro)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        normalize_text(seis)

def process_url2010():
  global year
  global abstract_counter

  year = 2010
  fh = open("/Users/josehurtado/conferenciaKDD.html","r")
  soup = BeautifulSoup(fh)
  tablita = soup.find('table', {'class': 'text12' , 'border': '0'})
  #for tabli in tablita:
  num_articles = 0
  #print 'huevonllege'
  algo = tablita.findAll('tr') 
  #print algo
  checker = 0 # not necessary

  for num in algo:
  #print num
  #print "antes"
    abstract_counter = abstract_counter + 1

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

def process_xml(xmlo):
  global year
  global abstract_counter

  year = 2010
  tree = ET.parse(xmlo)
  root = tree.getroot()
  checker = 0
  for country in root.findall('document'):
    abstract_counter = abstract_counter + 1

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



def process_datamining():
  global year
  global abstract_counter
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
      year_l = year_l.strip()
      #print year
    if(line.startswith( '#conf' )):
      conf = line[5:]
      conf = conf.strip() 
    if(line.startswith( '#!' )):
      abstract = line[2:]
      abstract = abstract.strip()
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
      
      cinco = nltk.word_tokenize(title)
      normalize_text(cinco)
      #print cinco
      transaction = nltk.sent_tokenize(abstract)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        normalize_text(seis)
        #print seis

    abstract = ''

def process_mining():
  global year
  global abstract_counter
  currsize = 0
  lista = []
  f = open('/Users/josehurtado/SDM2010conference.txt', 'r')
  year=2010
  title = ''
 
  abstract = ''
  line = f.readline()

  while line:
    lista.append(line)
    if (line.startswith( 'Abstract | PDF' )):

      #print "paco "+ line

      title = lista[currsize-4] 
      title = title.strip()
      #print title
      cinco = nltk.word_tokenize(title)
      normalize_text(cinco)


      f.readline()
      f.readline()
      f.readline()
      abstract = f.readline()
      #print abstract
      transaction = nltk.sent_tokenize(abstract)
      for wd in transaction:
        seis = nltk.word_tokenize(wd)
        normalize_text(seis)
      abstract_counter = abstract_counter + 1



    currsize = currsize + 1 

    line = f.readline()
  f.close()

  #for line in file:
    
  

    #abstract = ''

  #print num_articles
url = "http://dl.acm.org/citation.cfm?id=1137677&preflayout=flat#prox"
url1 = "http://dl.acm.org/citation.cfm?id=1270237&preflayout=flat"
url2 = "http://dl.acm.org/citation.cfm?id=1370018&preflayout=flat"
url3 = "http://dl.acm.org/citation.cfm?id=1586616&preflayout=flat" # does not work 
url4 = "http://dl.acm.org/citation.cfm?id=1808984&preflayout=flat#prox"
url5 = "http://dl.acm.org/citation.cfm?id=1988008&preflayout=flat"
url6 = "http://dl.acm.org/citation.cfm?id=1835804&preflayout=flat"
url7 = "http://www.icml2010.org/abstracts.html"


icac2009 = "http://dl.acm.org/citation.cfm?id=1555312&picked=prox&preflayout=flat"
icac2010 = "http://dl.acm.org/citation.cfm?id=1809049&preflayout=flat"
icac2011 = "http://dl.acm.org/citation.cfm?id=1998582&preflayout=flat"


xml1 = "/Users/josehurtado/icac2006.xml"
xml2 = "/Users/josehurtado/icac2007.xml"
xml3 = "/Users/josehurtado/icac2008.xml"
xml4 = "/Users/josehurtado/icdm2010.xml"

#process_datamining()
process_xml(xml4) 
process_url2009(url7)
process_url2010()
process_mining()
print "This is the number of abstracts" + str(abstract_counter)

def print_arff_file():
  print '%% Number of Attributes: %d'% (len(new_dict),)

  print '@relation icayseams'
  
  for pal in new_dict:
    print '@attribute '+ pal + ' {t}'

  print '@data'

  for line in MatrixAll:
    print ", ".join(str(e) for e in line)
    #print '\n'


print_arff_file()
