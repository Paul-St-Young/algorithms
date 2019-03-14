
# pip install python-levenshtein
import Levenshtein as lev
import numpy as np
import string

class WordSearch:
  def __init__(self,wordbank,compare=lev.distance):
    ''' Base class for word searching.'''
    self.wordbank=wordbank
    self.compare=compare
    self.ncompares=0

  def query(self,key):
    ''' Return closest match to key in database.
    Args:
      key (str): 
    Returns:
      str: Closest element in database.
    '''
    raise NotImplementedError()

    return {'word':'','dist':np.inf}

  def statistics(self,nruns):
    # Reset compare counter.
    self.ncompares=0

    # Perform tests.
    for i in range(nruns):
      # Generate a test key that differs from a word by one letter.
      testkey=list(np.random.choice(self.wordbank))
      testkey[np.random.randint(len(testkey))]=np.random.choice(tuple(string.ascii_letters))
      testkey=''.join(testkey)
      
      # Query
      result=self.query(testkey)
      #print(testkey,result)
      assert result['dist']<=1,"Found wrong test key."

    return self.ncompares/nruns

class Brute(WordSearch):
  ''' Brute force algorithm to find closest key in bank by just searching all the keys.'''
  def query(self,key):
    ''' Return closest match to key in database.
    Args:
      key (str): 
    Returns:
      str: Closest element in database.
    '''
    best={'word':'','dist':np.inf}
    for word in self.wordbank:
      dist=self.compare(key,word)
      self.ncompares+=1
      if dist<best['dist']:
        best={'word':word,'dist':dist}
        # Messes with testing, but is more efficient.
        if dist==0: return {'word':word,'dist':0}
    return best

  def print(self,depth=0):
    ''' Print visual representation for purposes.'''
    return depth*'>'+str(self.wordbank)

class BKTree(WordSearch):
  def __init__(self,wordbank,preferred_x0=None,brute_cutoff=2,compare=lev.distance):
    ''' BKTree for finding a closest match to a key in a word bank.

    Algorithm 1 from DOI:10.1145/362003.362025.
    Args:
      wordbank (list): list of words to search through.
      preferred_x0 (str): word you want to measure distances from (default: random from wordbank).
      brute_cutoff (int): maximum size for brute force search of subtree.
      compare (func): function to compare strings. Must satistfy triangle inequality.
    '''
    self.wordbank=np.unique(wordbank)
    self.compare=compare
    self.children={}
    self.ncompares=0

    # Determine chosen word.
    if preferred_x0 is None: 
      self.x0=np.random.choice(self.wordbank)
    else: 
      self.x0=preferred_x0

    # Build the tree.
    self.distances=[self.compare(self.x0,word) for word in self.wordbank]
    for word in self.wordbank:
      dist=self.compare(word,self.x0)
      try:
        self.children[dist].append(word)
      except KeyError:
        self.children[dist]=[word]

    # Recursive structure.
    for key,subbank in self.children.items():
      if len(subbank)<=brute_cutoff:
        self.children[key]=Brute(subbank,compare=self.compare)
      else:
        self.children[key]=BKTree(subbank,brute_cutoff=2,compare=self.compare)

  def print(self,depth=0):
    output=[]
    output+=[depth*'>'+'BKTree']
    for key,child in self.children.items():
      output+=[child.print(depth+1)]
    return '\n'.join(output)

  def query(self,key):
    jdist=self.compare(self.x0,key)
    best={'word':self.x0,'dist':jdist}

    # Search child trees.
    for child_dist,child in self.children.items():

      # Apply joint cutoff criterion.
      if abs(child_dist - jdist) < best['dist']:
        child.ncompares=0
        new=child.query(key)
        self.ncompares+=child.ncompares

        # Possibly update keys and best distance.
        if best['dist'] > new['dist']:
          best=new

    return best

###########################################################################################
# Testing suite
def sanitytest():
  #np.random.seed(0)
  wordbank=np.random.choice(open('/usr/share/dict/words','r').read().split(),100)
  searcher=Brute(wordbank)
  assert searcher.statistics(10)<=100
  print("Sanity test passed")

def brutetest():
  wordbank=open('/usr/share/dict/words','r').read().split()
  for size in np.linspace(10,len(wordbank),100,dtype=int):
    bank=np.random.choice(wordbank,size)
    brute=Brute(bank.copy())
    bk=BKTree(bank.copy())
    brute_ans=brute.query('this')
    bk_ans=bk.query('this')
    assert brute_ans['dist']==bk_ans['dist']
  print("Brute test passed")

def statistics():
  print("Statistics")
  bank=open('/usr/share/dict/words','r').read().split()
  print("Number of words")
  print(len(bank))
  brute=Brute(bank.copy())
  bk=BKTree(bank.copy())

  print("Brute:")
  print(brute.statistics(500))

  print("BK:")
  print(bk.statistics(500))

def languages():
  import os
  import pickle

  # Source: http://www.gwicks.net/dictionaries.htm

  french=BKTree(open('espanol.txt','r',encoding='latin-1').read().split('\n'))

if __name__=='__main__':
  #sanitytest()
  #brutetest()
  #statistics()
  languages()
