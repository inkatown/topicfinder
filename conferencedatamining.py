from bs4 import BeautifulSoup
import urllib2, re, nltk
import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import codecs
#Matrix = [[0 for x in xrange(1000)] for x in xrange(1000)] 
class BuildAbstractMatrix:
  new_dict = []
  MatrixAll = []
  year = None
  abstract_counter = 0
  #dictcount = []
  removepalabras=['solve','data','algorithm','problem','result','significantly','method','outperform','synthet','real','propos','experiment','show','address','paper','formul']
  def __init__(self):
    self.new_dict.append('year-regi') 
    self.new_dict.append('abstract-counter') 
  def build_dataset(self, filtered_words):
    #check if word is in dictionary
    Matrixx=['?'] * 14319
  #649
  #720
  #780
  #591
  #1081
    Matrixx[0] = self.year

    Matrixx[1] = self.abstract_counter
    for wd in filtered_words:
      indexx = -1
      for wrd in self.new_dict:
        if wd == wrd:
          indexx = self.new_dict.index(wrd)

      if indexx != -1: # if word is in dicionary then add a value to the corresponding matrix
        Matrixx[indexx] = 't'

      else: # add word to dictionary then add corresponding value to the matrix
        if wd not in self.removepalabras:
          self.new_dict.append(wd)  
          Matrixx[self.new_dict.index(wd)] = 't'
    #print Matrixx
    self.MatrixAll.append(Matrixx)
  def normalize_text(self, seis):
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
    stopwords1 = [word.encode('utf-8') for word in stopwords.words('english')]
    filtered_words = [token for token in seis if (not token in stopwords1) and len(token) >= minlength]
    #print stopwords.words('english')
    #print filtered_words
    #filtered verbs using tagger
    paco1 = []
    #print filtered_words
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
    self.build_dataset(filtered_words)

  def process_url(self, url):
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
        self.normalize_text(cinco)

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
        self.normalize_text(cinco)
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

  def process_xml_old(self, xmlo):
    
    tree = ET.parse(xmlo)
    root = tree.getroot()
    checker = 0
    for country in root.findall('document'):
      title = country.find('title').text
      if title != None:
        cinco = nltk.word_tokenize(title)
        self.normalize_text(cinco)
        checker = 1
      abstract = country.find('abstract').text
      if abstract != None and checker == 1:
        transaction = nltk.sent_tokenize(abstract)
        for wd in transaction:
          seis = nltk.word_tokenize(wd)
          normalize_text(seis)



  def process_datamining(self):
    #global year
    #global abstract_counter
    file = codecs.open('/Users/josehurtado/Downloads/DBLP-citation-Feb21.txt', 'r','utf-8')
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
      if year_l in ['2002','2003','2004', '2005', '2006', '2007', '2008', '2009'] and conf in ['KDD', 'ICDM', 'SDM','ICML'] and abstract != '': # '2007', '2008', '2009', '2010', '2011']
        '''print "**title**"
        print title
        print "**conf**"
        print conf
        print "**year**"
        print year_l
        print '**abstract**'
        print abstract'''
        self.year = int(year_l)
        #abstract_counter = abstract_counter + 1
        #title = title.text
        cinco = nltk.word_tokenize(title)
        self.normalize_text(cinco)
        #print cinco
        transaction = nltk.sent_tokenize(abstract)
        for wd in transaction:
          seis = nltk.word_tokenize(wd)
          self.normalize_text(seis)
          #print seis
        self.abstract_counter = self.abstract_counter + 1


      abstract = ''
    #print num_articles
  def process_url_icml(self, url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}

    #global year
    #global self.abstract_counter

    self.year = 2010

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
      self.abstract_counter = self.abstract_counter + 1
      #print num
      #print "antes"
      uno = num.find('h3')
      if uno != None:
        tres = uno.get_text(strip=True).encode('utf-8')
        cinco = nltk.word_tokenize(tres)
        self.normalize_text(cinco)
      dos = num.find('p', {'class': 'abstracts'})
      if dos != None:
        cuatro = dos.get_text(strip=True).encode('utf-8')
        num_articles = num_articles + 1
        transaction = nltk.sent_tokenize(cuatro)
        for wd in transaction:
          seis = nltk.word_tokenize(wd)
          normalize_text(seis)

  def process_KDD2010(self):
    #global self.year
    #global self.abstract_counter

    self.year = 2010
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
      self.abstract_counter = self.abstract_counter + 1

      uno = num.find('a', {'href' : re.compile(r"citation.cfm*")})
      if uno != None:
        tres = str(uno.get_text(strip=True))
        cinco = nltk.word_tokenize(tres)
        self.normalize_text(cinco)
      dos = num.find('span', {'id' : re.compile(r"toHide*")})
      if dos != None:
        cuatro = str(dos.div.get_text(strip=True))
        num_articles = num_articles + 1
        transaction = nltk.sent_tokenize(cuatro)
        for wd in transaction:
          seis = nltk.word_tokenize(wd)
          normalize_text(seis)
    #print num_articles

  def process_xml(self, xmlo):
    #global self.year
    #global self.abstract_counter

    self.year = 2010
    tree = ET.parse(xmlo)
    root = tree.getroot()
    checker = 0
    for country in root.findall('document'):
      self.abstract_counter = self.abstract_counter + 1

      title = country.find('title').text
      if title != None:
        cinco = nltk.word_tokenize(title)
        self.normalize_text(cinco)
        checker = 1
      abstract = country.find('abstract').text
      if abstract != None and checker == 1:
        transaction = nltk.sent_tokenize(abstract)
        for wd in transaction:
          seis = nltk.word_tokenize(wd)
          normalize_text(seis)





  def process_SDM2010(self):
    #global self.year
    #global self.abstract_counter
    currsize = 0
    lista = []
    f = open('/Users/josehurtado/SDM2010conference.txt', 'r')
    self.year=2010
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
        self.normalize_text(cinco)


        f.readline()
        f.readline()
        f.readline()
        abstract = f.readline()
        #print abstract
        transaction = nltk.sent_tokenize(abstract)
        for wd in transaction:
          seis = nltk.word_tokenize(wd)
          normalize_text(seis)
        self.abstract_counter = self.abstract_counter + 1



      currsize = currsize + 1 

      line = f.readline()
    f.close()

def count_pattern(word1, word2):
  dictcount = {2002: 0,2003: 0,2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0};
  pattern_counter = 0
  indexx1 = -1
  indexx2 = -1
  for wrd in self.new_dict:
    if word1 == wrd:
      indexx1 = self.new_dict.index(word1)
    if word2 == wrd:
      indexx2 = self.new_dict.index(word2)


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

  for wrd in self.new_dict:
    if word1 == wrd:
      indexx1 = self.new_dict.index(word1)
    if word2 == wrd:
      indexx2 = self.new_dict.index(word2)
    if word3 == wrd:
      indexx3 = self.new_dict.index(word3)

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


  for wrd in self.new_dict:
    if word1 == wrd:
      indexx1 = self.new_dict.index(word1)
    if word2 == wrd:
      indexx2 = self.new_dict.index(word2)
    if word3 == wrd:
      indexx3 = self.new_dict.index(word3)
    if word4 == wrd:
      indexx4 = self.new_dict.index(word4)

  if indexx1 != -1 and indexx2 != -1 and indexx3 != -1 and indexx4 != -1: # if pattern is found register in corresponding year
    for line in MatrixAll:
      if line[indexx1] == 't' and line[indexx2] == 't' and line[indexx3] == 't' and line[indexx4] == 't':
        key = line[0] 
          #if dictcount.has_key(key):
        dictcount[key] = dictcount[key] + 1

  print dictcount.values()






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
dprocss = BuildAbstractMatrix()

dprocss.process_datamining()
#dprocss.process_xml(xml4) 
#dprocss.process_url_icml(url7)
#dprocss.process_KDD2010()
#dprocss.process_SDM2010()
print "This is the number of abstracts" + str(dprocss.abstract_counter)

#sixnum = count_pattern(wdd1, wdd2) - fithnum - fourthnum -thirdnum  - secondnum - firstnum

#print firstnum , " " ,secondnum, " " , thirdnum, " ", fourthnum, " ", fithnum, " ",  sixnum


def print_arff_file():
  print '%% Number of Attributes: %d'% (len(self.new_dict),)

  print '@relation icayseams'
  
  for pal in self.new_dict:
    print '@attribute '+ pal + ' {t}'

  print '@data'

  for line in self.MatrixAll:
    print ", ".join(str(e) for e in line)
    #print '\n'

'''count_pattern('regress', 'logist')
count_pattern('random', 'walk')
count_pattern('neural', 'network')
count_pattern('mixtur', 'model')
count_pattern('detect', 'anomali')
count_pattern('search', 'engin')
count_pattern('model', 'graphic')
count_pattern('transfer', 'learn')
count_pattern('bay', 'naiv')
count_pattern('year', 'recent')
count_pattern('model', 'probabilist')
count_pattern('neighbor', 'nearest')
count_pattern('analysi', 'princip')
count_pattern('learn', 'semi-supervis')
count_pattern('squar', 'least')
count_pattern('collabor', 'filter')
count_pattern('model', 'latent')
count_pattern('graph', 'edg')
count_pattern('detect', 'outlier')
count_pattern('process', 'gaussian')
count_pattern('special', 'case')
count_pattern('model', 'markov')
count_pattern('inform', 'retriev')
count_pattern('subgraph', 'graph')
count_pattern('cluster', 'spectral')
count_pattern('prefer', 'user')
count_pattern('scale', 'larg')
count_pattern('learn', 'activ')
count_pattern('learn', 'reinforc')
count_pattern('gene', 'express')
count_pattern('topic', 'model')
count_pattern('system', 'recommend')
count_pattern('use', 'wide')
count_pattern('pattern', 'sequenti')
count_pattern('loss', 'function')
count_patternn('pattern', 'mine', 'frequent')
count_pattern('model', 'gaussian')
count_pattern('model', 'infer')
count_pattern('optim', 'convex')
count_pattern('global', 'local')
count_pattern('associ', 'rule')
count_pattern('text', 'categor')
count_pattern('model', 'build')
count_pattern('tree', 'decis')
count_pattern('dimension', 'reduct')
count_pattern('number', 'small')
count_pattern('dimension', 'high')
count_pattern('node', 'graph')
count_pattern('better', 'perform')
count_pattern('bayesian', 'network')
count_pattern('itemset', 'frequent')
count_pattern('ensembl', 'classifi')
count_pattern('hierarch', 'model')
count_pattern('subspac', 'cluster')
count_pattern('commun', 'network')
count_pattern('model', 'bayesian')
count_pattern('model', 'predict')
count_pattern('compon', 'princip')
count_pattern('matrix', 'factor')
count_pattern('analysi', 'discrimin')
count_pattern('compon', 'analysi')
count_pattern('document', 'word')
count_pattern('user', 'recommend')
count_pattern('comput', 'cost')
count_pattern('hierarch', 'cluster')
count_pattern('discov', 'pattern')
count_pattern('work', 'previou')
count_pattern('select', 'featur')
count_pattern('model', 'regress')
count_pattern('text', 'classif')
count_pattern('field', 'random')
count_pattern('metric', 'learn')
count_pattern('knowledg', 'prior')
count_pattern('model', 'paramet')
count_pattern('time', 'seri')
count_pattern('experi', 'extens')
count_pattern('model', 'variabl')
count_pattern('model', 'probabl')
count_pattern('itemset', 'mine')
count_pattern('perform', 'improv')
count_pattern('social', 'network')
count_pattern('mani', 'applic')
count_pattern('knowledg', 'discoveri')
count_pattern('approach', 'previou')
count_pattern('analysi', 'theoret')
count_pattern('machin', 'learn')
count_pattern('condit', 'model')
count_pattern('relev', 'featur')
count_pattern('featur', 'extract')
count_pattern('model', 'gener')
count_pattern('metric', 'distanc')
count_pattern('distanc', 'function')
count_pattern('improv', 'accuraci')
count_pattern('inform', 'sourc')
count_pattern('model', 'factor')
count_pattern('inform', 'extract')
count_pattern('model', 'estim')
count_pattern('approach', 'novel')
count_pattern('differ', 'type')
count_pattern('pattern', 'discoveri')
count_pattern('class', 'label')
count_patternnn('machin', 'support', 'vector', 'svm')
count_pattern('behavior', 'user')
count_pattern('page', 'web')
count_pattern('case', 'studi')
count_pattern('experi', 'improv')
count_pattern('approach', 'demonstr')
count_pattern('model', 'combin')
count_pattern('item', 'user')
count_pattern('process', 'markov')
count_pattern('model', 'random')
count_pattern('effect', 'demonstr')
count_pattern('signific', 'improv')
count_pattern('larg', 'scalabl')
count_pattern('larg', 'number')
count_pattern('classif', 'accuraci')
count_pattern('estim', 'probabl')
count_pattern('measur', 'similar')
count_pattern('perform', 'significantli')
count_pattern('new', 'introduc')
count_pattern('empir', 'studi')
count_pattern('dataset', 'real-world')
count_pattern('model', 'distribut')
count_pattern('model', 'statist')
count_pattern('object', 'function')
count_pattern('topic', 'document')
count_pattern('featur', 'space')
count_pattern('social', 'commun')
count_pattern('set', 'real-world')
count_pattern('document', 'text')
count_pattern('model', 'document')
count_pattern('import', 'applic')
count_pattern('model', 'dynam')'''


#print_arff_file()
'''count_patternn('support', 'vector', 'svm')
count_patternn('machin', 'support', 'vector') 
count_pattern('regress', 'logist')
count_pattern('squar', 'least')
count_pattern('time', 'seri') 
count_pattern('random', 'walk') 
count_pattern('neighbor', 'nearest') 
count_pattern('compon', 'princip') 
count_pattern('social', 'network') 
count_pattern('mixtur', 'model') 
count_pattern('search', 'engin') 
count_patternn('topic', 'model', 'document') 
count_pattern('model', 'graphic') 
count_pattern('transfer', 'learn') 
count_pattern('year', 'recent') 
count_pattern('model', 'probabilist') 
count_pattern('collabor', 'filter') 
count_pattern('detect', 'anomali') 
count_pattern('learn', 'activ') 
count_pattern('field', 'random') 
count_pattern('detect', 'outlier')
count_pattern('itemset', 'frequent')
count_pattern('model', 'latent') 
count_pattern('dimension', 'reduct') 
count_pattern('scale', 'larg') 
count_pattern('learn', 'semi-supervis') 
count_pattern('process', 'gaussian') 
count_pattern('select', 'featur') 
count_pattern('associ', 'rule') 
count_pattern('cluster', 'spectral') 
count_pattern('loss', 'function') 
count_patternn('pattern', 'mine', 'frequent') 
count_pattern('inform', 'retriev') 
count_pattern('model', 'markov')

#
count_patternn('machin','support','vector')
count_patternn('vector','machin','support')
count_pattern('seri','time')
count_patternn('experi','set','data')
count_pattern('solv','problem')
count_patternn('vector','support','machin')
count_pattern('world','real')
count_patternn('propos','experiment','result')
count_patternn('show','experiment','result')
count_patternn('data','experiment','result')
count_patternn('show','set','data')
count_patternn('method','set','data')
count_patternn('result','set','data')
count_patternn('mine','applic','data')
count_pattern('anomali','detect')
count_pattern('social','network')
count_pattern('stream','data')
count_pattern('experiment','result')
count_patternn('demonstr','experiment','result')
count_pattern('synthet','data')
count_patternn('result','demonstr','experiment')
count_patternn('algorithm','set','data')
count_pattern('synthet','real')
count_patternn('propos','set','data')
count_patternn('use','mine','data')
count_pattern('machin','learn')
count_pattern('outlier','detect')
count_pattern('outperform','show')
count_patternn('propos','result','experiment')
count_pattern('probabilist','model')
count_pattern('vector','support')
count_patternn('method','paper','propos')
count_patternn('result','experiment','show')
count_patternn('propos','result','show')
count_patternn('use','set','data')
count_patternn('paper','novel','propos')
count_pattern('activ','learn')
count_pattern('scale','larg')
count_patternn('method','result','show')
count_pattern('set','data')
count_patternn('propos','novel','paper')
count_patternn('propos','show','result')
count_patternn('problem','mine','data')
count_patternn('paper','model','propos')
count_pattern('mine','data')
count_pattern('frequent','mine')
count_pattern('significantli','show')
count_pattern('real-world','data')
count_pattern('itemset','frequent')
count_patternn('paper','approach','propos')
count_pattern('support','vector')
count_pattern('experiment','show')
count_pattern('vector','machin')
count_pattern('subspac','cluster')
count_patternn('paper','algorithm','propos')
count_patternn('result','show','experiment')
count_patternn('data','applic','mine')
count_pattern('real','data')
count_pattern('topic','model')
count_pattern('point','data')
count_pattern('outperform','method')
count_pattern('machin','vector')
count_patternn('algorithm','mine','data')
count_pattern('select','featur')
count_patternn('experi','data','set')
count_pattern('vector','machin')
count_pattern('machin','support')
count_pattern('avail','data')'''


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


